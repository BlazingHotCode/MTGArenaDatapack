scoreboard players set #h1_2 mtg 0
scoreboard players remove #handcount mtg 1
scoreboard players add #grave1 mtg 1
tellraw @a[tag=mtga.player] {"text":"Seat 1 discards hand slot 2 to the seven-card limit.","color":"gold"}
