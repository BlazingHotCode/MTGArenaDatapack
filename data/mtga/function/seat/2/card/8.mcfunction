execute unless score #mana2 mtg matches 2.. run return 0
scoreboard players add #grave2 mtg 1
scoreboard players add #life2 mtg 6
scoreboard players remove #mana2 mtg 2
scoreboard players set #played mtg 1
tellraw @a[tag=mtga.player] {"text":"Seat 2 plays Nourish.","color":"gold"}
