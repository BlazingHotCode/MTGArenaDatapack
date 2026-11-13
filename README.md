# MTG Arena — Minecraft learning duels

A fan-made **Java Edition 26.3** datapack (data format **121.0**).
Playable chat-based prototype, not a recreation of the full MTG rules engine.
No mods or resource pack required. Does not alter inventory, terrain, health,
gamemode, or other packs' scoreboards.

## Project status

The current release is a **chat-based rules prototype**, not an Arena-style
interface. Card selection and combat state can be difficult to follow in chat.
The next priority is clearer turn guidance and a visual battlefield, rather
than more cards.

Planned interface improvements include visible tapped/summoning-sickness states,
highlighted attackers, and connections between attackers and blockers. These are
**not implemented yet**. Custom card artwork would need a resource pack; a fully
custom Arena-like screen may need a client mod.

## Start

1. Back up your world.
2. This folder is already in `datapacks`; keep `pack.mcmeta` directly inside it.
3. Run `/reload` (requires cheats/operator), or reopen the world.
4. Run `/trigger mtg.menu set 1`.
5. Open chat with **T** and click **Solo**, or **Host PvP**.
   For PvP, the other player clicks **Join**.

Normal play uses `/trigger`, so players do not need operator permissions.
Only one match/lobby can exist in the world at a time. Red goes first.

## Playing

- Click cards in your private hand to play them. One land per turn.
- Lands automatically supply fresh mana at the start of your turn.
  Playing a land also supplies one mana immediately.
- Creatures cannot attack on the turn they enter play.
- Select **Toggle attack** on each creature you want to attack with.
  Click **End main** to commit those attacks.
- The defender selects one untapped creature for each attacker and clicks
  **Resolve blocks**. A creature can block even if it was just summoned.
- Unblocked attackers damage the opponent. Blocked creatures deal simultaneous
  damage to each other. Surviving creatures recover after combat.
- You win when your opponent reaches zero life or must draw from an empty deck.
- **Refresh** displays current boards and your own hand.
- **Concede** ends your match; a lobby host can use it to cancel their lobby.

### Reading creature states

| Chat label / term | Meaning |
| --- | --- |
| **Slot** | A numbered position, not a card identity. Hand slots and battlefield slots are separate. |
| **2/1** | 2 power (damage dealt), 1 toughness (damage needed to kill it). |
| **R:1** | Ready to attack, provided it is not tapped. |
| **R:0 / summoning sickness** | Cannot attack yet. A new creature can still block. |
| **T:1 / tapped** | Already committed to attacking; cannot attack again or block until your next turn. |
| **A:1 / attacking** | Selected to attack. Before ending main, click again to deselect it. |
| **B:3** | This attacker is blocked by the opponent's creature in battlefield slot 3. **B:0** means unblocked. |

During blocking, choose an enemy attacker, then click **Block with N** to assign
your creature in slot N. One creature cannot block two attackers. Use **Unblock**
to remove an assignment, or choose another available creature to replace it.
Click **Resolve blocks** only when all your assignments are finished.

For example: your **Grizzly Bears (2/2)** blocks a **Goblin Piker (2/1)**.
Both deal 2 damage simultaneously, so **both die**. The attacker deals no damage
to your life total.

Commands also work without clickable chat:

| Command | Action |
| --- | --- |
| `/trigger mtg.menu set 1` | Open menu |
| `/trigger mtg.menu set 2` | Start solo as Red |
| `/trigger mtg.menu set 3` | Host PvP as Red |
| `/trigger mtg.menu set 4` | Join PvP as Green |
| `/trigger mtg.menu set 5` | Concede/cancel |
| `/trigger mtg.menu set 6` | View match |
| `/trigger mtg.play set 3` | Play hand slot 3 |
| `/trigger mtg.attack set 2` | Toggle creature slot 2 as attacker |
| `/trigger mtg.block set 23` | Block enemy slot 2 with your slot 3 |
| `/trigger mtg.block set 20` | Remove blocker from enemy slot 2 |
| `/trigger mtg.end set 1` | End main / resolve blocks |

Each trigger is re-enabled on the next server tick. Invalid actions are ignored:
check whose turn it is, mana, the land limit, and the five-creature board limit.

## Preset decks

Each deck has **24 cards**, an opening hand of seven, and **20 starting life**.
Cards are randomly drawn without replacement. Red skips the first turn's draw.

| Red | Copies | Green | Copies |
| --- | ---: | --- | ---: |
| Mountain | 10 | Forest | 10 |
| Goblin Piker — 2 mana, 2/1 | 6 | Grizzly Bears — 2 mana, 2/2 | 6 |
| Hill Giant — 4 mana, 3/3 | 4 | Spined Wurm — 5 mana, 5/4 | 4 |
| Shock — 1 mana, 2 damage to opponent | 4 | Nourish — 2 mana, gain 6 life | 4 |

