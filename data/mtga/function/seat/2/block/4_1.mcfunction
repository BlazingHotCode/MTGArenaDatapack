execute unless score #a1_4 mtg matches 1 run return 0
execute unless score #c2_1 mtg matches 1.. run return 0
execute unless score #tap2_1 mtg matches 0 run return 0
execute unless score #used2_1 mtg matches 0 run return 0
execute if score #b1_4 mtg matches 1 run scoreboard players set #used2_1 mtg 0
execute if score #b1_4 mtg matches 2 run scoreboard players set #used2_2 mtg 0
execute if score #b1_4 mtg matches 3 run scoreboard players set #used2_3 mtg 0
execute if score #b1_4 mtg matches 4 run scoreboard players set #used2_4 mtg 0
execute if score #b1_4 mtg matches 5 run scoreboard players set #used2_5 mtg 0
scoreboard players set #b1_4 mtg 1
scoreboard players set #used2_1 mtg 1
