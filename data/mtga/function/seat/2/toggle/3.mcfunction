execute unless score #c2_3 mtg matches 1.. run return 0
execute unless score #r2_3 mtg matches 1 run return 0
execute unless score #tap2_3 mtg matches 0 run return 0
scoreboard players operation #old mtg = #a2_3 mtg
scoreboard players set #a2_3 mtg 1
execute if score #old mtg matches 1 run scoreboard players set #a2_3 mtg 0
