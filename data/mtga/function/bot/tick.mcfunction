scoreboard players add #delay mtg 1
execute unless score #delay mtg matches 30.. run return 0
scoreboard players set #delay mtg 0
execute if score #turn mtg matches 2 if score #phase mtg matches 1 run return run function mtga:bot/main
execute if score #turn mtg matches 1 if score #phase mtg matches 2 run function mtga:bot/blocks
