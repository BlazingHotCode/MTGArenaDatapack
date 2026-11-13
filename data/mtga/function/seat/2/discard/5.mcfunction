scoreboard players set #h2_5 mtg 0
scoreboard players remove #handcount mtg 1
scoreboard players add #grave2 mtg 1
tellraw @a[tag=mtga.player] {"text":"Seat 2 discards hand slot 5 to the seven-card limit.","color":"gold"}
