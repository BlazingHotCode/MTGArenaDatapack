scoreboard players set #landed2 mtg 0
scoreboard players operation #mana2 mtg = #lands2 mtg
scoreboard players set #tap2_1 mtg 0
scoreboard players set #tap2_2 mtg 0
scoreboard players set #tap2_3 mtg 0
scoreboard players set #tap2_4 mtg 0
scoreboard players set #tap2_5 mtg 0
execute if score #c2_1 mtg matches 1.. run scoreboard players set #r2_1 mtg 1
execute if score #c2_2 mtg matches 1.. run scoreboard players set #r2_2 mtg 1
execute if score #c2_3 mtg matches 1.. run scoreboard players set #r2_3 mtg 1
execute if score #c2_4 mtg matches 1.. run scoreboard players set #r2_4 mtg 1
execute if score #c2_5 mtg matches 1.. run scoreboard players set #r2_5 mtg 1
function mtga:seat/2/draw
