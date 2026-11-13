"""Run generated game functions in a small, deliberately limited command model.

This tests game logic, NOT Minecraft syntax, permissions, selectors, or networking.
"""
from pathlib import Path
import hashlib
import json
import random
import re
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1] / "data/mtga/function"
BASELINE = Path(__file__).resolve().parent / "fixtures/duels.json"
RECORD_BASELINE = "--record-baseline" in sys.argv
if RECORD_BASELINE:
    sys.argv.remove("--record-baseline")


class Returned(Exception):
    def __init__(self, value):
        self.value = value


class Game:
    def __init__(self, seed=0):
        self.scores = {}
        self.storage = {"mtga:args": {}, "mtga:game": {}}
        self.random = random.Random(seed)
        self.commands = 0

    def get(self, key):
        return self.scores.get("#" + key, 0)

    def set(self, key, value):
        self.scores["#" + key] = value

    def run(self, name, args=None):
        try:
            for line in (ROOT / (name + ".mcfunction")).read_text(encoding="utf-8").splitlines():
                if line.startswith("$"):
                    assert args is not None
                    line = re.sub(r"\$\((\w+)\)", lambda m: str(args[m[1]]), line[1:])
                if line and not line.startswith("#"):
                    self.command(line)
        except Returned as result:
            return result.value
        return 0

    @staticmethod
    def matches(value, interval):
        if ".." not in interval:
            return value == int(interval)
        lo, hi = interval.split("..")
        return (not lo or value >= int(lo)) and (not hi or value <= int(hi))

    def command(self, line):
        self.commands += 1
        assert self.commands < 2_000_000, "Possible runaway function"
        if line.startswith("return run "):
            raise Returned(self.command(line[11:]))
        if line.startswith("return "):
            raise Returned(int(line[7:]))
        if line.startswith("execute store result "):
            dest, inner = line[21:].split(" run ", 1)
            value = self.command(inner)
            parts = dest.split()
            if parts[0] == "score":
                self.scores[parts[1]] = value
            else:
                assert parts[0] == "storage"
                self.storage[parts[1]][parts[2]] = value
            return value
        if line.startswith("execute "):
            tests, inner = line[8:].split(" run ", 1)
            parts = tests.split()
            while parts:
                polarity, kind = parts[:2]
                assert polarity in ("if", "unless") and kind == "score", tests
                holder, objective, operator = parts[2:5]
                value = self.scores.get(holder)
                assert objective == "mtg"
                if operator == "matches":
                    matched = value is not None and self.matches(value, parts[5])
                    parts = parts[6:]
                else:
                    other = self.scores.get(parts[5])
                    assert parts[6] == "mtg"
                    matched = value is not None and other is not None and {
                        "=": lambda: value == other, ">=": lambda: value >= other,
                        "<=": lambda: value <= other, ">": lambda: value > other,
                        "<": lambda: value < other,
                    }[operator]()
                    parts = parts[7:]
                if matched != (polarity == "if"):
                    return 0
            return self.command(inner)
        if line.startswith("function "):
            parts = line.split(" ", 2)
            assert parts[1].startswith("mtga:")
            args = None
            if len(parts) > 2:
                if parts[2].startswith("with storage "):
                    args = self.storage[parts[2].split()[2]]
                else:
                    args = json.loads(parts[2])
            return self.run(parts[1][5:], args)
        if line.startswith("scoreboard players "):
            parts = line.split()
            action, holder = parts[2:4]
            if action == "get":
                return self.scores[holder]
            if action in ("set", "add", "remove"):
                value = int(parts[5])
                if action == "add":
                    value = self.scores.get(holder, 0) + value
                elif action == "remove":
                    value = self.scores.get(holder, 0) - value
                self.scores[holder] = value
                return value
            assert action == "operation"
            other = self.scores[parts[6]]
            operator = parts[5]
            self.scores[holder] = {
                "=": lambda: other, "+=": lambda: self.scores[holder] + other,
                "-=": lambda: self.scores[holder] - other,
            }[operator]()
            return self.scores[holder]
        if line.startswith("data modify storage "):
            _, _, _, store, path, _, _, value = line.split(" ", 7)
            self.storage[store][path] = json.loads(value)
            return 1
        if line.startswith(("data get storage ", "data remove storage ")):
            parts = line.split()
            store, path = parts[3:5]
            indexed = re.fullmatch(r"(\w+)\[(\d+)\]", path)
            if indexed:
                array = self.storage[store][indexed[1]]
                index = int(indexed[2])
                return array.pop(index) if parts[1] == "remove" else array[index]
            value = self.storage[store][path]
            return len(value) if isinstance(value, list) else value
        if line.startswith("random value "):
            lo, hi = map(int, line.split()[-1].split(".."))
            return self.random.randint(lo, hi)
        if line.startswith(("tellraw ", "tag ")):
            return 1
        raise AssertionError("Unsupported modeled command: " + line)

