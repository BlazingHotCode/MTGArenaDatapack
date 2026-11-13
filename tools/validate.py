"""Static checks; deliberately not advertised as an in-game command parser."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
functions = ROOT / "data/mtga/function"
errors = []
for path in [ROOT / "pack.mcmeta", *ROOT.rglob("*.json")]:
    try:
        json.loads(path.read_text(encoding="utf-8"))
    except (ValueError, OSError) as exc:
        errors.append(f"{path.relative_to(ROOT)}: {exc}")

refs = 0
sources = {path.relative_to(functions).as_posix().removesuffix(".mcfunction"):
           path.read_text(encoding="utf-8") for path in functions.rglob("*.mcfunction")}
parameters = {name: set(re.findall(r"\$\((\w+)\)", source)) for name, source in sources.items()}
for path in functions.rglob("*.mcfunction"):
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if "$(" in line and not line.startswith("$"):
            errors.append(f"{path.relative_to(ROOT)}:{number}: macro line missing $ prefix")
        for match in re.finditer(r"\bfunction mtga:([a-z0-9_/]+)(.*)$", line):
            name, tail = match.groups()
            refs += 1
            if name not in sources:
                errors.append(f"{path.relative_to(ROOT)}:{number}: missing {name}")
                continue
            if tail.strip().startswith("with storage "):
                continue  # Storage arguments are exercised by game-logic tests.
            try:
                args = json.loads(tail) if tail.strip() else {}
                missing = parameters[name] - args.keys()
                if missing:
                    errors.append(f"{path.relative_to(ROOT)}:{number}: {name} missing arguments {sorted(missing)}")
            except (ValueError, AttributeError):
                errors.append(f"{path.relative_to(ROOT)}:{number}: invalid inline macro arguments")
        if "clickEvent" in line or "hoverEvent" in line:
            errors.append(f"{path.relative_to(ROOT)}:{number}: obsolete text component field")
        if "tellraw " in line:
            payload = line.split("tellraw ", 1)[1].split(" ", 1)[1]
            try:
                json.loads(payload)
            except ValueError:
                errors.append(f"{path.relative_to(ROOT)}:{number}: invalid tellraw JSON")

start = (functions / "game/start.mcfunction").read_text(encoding="utf-8")
cards = json.loads((ROOT / "design/cards.json").read_text(encoding="utf-8"))
for seat in (1, 2):
    match = re.search(rf"deck{seat} set value (\[.*\])", start)
    assert match, f"Missing deck {seat}"
    deck = json.loads(match[1])
    assert len(deck) == 24
    assert all(str(cid) in cards for cid in deck)
    assert deck.count(seat) == 10
    assert start.count(f"function mtga:seat/{seat}/draw") == 7
assert json.loads((ROOT / "pack.mcmeta").read_text())["pack"]["min_format"] == [121, 0]

if errors:
    raise SystemExit("\n".join(errors))
print(f"PASS: metadata/JSON, tellraw payloads, {refs} function references and macro arguments, two 24-card decks.")
print("Minecraft runtime validation still required.")
