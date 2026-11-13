execute unless score #active mtg matches 1 run return 0
execute store result score #count mtg run data get storage mtga:game deck1
execute if score #count mtg matches 0 run return run function mtga:seat/1/deck_loss
scoreboard players remove #count mtg 1
execute store result storage mtga:args max int 1 run scoreboard players get #count mtg
function mtga:seat/1/random with storage mtga:args
function mtga:seat/1/draw_pick with storage mtga:args
execute if score #h1_1 mtg matches 0 run return run scoreboard players operation #h1_1 mtg = #draw mtg
execute if score #h1_2 mtg matches 0 run return run scoreboard players operation #h1_2 mtg = #draw mtg
execute if score #h1_3 mtg matches 0 run return run scoreboard players operation #h1_3 mtg = #draw mtg
execute if score #h1_4 mtg matches 0 run return run scoreboard players operation #h1_4 mtg = #draw mtg
execute if score #h1_5 mtg matches 0 run return run scoreboard players operation #h1_5 mtg = #draw mtg
execute if score #h1_6 mtg matches 0 run return run scoreboard players operation #h1_6 mtg = #draw mtg
execute if score #h1_7 mtg matches 0 run return run scoreboard players operation #h1_7 mtg = #draw mtg
execute if score #h1_8 mtg matches 0 run return run scoreboard players operation #h1_8 mtg = #draw mtg
execute if score #h1_9 mtg matches 0 run return run scoreboard players operation #h1_9 mtg = #draw mtg
execute if score #h1_10 mtg matches 0 run return run scoreboard players operation #h1_10 mtg = #draw mtg
execute if score #h1_11 mtg matches 0 run return run scoreboard players operation #h1_11 mtg = #draw mtg
execute if score #h1_12 mtg matches 0 run return run scoreboard players operation #h1_12 mtg = #draw mtg
execute if score #h1_13 mtg matches 0 run return run scoreboard players operation #h1_13 mtg = #draw mtg
execute if score #h1_14 mtg matches 0 run return run scoreboard players operation #h1_14 mtg = #draw mtg
execute if score #h1_15 mtg matches 0 run return run scoreboard players operation #h1_15 mtg = #draw mtg
execute if score #h1_16 mtg matches 0 run return run scoreboard players operation #h1_16 mtg = #draw mtg
execute if score #h1_17 mtg matches 0 run return run scoreboard players operation #h1_17 mtg = #draw mtg
execute if score #h1_18 mtg matches 0 run return run scoreboard players operation #h1_18 mtg = #draw mtg
execute if score #h1_19 mtg matches 0 run return run scoreboard players operation #h1_19 mtg = #draw mtg
execute if score #h1_20 mtg matches 0 run return run scoreboard players operation #h1_20 mtg = #draw mtg
execute if score #h1_21 mtg matches 0 run return run scoreboard players operation #h1_21 mtg = #draw mtg
execute if score #h1_22 mtg matches 0 run return run scoreboard players operation #h1_22 mtg = #draw mtg
execute if score #h1_23 mtg matches 0 run return run scoreboard players operation #h1_23 mtg = #draw mtg
execute if score #h1_24 mtg matches 0 run return run scoreboard players operation #h1_24 mtg = #draw mtg
