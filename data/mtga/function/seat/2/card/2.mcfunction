execute if score #landed2 mtg matches 1 run return 0
scoreboard players add #lands2 mtg 1
scoreboard players add #mana2 mtg 1
scoreboard players set #landed2 mtg 1
scoreboard players set #played mtg 1
tellraw @a[tag=mtga.player] {"text":"Seat 2 plays Forest.","color":"gold"}
