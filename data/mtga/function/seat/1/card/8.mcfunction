execute unless score #mana1 mtg matches 2.. run return 0
scoreboard players add #grave1 mtg 1
scoreboard players add #life1 mtg 6
scoreboard players remove #mana1 mtg 2
scoreboard players set #played mtg 1
tellraw @a[tag=mtga.player] {"text":"Seat 1 plays Nourish.","color":"gold"}
