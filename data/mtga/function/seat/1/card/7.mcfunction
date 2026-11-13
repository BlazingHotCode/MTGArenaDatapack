execute unless score #mana1 mtg matches 1.. run return 0
scoreboard players add #grave1 mtg 1
scoreboard players remove #life2 mtg 2
scoreboard players remove #mana1 mtg 1
scoreboard players set #played mtg 1
tellraw @a[tag=mtga.player] {"text":"Seat 1 plays Shock.","color":"gold"}
