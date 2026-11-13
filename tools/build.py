"""Generate the MTG Arena learning datapack. Run from any working directory."""
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
FUN = ROOT / "data/mtga/function"
CARDS = {
    1: ("Mountain", 0, 0, 0, "Land: add one red mana each turn."),
    2: ("Forest", 0, 0, 0, "Land: add one green mana each turn."),
    3: ("Goblin Piker", 2, 2, 1, "Creature - Goblin Warrior"),
    4: ("Grizzly Bears", 2, 2, 2, "Creature - Bear"),
    5: ("Hill Giant", 4, 3, 3, "Creature - Giant"),
    6: ("Spined Wurm", 5, 5, 4, "Creature - Wurm"),
    7: ("Shock", 1, 0, 0, "Deal 2 damage to your opponent. Main phase only in this prototype."),
    8: ("Nourish", 2, 0, 0, "Gain 6 life. Main phase only in this prototype."),
}
TRIGGERS = ["menu", "play", "attack", "block", "end"]
OUTPUTS = {}
MANIFEST = ROOT / "tools/generated.json"


def write(path, value):
    OUTPUTS[path] = value


def fn(name, lines):
    if isinstance(lines, str):
        lines = lines.strip().splitlines()
    lines = [("$" + line if "$(" in line and not line.startswith("$") else line) for line in lines]
    write(f"data/mtga/function/{name}.mcfunction", "\n".join(lines) + "\n")


def set_(key, n):
    return f"scoreboard players set #{key} mtg {n}"


def op(a, sign, b):
    return f"scoreboard players operation #{a} mtg {sign} #{b} mtg"


def cond(key, value, command):
    return f"execute if score #{key} mtg matches {value} run {command}"


def call(name):
    return f"function mtga:{name}"


def macrocall(name, **args):
    return call(name) + " " + json.dumps(args, separators=(",", ":"))


def digest(value):
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def finish():
    """Only remove obsolete outputs recorded by an earlier build, if unchanged."""
    previous = json.loads(MANIFEST.read_text(encoding="utf-8")) if MANIFEST.exists() else {}
    obsolete = previous.keys() - OUTPUTS.keys()
    for name in obsolete:
        path = (ROOT / name).resolve()
        if not path.is_relative_to(FUN.resolve()):
            raise SystemExit(f"Refusing to remove output outside function directory: {name}")
        if path.exists() and digest(path.read_text(encoding="utf-8")) != previous[name]:
            raise SystemExit(f"Refusing to remove modified generated file: {name}")
    manifest = json.dumps({name: digest(value) for name, value in sorted(OUTPUTS.items())}, indent=2) + "\n"
    if "--check" in sys.argv:
        stale = [name for name, value in OUTPUTS.items()
                 if not (ROOT / name).exists() or (ROOT / name).read_text(encoding="utf-8") != value]
        stale += [name for name in obsolete if (ROOT / name).exists()]
        if not MANIFEST.exists() or MANIFEST.read_text(encoding="utf-8") != manifest:
            stale.append("tools/generated.json")
        if stale:
            raise SystemExit("Generated outputs are stale:\n" + "\n".join(stale))
        print("PASS: generated outputs and manifest are up to date.")
        return
    for name, value in OUTPUTS.items():
        path = ROOT / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(value, encoding="utf-8")
    for name in obsolete:
        (ROOT / name).unlink(missing_ok=True)
    MANIFEST.write_text(manifest, encoding="utf-8")
    count = sum(name.endswith(".mcfunction") for name in OUTPUTS)
    print(f"Generated {count} functions; removed {len(obsolete)} obsolete outputs.")


def text(value, color="gray"):
    return {"text": value, "color": color}


def score(key):
    return {"score": {"name": f"#{key}", "objective": "mtg"}, "color": "white"}


def button(label, objective, value, hint=""):
    c = text(label, "aqua")
    c["click_event"] = {"action": "run_command", "command": f"/trigger mtg.{objective} set {value}"}
    if hint:
        c["hover_event"] = {"action": "show_text", "value": text(hint, "white")}
    return c


def tell(target, components):
    if isinstance(components, str):
        components = text(components)
    return "tellraw " + target + " " + json.dumps(components, separators=(",", ":"))


def announce(message):
    return tell("@a[tag=mtga.player]", text(message, "gold"))


