$scoreboard players operation #card mtg = #h2_$(h) mtg
scoreboard players set #played mtg 0
execute if score #card mtg matches 1 run function mtga:seat/2/card/1
execute if score #card mtg matches 2 run function mtga:seat/2/card/2
execute if score #card mtg matches 3 run function mtga:seat/2/card/3
execute if score #card mtg matches 4 run function mtga:seat/2/card/4
execute if score #card mtg matches 5 run function mtga:seat/2/card/5
execute if score #card mtg matches 6 run function mtga:seat/2/card/6
execute if score #card mtg matches 7 run function mtga:seat/2/card/7
execute if score #card mtg matches 8 run function mtga:seat/2/card/8
$execute if score #played mtg matches 1 run scoreboard players set #h2_$(h) mtg 0
