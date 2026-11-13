execute unless score #active mtg matches 1 run return 0
execute store result score #count mtg run data get storage mtga:game deck2
execute if score #count mtg matches 0 run return run function mtga:seat/2/deck_loss
scoreboard players remove #count mtg 1
execute store result storage mtga:args max int 1 run scoreboard players get #count mtg
function mtga:seat/2/random with storage mtga:args
function mtga:seat/2/draw_pick with storage mtga:args
execute if score #h2_1 mtg matches 0 run return run scoreboard players operation #h2_1 mtg = #draw mtg
execute if score #h2_2 mtg matches 0 run return run scoreboard players operation #h2_2 mtg = #draw mtg
execute if score #h2_3 mtg matches 0 run return run scoreboard players operation #h2_3 mtg = #draw mtg
execute if score #h2_4 mtg matches 0 run return run scoreboard players operation #h2_4 mtg = #draw mtg
execute if score #h2_5 mtg matches 0 run return run scoreboard players operation #h2_5 mtg = #draw mtg
execute if score #h2_6 mtg matches 0 run return run scoreboard players operation #h2_6 mtg = #draw mtg
execute if score #h2_7 mtg matches 0 run return run scoreboard players operation #h2_7 mtg = #draw mtg
execute if score #h2_8 mtg matches 0 run return run scoreboard players operation #h2_8 mtg = #draw mtg
execute if score #h2_9 mtg matches 0 run return run scoreboard players operation #h2_9 mtg = #draw mtg
execute if score #h2_10 mtg matches 0 run return run scoreboard players operation #h2_10 mtg = #draw mtg
execute if score #h2_11 mtg matches 0 run return run scoreboard players operation #h2_11 mtg = #draw mtg
execute if score #h2_12 mtg matches 0 run return run scoreboard players operation #h2_12 mtg = #draw mtg
execute if score #h2_13 mtg matches 0 run return run scoreboard players operation #h2_13 mtg = #draw mtg
execute if score #h2_14 mtg matches 0 run return run scoreboard players operation #h2_14 mtg = #draw mtg
execute if score #h2_15 mtg matches 0 run return run scoreboard players operation #h2_15 mtg = #draw mtg
execute if score #h2_16 mtg matches 0 run return run scoreboard players operation #h2_16 mtg = #draw mtg
execute if score #h2_17 mtg matches 0 run return run scoreboard players operation #h2_17 mtg = #draw mtg
execute if score #h2_18 mtg matches 0 run return run scoreboard players operation #h2_18 mtg = #draw mtg
execute if score #h2_19 mtg matches 0 run return run scoreboard players operation #h2_19 mtg = #draw mtg
execute if score #h2_20 mtg matches 0 run return run scoreboard players operation #h2_20 mtg = #draw mtg
execute if score #h2_21 mtg matches 0 run return run scoreboard players operation #h2_21 mtg = #draw mtg
execute if score #h2_22 mtg matches 0 run return run scoreboard players operation #h2_22 mtg = #draw mtg
execute if score #h2_23 mtg matches 0 run return run scoreboard players operation #h2_23 mtg = #draw mtg
execute if score #h2_24 mtg matches 0 run return run scoreboard players operation #h2_24 mtg = #draw mtg