write("pack.mcmeta", json.dumps({"pack": {
    "description": "MTG Arena | Learning duels: PvP + solo bot | Java 26.3",
    "min_format": [121, 0], "max_format": [121, 0]
}}, indent=2) + "\n")
for tag in ("load", "tick"):
    write(f"data/minecraft/tags/function/{tag}.json",
          json.dumps({"values": [f"mtga:{tag}"]}, indent=2) + "\n")

fn("load", [
    "execute unless data storage mtga:meta installed run function mtga:install",
    tell("@a", [text("[MTG] ", "gold"), text("Ready. "), button("[Open menu]", "menu", 1),
                text(" or /trigger mtg.menu set 1")]),
])
fn("install", [
    "scoreboard objectives add mtg dummy",
    "scoreboard objectives add mtg.session dummy",
    *[f"scoreboard objectives add mtg.{t} trigger" for t in TRIGGERS],
    set_("installed", 1), set_("active", 0), set_("bot", 0), set_("session", 0),
    "data modify storage mtga:meta installed set value 1b",
])
fn("tick", [
    "execute as @a[tag=mtga.player] unless score @s mtg.session = #session mtg run function mtga:lobby/clear_tags",
    "execute if score #active mtg matches 0 as @a[tag=mtga.player] run function mtga:lobby/clear_tags",
    *[f"execute as @a[scores={{mtg.{t}=1..}}] run function mtga:input/{t}" for t in TRIGGERS],
    *[f"execute as @a[scores={{mtg.{t}=..-1}}] run scoreboard players set @s mtg.{t} 0" for t in TRIGGERS],
    *[f"scoreboard players enable @a mtg.{t}" for t in TRIGGERS],
    "execute if score #active mtg matches 1 if score #bot mtg matches 1 run function mtga:bot/tick",
])
fn("lobby/clear_tags", [
    "tag @s remove mtga.player", "tag @s remove mtga.p1", "tag @s remove mtga.p2",
])
fn("menu", [
    tell("@s", text("=== MTG Arena: learning duels ===", "gold")),
    tell("@s", [button("[Solo: Red vs Green bot]", "menu", 2), text("  "),
                button("[Host PvP: Red]", "menu", 3), text("  "), button("[Join: Green]", "menu", 4)]),
    tell("@s", [button("[View match / hand]", "menu", 6), text("  "),
                button("[Concede / cancel lobby]", "menu", 5)]),
    tell("@s", "One match per world. No inventory or terrain changes. Open chat (T) to click."),
    tell("@s", "Main: play cards, select attackers, then End. Defense: assign blockers, then Resolve."),
])
fn("input/menu", [
    "scoreboard players operation #request mtg = @s mtg.menu",
    "scoreboard players set @s mtg.menu 0",
    cond("request", 1, call("menu")),
    cond("request", 2, call("lobby/solo")),
    cond("request", 3, call("lobby/host")),
    cond("request", 4, call("lobby/join")),
    cond("request", 5, call("lobby/concede")),
    cond("request", 6, call("view")),
])
for mode in ("solo", "host"):
    fn(f"lobby/{mode}", [
        'execute unless score #active mtg matches 0 run return run ' +
        tell("@s", "A match or lobby already exists. Finish it or have its host cancel."),
        "tag @a remove mtga.p1", "tag @a remove mtga.p2", "tag @a remove mtga.player",
        "scoreboard players add #session mtg 1",
        "scoreboard players operation @s mtg.session = #session mtg",
        "tag @s add mtga.p1", "tag @s add mtga.player",
        set_("bot", 1 if mode == "solo" else 0),
        *([call("game/start")] if mode == "solo" else [
            set_("active", 2),
            tell("@a", [text("[MTG] A PvP lobby is open. ", "gold"), button("[Join Green deck]", "menu", 4)]),
        ]),
    ])
