scoreboard players set #deadA mtg 0
scoreboard players set #deadB mtg 0
execute if score #p1_1 mtg >= #t2_5 mtg run scoreboard players set #deadB mtg 1
execute if score #p2_5 mtg >= #t1_1 mtg run scoreboard players set #deadA mtg 1
execute if score #deadA mtg matches 1 run function mtga:seat/1/die/1
execute if score #deadB mtg matches 1 run function mtga:seat/2/die/5
