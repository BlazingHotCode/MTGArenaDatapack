scoreboard players set #landed1 mtg 0
scoreboard players operation #mana1 mtg = #lands1 mtg
scoreboard players set #tap1_1 mtg 0
scoreboard players set #tap1_2 mtg 0
scoreboard players set #tap1_3 mtg 0
scoreboard players set #tap1_4 mtg 0
scoreboard players set #tap1_5 mtg 0
execute if score #c1_1 mtg matches 1.. run scoreboard players set #r1_1 mtg 1
execute if score #c1_2 mtg matches 1.. run scoreboard players set #r1_2 mtg 1
execute if score #c1_3 mtg matches 1.. run scoreboard players set #r1_3 mtg 1
execute if score #c1_4 mtg matches 1.. run scoreboard players set #r1_4 mtg 1
execute if score #c1_5 mtg matches 1.. run scoreboard players set #r1_5 mtg 1
function mtga:seat/1/draw