fn("lobby/join", [
    "execute unless score #active mtg matches 2 run return run " + tell("@s", "No open PvP lobby."),
    "execute if entity @s[tag=mtga.p1] run return run " + tell("@s", "Wait for another player to join."),
    "scoreboard players operation @s mtg.session = #session mtg",
    "tag @s add mtga.p2", "tag @s add mtga.player", call("game/start"),
])
fn("lobby/concede", [
    "execute unless entity @s[tag=mtga.player] run return 0",
    "execute if score #active mtg matches 2 run return run function mtga:game/stop",
    "execute unless score #active mtg matches 1 run return 0",
    "execute if entity @s[tag=mtga.p1] run scoreboard players set #winner mtg 2",
    "execute if entity @s[tag=mtga.p2] run scoreboard players set #winner mtg 1",
    call("game/finish"),
])
fn("game/start", [
    set_("active", 1), set_("phase", 1), set_("turn", 1), set_("winner", 0),
    set_("round", 1), set_("delay", 0),
    *[set_(f"{key}{s}", n) for s in (1, 2)
      for key, n in [("life", 20), ("lands", 0), ("mana", 0), ("landed", 0), ("grave", 0)]],
    *[set_(f"h{s}_{h}", 0) for s in (1, 2) for h in range(1, 25)],
    *[set_(f"{key}{s}_{b}", 0) for s in (1, 2) for b in range(1, 6)
      for key in ("c", "p", "t", "r", "tap", "a", "b", "used")],
    "data modify storage mtga:game deck1 set value " + json.dumps([1]*10+[3]*6+[5]*4+[7]*4),
    "data modify storage mtga:game deck2 set value " + json.dumps([2]*10+[4]*6+[6]*4+[8]*4),
    *[call(f"seat/{s}/draw") for _ in range(7) for s in (1, 2)],
    announce("Duel started! Red is seat 1; Green is seat 2. Red takes the first turn (no first draw)."),
    call("game/refresh"),
])
fn("game/stop", [
    set_("active", 0), announce("Match / lobby closed. Open the menu to play again."),
    "tag @a remove mtga.player", "tag @a remove mtga.p1", "tag @a remove mtga.p2",
])
fn("game/check", [
    "execute unless score #active mtg matches 1 run return 0",
    cond("life1", "..0", set_("winner", 2)),
    cond("life2", "..0", set_("winner", 1)),
    cond("winner", "1..2", call("game/finish")),
])
fn("game/finish", [
    cond("winner", 1, announce("Red wins the duel!")),
    cond("winner", 2, announce("Green wins the duel!")),
    call("game/stop"),
])
fn("game/refresh", [
    "execute if score #active mtg matches 1 as @a[tag=mtga.player] run function mtga:view",
])
fn("view", [
    "execute unless entity @s[tag=mtga.player] run return run function mtga:menu",
    "execute unless score #active mtg matches 1 run return run function mtga:menu",
    tell("@s", [text("=== MTG | Turn ", "gold"), score("round"), text(" | Active seat: "), score("turn"),
                text(" | Phase 1=main, 2=blocks: "), score("phase")]),
    *[tell("@s", [text(f"{'Red' if s == 1 else 'Green'} | Life: ", "red" if s == 1 else "green"),
                  score(f"life{s}"), text(" | Mana: "), score(f"mana{s}"),
                  text(" / "), score(f"lands{s}"), text(" | Graveyard: "), score(f"grave{s}")])
      for s in (1, 2)],
    *[f"execute if entity @s[tag=mtga.p{s}] run function mtga:seat/{s}/view" for s in (1, 2)],
    tell("@s", [button("[End main / Resolve blocks]", "end", 1), text("  "),
                button("[Refresh]", "menu", 6), text("  "), button("[Menu]", "menu", 1)]),
])

