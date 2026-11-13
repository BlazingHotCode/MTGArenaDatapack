execute unless score #c1_3 mtg matches 1.. run return 0
execute unless score #r1_3 mtg matches 1 run return 0
execute unless score #tap1_3 mtg matches 0 run return 0
scoreboard players operation #old mtg = #a1_3 mtg
scoreboard players set #a1_3 mtg 1
execute if score #old mtg matches 1 run scoreboard players set #a1_3 mtg 0
