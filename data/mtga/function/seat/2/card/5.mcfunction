execute unless score #mana2 mtg matches 4.. run return 0
scoreboard players set #slot mtg 0
execute if score #slot mtg matches 0 if score #c2_1 mtg matches 0 run scoreboard players set #slot mtg 1
execute if score #slot mtg matches 0 if score #c2_2 mtg matches 0 run scoreboard players set #slot mtg 2
execute if score #slot mtg matches 0 if score #c2_3 mtg matches 0 run scoreboard players set #slot mtg 3
execute if score #slot mtg matches 0 if score #c2_4 mtg matches 0 run scoreboard players set #slot mtg 4
execute if score #slot mtg matches 0 if score #c2_5 mtg matches 0 run scoreboard players set #slot mtg 5
execute if score #slot mtg matches 0 run return 0
execute if score #slot mtg matches 1 run scoreboard players set #c2_1 mtg 5
execute if score #slot mtg matches 1 run scoreboard players set #p2_1 mtg 3
execute if score #slot mtg matches 1 run scoreboard players set #t2_1 mtg 3
execute if score #slot mtg matches 1 run scoreboard players set #r2_1 mtg 0
execute if score #slot mtg matches 1 run scoreboard players set #tap2_1 mtg 0
execute if score #slot mtg matches 1 run scoreboard players set #a2_1 mtg 0
execute if score #slot mtg matches 1 run scoreboard players set #b2_1 mtg 0
execute if score #slot mtg matches 1 run scoreboard players set #used2_1 mtg 0
execute if score #slot mtg matches 2 run scoreboard players set #c2_2 mtg 5
execute if score #slot mtg matches 2 run scoreboard players set #p2_2 mtg 3
execute if score #slot mtg matches 2 run scoreboard players set #t2_2 mtg 3
execute if score #slot mtg matches 2 run scoreboard players set #r2_2 mtg 0
execute if score #slot mtg matches 2 run scoreboard players set #tap2_2 mtg 0
execute if score #slot mtg matches 2 run scoreboard players set #a2_2 mtg 0
execute if score #slot mtg matches 2 run scoreboard players set #b2_2 mtg 0
execute if score #slot mtg matches 2 run scoreboard players set #used2_2 mtg 0
execute if score #slot mtg matches 3 run scoreboard players set #c2_3 mtg 5
execute if score #slot mtg matches 3 run scoreboard players set #p2_3 mtg 3
execute if score #slot mtg matches 3 run scoreboard players set #t2_3 mtg 3
execute if score #slot mtg matches 3 run scoreboard players set #r2_3 mtg 0
execute if score #slot mtg matches 3 run scoreboard players set #tap2_3 mtg 0
execute if score #slot mtg matches 3 run scoreboard players set #a2_3 mtg 0
execute if score #slot mtg matches 3 run scoreboard players set #b2_3 mtg 0
execute if score #slot mtg matches 3 run scoreboard players set #used2_3 mtg 0
execute if score #slot mtg matches 4 run scoreboard players set #c2_4 mtg 5
execute if score #slot mtg matches 4 run scoreboard players set #p2_4 mtg 3
execute if score #slot mtg matches 4 run scoreboard players set #t2_4 mtg 3
execute if score #slot mtg matches 4 run scoreboard players set #r2_4 mtg 0
execute if score #slot mtg matches 4 run scoreboard players set #tap2_4 mtg 0
execute if score #slot mtg matches 4 run scoreboard players set #a2_4 mtg 0
execute if score #slot mtg matches 4 run scoreboard players set #b2_4 mtg 0
execute if score #slot mtg matches 4 run scoreboard players set #used2_4 mtg 0
execute if score #slot mtg matches 5 run scoreboard players set #c2_5 mtg 5
execute if score #slot mtg matches 5 run scoreboard players set #p2_5 mtg 3
execute if score #slot mtg matches 5 run scoreboard players set #t2_5 mtg 3
execute if score #slot mtg matches 5 run scoreboard players set #r2_5 mtg 0
execute if score #slot mtg matches 5 run scoreboard players set #tap2_5 mtg 0
execute if score #slot mtg matches 5 run scoreboard players set #a2_5 mtg 0
execute if score #slot mtg matches 5 run scoreboard players set #b2_5 mtg 0
execute if score #slot mtg matches 5 run scoreboard players set #used2_5 mtg 0
scoreboard players remove #mana2 mtg 4
scoreboard players set #played mtg 1
tellraw @a[tag=mtga.player] {"text":"Seat 2 plays Hill Giant.","color":"gold"}