for s in (1, 2):
    o = 3-s
    prefix = f"seat/{s}"
    # Slot macros receive bounded integer arguments from dispatchers below.
    fn(f"{prefix}/draw_pick", [
        f"$execute store result score #draw mtg run data get storage mtga:game deck{s}[$(index)]",
        f"$data remove storage mtga:game deck{s}[$(index)]",
    ])
    fn(f"{prefix}/draw", [
        "execute unless score #active mtg matches 1 run return 0",
        f"execute store result score #count mtg run data get storage mtga:game deck{s}",
        "execute if score #count mtg matches 0 run return run function " + f"mtga:{prefix}/deck_loss",
        "scoreboard players remove #count mtg 1",
        "execute store result storage mtga:args max int 1 run scoreboard players get #count mtg",
        call(f"{prefix}/random") + " with storage mtga:args",
        call(f"{prefix}/draw_pick") + " with storage mtga:args",
        *[f"execute if score #h{s}_{h} mtg matches 0 run return run " +
          op(f"h{s}_{h}", "=", "draw") for h in range(1, 25)],
    ])
    fn(f"{prefix}/random", [
        "$execute store result storage mtga:args index int 1 run random value 0..$(max)",
    ])
    fn(f"{prefix}/deck_loss", [set_("winner", o),
                               announce(f"Seat {s} cannot draw: empty library."), call("game/finish")])
    view = [tell("@s", text("Your hand (click a card to play it):", "yellow"))]
    for h in range(1, 25):
        for cid, (name, cost, power, tough, desc) in CARDS.items():
            label = f"[{h}: {name}" + (f" | {cost} mana" if cid > 2 else " | land") + (
                f" | {power}/{tough}" if power else "") + "] "
            view.append(cond(f"h{s}_{h}", cid, tell("@s", button(label, "play", h, desc))))
    view.append(tell("@s", text("Battlefields: R=can attack; T=tapped; A=attacking; B=blocker slot.", "yellow")))
    for owner in (s, o):
        for b in range(1, 6):
            for cid, (name, cost, power, tough, desc) in CARDS.items():
                if not power:
                    continue
                row = [text(f"{'You' if owner == s else 'Enemy'} {b}: {name} {power}/{tough} "),
                       text("R:"), score(f"r{owner}_{b}"), text(" T:"), score(f"tap{owner}_{b}"),
                       text(" A:"), score(f"a{owner}_{b}"), text(" B:"), score(f"b{owner}_{b}")]
                if owner == s:
                    row += [text(" "), button("[Toggle attack]", "attack", b)]
                view.append(cond(f"c{owner}_{b}", cid, tell("@s", row)))
    view += [
        f"execute if score #phase mtg matches 2 unless score #turn mtg matches {s} run function mtga:{prefix}/block_menu",
        tell("@s", "Attackers are selected before End main. Block code = enemy slot * 10 + your slot (e.g. 23)."),
    ]
    fn(f"{prefix}/view", view)
    fn(f"{prefix}/block_menu", [
        tell("@s", text("Assign one untapped blocker per attacker. Reassigning frees the old blocker.", "yellow")),
        *[cond(f"a{o}_{a}", 1, tell("@s", [
            text(f"Enemy attacker {a}: "),
            *[button(f"[Block with {b}] ", "block", a*10+b) for b in range(1, 6)],
            button("[Unblock]", "block", a*10),
        ])) for a in range(1, 6)],
    ])
    fn(f"{prefix}/play", [
        f"execute unless score #turn mtg matches {s} run return 0",
        "execute unless score #phase mtg matches 1 run return 0",
        *[cond("request", h, macrocall(f"{prefix}/hand", h=h)) for h in range(1, 25)],
    ])
    fn(f"{prefix}/hand", [
        op("card", "=", f"h{s}_$(h)"), set_("played", 0),
        *[cond("card", cid, call(f"{prefix}/card/{cid}")) for cid in CARDS],
        cond("played", 1, set_(f"h{s}_$(h)", 0)),
    ])
    for cid, (name, cost, power, tough, desc) in CARDS.items():
        lines = []
        if cid <= 2:
            lines += [
                f"execute if score #landed{s} mtg matches 1 run return 0",
                f"scoreboard players add #lands{s} mtg 1",
                f"scoreboard players add #mana{s} mtg 1", set_(f"landed{s}", 1),
            ]
        else:
            lines += [f"execute unless score #mana{s} mtg matches {cost}.. run return 0"]
            if power:
                lines += [set_("slot", 0)]
                lines += [f"execute if score #slot mtg matches 0 if score #c{s}_{b} mtg matches 0 run " +
                          set_("slot", b) for b in range(1, 6)]
                lines += ["execute if score #slot mtg matches 0 run return 0"]
                for b in range(1, 6):
                    for key, n in [("c", cid), ("p", power), ("t", tough),
                                   ("r", 0), ("tap", 0), ("a", 0), ("b", 0), ("used", 0)]:
                        lines.append(cond("slot", b, set_(f"{key}{s}_{b}", n)))
            else:
                lines += [f"scoreboard players add #grave{s} mtg 1"]
                lines += ([f"scoreboard players remove #life{o} mtg 2"] if cid == 7 else
                          [f"scoreboard players add #life{s} mtg 6"])
            lines += [f"scoreboard players remove #mana{s} mtg {cost}"]
        lines += [set_("played", 1), announce(f"Seat {s} plays {name}.")]
        fn(f"{prefix}/card/{cid}", lines)
    fn(f"{prefix}/attack", [
        f"execute unless score #turn mtg matches {s} run return 0",
        "execute unless score #phase mtg matches 1 run return 0",
        *[cond("request", b, macrocall(f"{prefix}/toggle", b=b)) for b in range(1, 6)],
    ])
    fn(f"{prefix}/toggle", [
        f"execute unless score #c{s}_$(b) mtg matches 1.. run return 0",
        f"execute unless score #r{s}_$(b) mtg matches 1 run return 0",
        f"execute unless score #tap{s}_$(b) mtg matches 0 run return 0",
        op("old", "=", f"a{s}_$(b)"), set_(f"a{s}_$(b)", 1),
        cond("old", 1, set_(f"a{s}_$(b)", 0)),
    ])
    fn(f"{prefix}/block", [
        f"execute if score #turn mtg matches {s} run return 0",
        "execute unless score #phase mtg matches 2 run return 0",
        *[cond("request", a*10+b, macrocall(f"{prefix}/block_pair", a=a, b=b))
          for a in range(1, 6) for b in range(0, 6)],
    ])
    fn(f"{prefix}/block_pair", [
        f"execute unless score #a{o}_$(a) mtg matches 1 run return 0",
        set_("blocker", "$(b)"),
        *[f"execute unless score #blocker mtg matches 0 unless score #{key}{s}_$(b) mtg matches {value} run return 0"
          for key, value in (("c", "1.."), ("tap", "0"), ("used", "0"))],
        *[cond(f"b{o}_$(a)", prev, set_(f"used{s}_{prev}", 0)) for prev in range(1, 6)],
        set_(f"b{o}_$(a)", "$(b)"),
        f"execute unless score #blocker mtg matches 0 run " + set_(f"used{s}_$(b)", 1),
    ])
    fn(f"{prefix}/end", [
        f"execute if score #phase mtg matches 1 if score #turn mtg matches {s} run return run function mtga:{prefix}/commit",
        f"execute if score #phase mtg matches 2 unless score #turn mtg matches {s} run function mtga:game/combat",
    ])
    fn(f"{prefix}/commit", [
        set_("attackers", 0),
        *[f"execute if score #a{s}_{b} mtg matches 1 run scoreboard players add #attackers mtg 1"
          for b in range(1, 6)],
        *[cond(f"a{s}_{b}", 1, set_(f"tap{s}_{b}", 1)) for b in range(1, 6)],
        "execute if score #attackers mtg matches 0 run return run function mtga:game/next",
        set_("phase", 2), set_("delay", 0),
        announce(f"Seat {s} attacks. Seat {o}: assign blockers, then click Resolve blocks."),
    ])
    fn(f"{prefix}/begin", [
        set_(f"landed{s}", 0), op(f"mana{s}", "=", f"lands{s}"),
        *[set_(f"tap{s}_{b}", 0) for b in range(1, 6)],
        *[cond(f"c{s}_{b}", "1..", set_(f"r{s}_{b}", 1)) for b in range(1, 6)],
        call(f"{prefix}/draw"),
    ])
    # End-step hand-size limit: automatically discard highest hand slots.
    fn(f"{prefix}/cleanup", [
        set_("handcount", 0),
        *[f"execute if score #h{s}_{h} mtg matches 1.. run scoreboard players add #handcount mtg 1"
          for h in range(1, 25)],
        *[f"execute if score #handcount mtg matches 8.. if score #h{s}_{h} mtg matches 1.. run " +
          macrocall(f"{prefix}/discard", h=h)
          for h in range(24, 0, -1)],
    ])
    fn(f"{prefix}/discard", [
        set_(f"h{s}_$(h)", 0), "scoreboard players remove #handcount mtg 1",
        f"scoreboard players add #grave{s} mtg 1",
        announce(f"Seat {s} discards hand slot $(h) to the seven-card limit."),
    ])
    # Resolve each pair using pre-damage stats, so both creatures can die.
    fn(f"{prefix}/combat", [
        f"execute if score #b{s}_$(a) mtg matches 0 run return run " +
        op(f"life{o}", "-=", f"p{s}_$(a)"),
        *[cond(f"b{s}_$(a)", b, macrocall(f"{prefix}/fight", a="$(a)", b=b)) for b in range(1, 6)],
    ])
    fn(f"{prefix}/fight", [
        set_("deadA", 0), set_("deadB", 0),
        f"execute if score #p{s}_$(a) mtg >= #t{o}_$(b) mtg run " + set_("deadB", 1),
        f"execute if score #p{o}_$(b) mtg >= #t{s}_$(a) mtg run " + set_("deadA", 1),
        cond("deadA", 1, macrocall(f"{prefix}/die", b="$(a)")),
        cond("deadB", 1, macrocall(f"seat/{o}/die", b="$(b)")),
    ])
    fn(f"{prefix}/die", [
        *[set_(f"{key}{s}_$(b)", 0) for key in ("c", "p", "t", "r", "tap", "a", "b", "used")],
        f"scoreboard players add #grave{s} mtg 1", announce(f"Seat {s}'s creature in slot $(b) dies."),
    ])

