execute if score #landed1 mtg matches 1 run return 0
scoreboard players add #lands1 mtg 1
scoreboard players add #mana1 mtg 1
scoreboard players set #landed1 mtg 1
scoreboard players set #played mtg 1
tellraw @a[tag=mtga.player] {"text":"Seat 1 plays Forest.","color":"gold"}
