execute if score #turn mtg matches 1 run function mtga:seat/1/cleanup
execute if score #turn mtg matches 2 run function mtga:seat/2/cleanup
scoreboard players operation #previous mtg = #turn mtg
scoreboard players set #turn mtg 1
execute if score #previous mtg matches 1 run scoreboard players set #turn mtg 2
scoreboard players add #round mtg 1
scoreboard players set #phase mtg 1
scoreboard players set #delay mtg 0
scoreboard players set #a1_1 mtg 0
scoreboard players set #b1_1 mtg 0
scoreboard players set #used1_1 mtg 0
scoreboard players set #a1_2 mtg 0
scoreboard players set #b1_2 mtg 0
scoreboard players set #used1_2 mtg 0
scoreboard players set #a1_3 mtg 0
scoreboard players set #b1_3 mtg 0
scoreboard players set #used1_3 mtg 0
scoreboard players set #a1_4 mtg 0
scoreboard players set #b1_4 mtg 0
scoreboard players set #used1_4 mtg 0
scoreboard players set #a1_5 mtg 0
scoreboard players set #b1_5 mtg 0
scoreboard players set #used1_5 mtg 0
scoreboard players set #a2_1 mtg 0
scoreboard players set #b2_1 mtg 0
scoreboard players set #used2_1 mtg 0
scoreboard players set #a2_2 mtg 0
scoreboard players set #b2_2 mtg 0
scoreboard players set #used2_2 mtg 0
scoreboard players set #a2_3 mtg 0
scoreboard players set #b2_3 mtg 0
scoreboard players set #used2_3 mtg 0
scoreboard players set #a2_4 mtg 0
scoreboard players set #b2_4 mtg 0
scoreboard players set #used2_4 mtg 0
scoreboard players set #a2_5 mtg 0
scoreboard players set #b2_5 mtg 0
scoreboard players set #used2_5 mtg 0
execute if score #turn mtg matches 1 run function mtga:seat/1/begin
execute if score #turn mtg matches 2 run function mtga:seat/2/begin