for action in ("play", "attack", "block", "end"):
    fn(f"input/{action}", [
        f"scoreboard players operation #request mtg = @s mtg.{action}",
        f"scoreboard players set @s mtg.{action} 0",
        "execute unless score #active mtg matches 1 run return 0",
        *[f"execute if entity @s[tag=mtga.p{s}] run function mtga:seat/{s}/{action}" for s in (1, 2)],
        call("game/check"), call("game/refresh"),
    ])
fn("game/combat", [
    *[f"execute if score #turn mtg matches {s} if score #a{s}_{a} mtg matches 1 run " +
      macrocall(f"seat/{s}/combat", a=a)
      for s in (1, 2) for a in range(1, 6)],
    call("game/check"),
    "execute if score #active mtg matches 1 run function mtga:game/next",
])
fn("game/next", [
    cond("turn", 1, call("seat/1/cleanup")),
    cond("turn", 2, call("seat/2/cleanup")),
    op("previous", "=", "turn"), set_("turn", 1),
    cond("previous", 1, set_("turn", 2)),
    "scoreboard players add #round mtg 1", set_("phase", 1), set_("delay", 0),
    *[set_(f"{key}{s}_{b}", 0) for s in (1, 2) for b in range(1, 6)
      for key in ("a", "b", "used")],
    cond("turn", 1, call("seat/1/begin")),
    cond("turn", 2, call("seat/2/begin")),
])
fn("bot/tick", [
    "scoreboard players add #delay mtg 1",
    "execute unless score #delay mtg matches 30.. run return 0",
    set_("delay", 0),
    "execute if score #turn mtg matches 2 if score #phase mtg matches 1 run return run function mtga:bot/main",
    "execute if score #turn mtg matches 1 if score #phase mtg matches 2 run function mtga:bot/blocks",
])
fn("bot/main", [
    # Land before spells; larger creatures before smaller ones; then life gain.
    *[f"execute if score #h2_{h} mtg matches 2 run " + macrocall("seat/2/hand", h=h) for h in range(1, 25)],
    *[f"execute if score #h2_{h} mtg matches {cid} run " + macrocall("seat/2/hand", h=h)
      for cid in (6, 4, 8) for h in range(1, 25)],
    *[f"execute if score #r2_{b} mtg matches 1 if score #tap2_{b} mtg matches 0 if score #c2_{b} mtg matches 1.. run " +
      set_(f"a2_{b}", 1) for b in range(1, 6)],
    call("game/check"),
    "execute if score #active mtg matches 1 run function mtga:seat/2/commit",
    call("game/refresh"),
])
fn("bot/blocks", [
    *[f"execute if score #a1_{a} mtg matches 1 if score #b1_{a} mtg matches 0 if score #c2_{b} mtg matches 1.. if score #tap2_{b} mtg matches 0 if score #used2_{b} mtg matches 0 run " +
      macrocall("seat/2/block_pair", a=a, b=b)
      for a in range(1, 6) for b in range(1, 6)],
    announce("Green bot has assigned blockers."), call("game/combat"), call("game/refresh"),
])
fn("admin/reset", [
    announce("An administrator reset the MTG match."),
    call("game/stop"),
])

# Keep editable card/deck data available for future expansion.
write("design/cards.json", json.dumps({
    str(cid): dict(name=v[0], cost=v[1], power=v[2], toughness=v[3], text=v[4])
    for cid, v in CARDS.items()
}, indent=2) + "\n")
finish()
