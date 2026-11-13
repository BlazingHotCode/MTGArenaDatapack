scoreboard players set #deadA mtg 0
scoreboard players set #deadB mtg 0
execute if score #p1_2 mtg >= #t2_3 mtg run scoreboard players set #deadB mtg 1
execute if score #p2_3 mtg >= #t1_2 mtg run scoreboard players set #deadA mtg 1
execute if score #deadA mtg matches 1 run function mtga:seat/1/die/2
execute if score #deadB mtg matches 1 run function mtga:seat/2/die/3
