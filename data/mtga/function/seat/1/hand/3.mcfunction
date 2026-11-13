scoreboard players operation #card mtg = #h1_3 mtg
scoreboard players set #played mtg 0
execute if score #card mtg matches 1 run function mtga:seat/1/card/1
execute if score #card mtg matches 2 run function mtga:seat/1/card/2
execute if score #card mtg matches 3 run function mtga:seat/1/card/3
execute if score #card mtg matches 4 run function mtga:seat/1/card/4
execute if score #card mtg matches 5 run function mtga:seat/1/card/5
execute if score #card mtg matches 6 run function mtga:seat/1/card/6
execute if score #card mtg matches 7 run function mtga:seat/1/card/7
execute if score #card mtg matches 8 run function mtga:seat/1/card/8
execute if score #played mtg matches 1 run scoreboard players set #h1_3 mtg 0