class Rules(unittest.TestCase):
    def game(self, seed=0):
        g = Game(seed)
        # Skip UI dispatch, which needs player selector evaluation.
        original = g.command

        def no_view(line):
            if line == "function mtga:game/refresh":
                return 0
            return original(line)

        g.command = no_view
        g.set("bot", 1)
        g.run("game/start")
        return g

    def creature(self, g, seat, slot, power, toughness, ready=1):
        for key, value in [("c", 3), ("p", power), ("t", toughness), ("r", ready),
                           ("tap", 0), ("a", 0), ("b", 0), ("used", 0)]:
            g.set(f"{key}{seat}_{slot}", value)

    def test_opening_and_draws(self):
        for seed in range(20):
            g = self.game(seed)
            for s in (1, 2):
                self.assertEqual(g.get(f"life{s}"), 20)
                self.assertEqual(sum(g.get(f"h{s}_{h}") > 0 for h in range(1, 25)), 7)
                self.assertEqual(len(g.storage["mtga:game"][f"deck{s}"]), 17)
            g.run("seat/1/commit")
            self.assertEqual(g.get("turn"), 2)
            self.assertEqual(len(g.storage["mtga:game"]["deck2"]), 16)

    def test_land_mana_cost_and_sickness(self):
        g = self.game()
        g.set("h1_1", 1)
        g.set("h1_2", 1)
        g.set("h1_3", 3)
        g.run("seat/1/hand", {"h": 1})
        self.assertEqual(g.get("mana1"), 1)
        g.run("seat/1/hand", {"h": 2})
        self.assertEqual(g.get("h1_2"), 1)
        g.run("seat/1/hand", {"h": 3})
        self.assertEqual(g.get("h1_3"), 3)  # Can't afford it.
        g.set("mana1", 2)
        g.run("seat/1/hand", {"h": 3})
        self.assertEqual(g.get("mana1"), 0)
        self.assertEqual(g.get("c1_1"), 3)
        g.run("seat/1/toggle", {"b": 1})
        self.assertEqual(g.get("a1_1"), 0)

    def test_simultaneous_lethal_trade(self):
        g = self.game()
        self.creature(g, 1, 1, 2, 2)
        self.creature(g, 2, 1, 2, 1, ready=0)  # Summoning sickness doesn't prevent blocks.
        g.run("seat/1/toggle", {"b": 1})
        g.run("seat/1/commit")
        self.assertEqual(g.get("phase"), 2)
        self.assertEqual(g.get("tap1_1"), 1)
        g.run("seat/2/block_pair", {"a": 1, "b": 1})
        g.run("game/combat")
        self.assertEqual(g.get("c1_1"), 0)
        self.assertEqual(g.get("c2_1"), 0)
        self.assertEqual(g.get("life2"), 20)
        self.assertEqual(g.get("grave1"), 1)
        self.assertEqual(g.get("grave2"), 1)

    def test_reassign_and_tapped_blocker(self):
        g = self.game()
        for s in (1, 2):
            for slot in (1, 2):
                self.creature(g, s, slot, 2, 2)
        for slot in (1, 2):
            g.run("seat/1/toggle", {"b": slot})
        g.run("seat/1/commit")
        g.run("seat/2/block_pair", {"a": 1, "b": 1})
        g.run("seat/2/block_pair", {"a": 2, "b": 1})  # Already used.
        self.assertEqual(g.get("b1_2"), 0)
        g.run("seat/2/block_pair", {"a": 1, "b": 2})
        self.assertEqual(g.get("used2_1"), 0)
        g.run("seat/2/block_pair", {"a": 2, "b": 1})
        self.assertEqual(g.get("b1_2"), 1)
        g.run("seat/2/block_pair", {"a": 1, "b": 0})
        self.assertEqual(g.get("used2_2"), 0)
        g.set("tap2_2", 1)
        g.run("seat/2/block_pair", {"a": 1, "b": 2})
        self.assertEqual(g.get("b1_1"), 0)

    def test_unblocked_damage_and_turn_reset(self):
        g = self.game()
        self.creature(g, 1, 1, 3, 3)
        g.run("seat/1/toggle", {"b": 1})
        g.run("seat/1/commit")
        g.run("game/combat")
        self.assertEqual(g.get("life2"), 17)
        self.assertEqual(g.get("tap1_1"), 1)
        g.run("seat/2/commit")
        self.assertEqual(g.get("turn"), 1)
        self.assertEqual(g.get("tap1_1"), 0)
        self.assertEqual(g.get("a1_1"), 0)

    def test_spells_board_limit_and_cleanup(self):
        g = self.game()
        g.set("mana1", 10)
        g.set("h1_1", 7)
        g.run("seat/1/hand", {"h": 1})
        self.assertEqual(g.get("life2"), 18)
        self.assertEqual(g.get("mana1"), 9)
        g.set("mana2", 2)
        g.set("h2_1", 8)
        g.run("seat/2/hand", {"h": 1})
        self.assertEqual(g.get("life2"), 24)
        for b in range(1, 6):
            self.creature(g, 1, b, 2, 2)
        g.set("h1_1", 3)
        g.run("seat/1/hand", {"h": 1})
        self.assertEqual(g.get("h1_1"), 3)
        self.assertEqual(g.get("mana1"), 9)
        for h in range(1, 11):
            g.set(f"h1_{h}", 1)
        g.run("seat/1/cleanup")
        self.assertEqual(sum(g.get(f"h1_{h}") > 0 for h in range(1, 25)), 7)
        self.assertEqual(g.get("h1_10"), 0)

    def test_empty_library_and_lethal_shock(self):
        g = self.game()
        g.storage["mtga:game"]["deck1"] = []
        g.run("seat/1/draw")
        self.assertEqual(g.get("winner"), 2)
        self.assertEqual(g.get("active"), 0)
        g = self.game()
        g.set("life2", 2)
        g.set("mana1", 1)
        g.set("h1_1", 7)
        g.run("seat/1/hand", {"h": 1})
        g.run("game/check")
        self.assertEqual(g.get("winner"), 1)
        self.assertEqual(g.get("active"), 0)

    def test_slot_dispatch_and_invalid_requests(self):
        for seat in (1, 2):
            for hand in range(1, 25):
                g = self.game()
                g.set("turn", seat)
                g.set(f"h{seat}_{hand}", seat)
                g.set("request", hand)
                g.run(f"seat/{seat}/play")
                self.assertEqual(g.get(f"h{seat}_{hand}"), 0)
                self.assertEqual(g.get(f"lands{seat}"), 1)
            for slot in range(1, 6):
                g = self.game()
                g.set("turn", seat)
                self.creature(g, seat, slot, 2, 2)
                g.set("request", slot)
                g.run(f"seat/{seat}/attack")
                self.assertEqual(g.get(f"a{seat}_{slot}"), 1)
            for action in ("play", "attack", "block"):
                g = self.game()
                g.set("turn", seat if action != "block" else 3-seat)
                g.set("phase", 2 if action == "block" else 1)
                for request in (-1, 0, 6 if action == "attack" else 999):
                    before = dict(g.scores)
                    before["#request"] = request
                    g.set("request", request)
                    g.run(f"seat/{seat}/{action}")
                    self.assertEqual(g.scores, before)

    def test_every_block_and_combat_pair(self):
        for seat in (1, 2):
            other = 3-seat
            for attacker in range(1, 6):
                for blocker in range(1, 6):
                    g = self.game()
                    g.set("turn", other)
                    self.creature(g, other, attacker, 2, 2)
                    self.creature(g, seat, blocker, 2, 2)
                    g.set(f"a{other}_{attacker}", 1)
                    g.set("phase", 2)
                    g.set("request", attacker*10+blocker)
                    g.run(f"seat/{seat}/block")
                    self.assertEqual(g.get(f"b{other}_{attacker}"), blocker)
                    g.run("game/combat")
                    self.assertEqual(g.get(f"c{other}_{attacker}"), 0)
                    self.assertEqual(g.get(f"c{seat}_{blocker}"), 0)
                    self.assertEqual(g.get(f"grave{seat}"), 1)
                    self.assertEqual(g.get(f"grave{other}"), 1)

    def test_bot_and_long_games(self):
        results = []
        for seed in range(30):
            g = self.game(seed)
            trace = hashlib.sha256()
            # A simple Red policy versus the shipped Green policy.
            for _ in range(150):
                if g.get("active") == 0:
                    break
                if g.get("phase") == 2:
                    g.run("bot/blocks" if g.get("turn") == 1 else "game/combat")
                elif g.get("turn") == 2:
                    g.run("bot/main")
                else:
                    for cid in (1, 5, 3, 7):
                        for h in range(1, 25):
                            if g.get(f"h1_{h}") == cid:
                                g.run("seat/1/hand", {"h": h})
                    g.run("game/check")
                    if not g.get("active"):
                        break
                    for b in range(1, 6):
                        g.run("seat/1/toggle", {"b": b})
                    g.run("seat/1/commit")
                for seat in (1, 2):
                    self.assertGreaterEqual(g.get(f"mana{seat}"), 0)
                    self.assertLessEqual(g.get(f"mana{seat}"), g.get(f"lands{seat}"))
                    cards = len(g.storage["mtga:game"][f"deck{seat}"])
                    cards += sum(g.get(f"h{seat}_{h}") > 0 for h in range(1, 25))
                    cards += sum(g.get(f"c{seat}_{b}") > 0 for b in range(1, 6))
                    cards += g.get(f"lands{seat}") + g.get(f"grave{seat}")
                    self.assertEqual(cards, 24)
                state = {
                    "scores": {k: v for k, v in g.scores.items() if re.fullmatch(
                        r"#(?:active|bot|phase|turn|winner|round|delay|"
                        r"(?:life|lands|mana|landed|grave)[12]|"
                        r"(?:h|c|p|t|r|tap|a|b|used)[12]_\d+)", k)},
                    "decks": g.storage["mtga:game"],
                }
                trace.update(json.dumps(state, sort_keys=True).encode("utf-8"))
            self.assertEqual(g.get("active"), 0, f"Seed {seed} did not finish")
            results.append({"seed": seed, "winner": g.get("winner"),
                            "round": g.get("round"), "trace": trace.hexdigest()})
        if RECORD_BASELINE:
            BASELINE.parent.mkdir(parents=True, exist_ok=True)
            BASELINE.write_text(json.dumps(results, indent=2) + "\n", encoding="utf-8")
        else:
            self.assertEqual(results, json.loads(BASELINE.read_text(encoding="utf-8")),
                             "Game behavior changed from the pre-macro baseline")


if __name__ == "__main__":
    unittest.main(verbosity=2)
