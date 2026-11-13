execute unless score #a2_4 mtg matches 1 run return 0
execute if score #b2_4 mtg matches 1 run scoreboard players set #used1_1 mtg 0
execute if score #b2_4 mtg matches 2 run scoreboard players set #used1_2 mtg 0
execute if score #b2_4 mtg matches 3 run scoreboard players set #used1_3 mtg 0
execute if score #b2_4 mtg matches 4 run scoreboard players set #used1_4 mtg 0
execute if score #b2_4 mtg matches 5 run scoreboard players set #used1_5 mtg 0
scoreboard players set #b2_4 mtg 0