These are introductory decks, **not format-legal constructed decks**.
The Green bot plays lands, prioritizes large creatures, attacks with all ready
creatures, and assigns available blockers in slot order. It does not inspect
the human's hidden hand.

## Prototype rules and limitations

- Maximum five creatures per side; no tokens or other permanent types.
- One combined main/attack-selection phase, followed by blocking and the next
  player's turn. No second main phase.
- No stack, priority, responses, instant-speed spells, mulligans, abilities,
  keywords, multiple blockers, planeswalkers, or deck builder.
- Shock can only target the opposing player, and both spells are main-phase only.
- Monocolor decks: colored requirements are represented by a single mana pool.
  Mana is automatic; no manual land tapping.
- At end of turn, excess cards over seven are automatically discarded from the
  **highest numbered occupied hand slots**. You do not choose discards yet.
- A disconnected player's match pauses on their actions; reconnect to continue.
  Tags and match state survive `/reload` and normal world saves.
- Boards and hands are text, not physical cards or an Arena-style graphical UI.
  Hidden hands are only displayed to their owner (operators can inspect storage).

## Administration / troubleshooting

- `/datapack list enabled` — check that the pack loaded.
- `/function mtga:menu` — open menu as a player (operator).
- `/function mtga:admin/reset` — clear a stuck lobby/match, including an offline
  participant. Stale offline player tags are cleaned automatically on reconnect.
- If `/reload` reports an error, check `logs/latest.log` and share the error.
- There is no scheduled bot task to leak after ending a match.
- Remove this folder to disable the pack. Its namespaced scores/storage remain
  inert; the pack never clears anyone's items.

## Development and testing

### Repository layout

| Path | Purpose |
| --- | --- |
| `pack.mcmeta` | Minecraft version compatibility and pack description |
| `data/minecraft/tags/function/` | Load and tick entry points |
| `data/mtga/function/` | Generated match logic, controls, bot, and chat interface |
| `design/cards.json` | Generated card reference |
| `tools/build.py` | Source generator for the datapack and card reference |
| `tools/generated.json` | Generated-output checksums for safe cleanup |
| `tools/validate.py` | Static checks |
| `tools/test_game.py` | Simulated game-logic tests |
| `tools/test_build.py` | Isolated build and cleanup tests |
| `tools/fixtures/duels.json` | Pre-refactor behavior baseline for 30 seeded games |

The pack uses **82 function files**, down from 304. Reusable macros handle hand
slots, attack toggles, blocker assignments, discards, combat pairs, and deaths.
The two seats retain separate entry points for readability. Dispatchers only
pass bounded slot numbers to macros; the player-facing controls are unchanged.
Generated pack files are committed so the repository works as a datapack without
Python.

`tools/build.py` generates the functions and metadata using Python 3.
Edit that generator rather than editing generated functions, then run:

```text
python tools/build.py
python tools/build.py --check
python tools/validate.py
python tools/test_game.py
python tools/test_build.py
```

The builder records its outputs in `tools/generated.json`. On a later build,
it removes obsolete function files only if their content still matches the
recorded checksum. Modified obsolete files cause an error rather than being
deleted; unrecognized files are left alone. `--check` reports stale outputs
without changing files.

Validation checks JSON, function references, inline macro arguments, and deck/card invariants;
it is **not** a Minecraft command parser. In-game testing is still required.
The logic tests run generated functions in a limited Python command model, with
ten test cases including every hand slot, every attacker/blocker pairing, and
30 complete simulated games with card-conservation checks. Game-state traces
are compared with the pre-macro version to detect behavior changes.
The six build tests verify repeatable generation, check-only mode, and safe cleanup.
These tests do not validate Minecraft syntax, selectors, permissions, or networking.
This pack has not yet been loaded in an actual Minecraft server by the authoring
assistant.

### In-game smoke test

1. Reload: no errors; menu opens for a non-operator.
2. Start solo: both life totals 20, private hand seven, no opening draw for Red.
3. Play one land: mana increases; a second land is rejected.
4. Cast a creature: mana decreases; it cannot attack immediately.
5. End: bot takes a turn; on your next turn your creature can attack.
6. Attack: tapped attackers cannot block on the opponent's next turn.
7. PvP: join from another account; hands remain private. Assign/reassign/remove
   blockers, resolve combat, and confirm both creatures die on a lethal trade.
8. Concede, restart, reload mid-match, and test administrator reset.

Unofficial fan project. Magic: The Gathering and its card names belong to
Wizards of the Coast. No official artwork, logos, or card images are included.
