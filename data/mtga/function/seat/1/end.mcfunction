execute if score #phase mtg matches 1 if score #turn mtg matches 1 run return run function mtga:seat/1/commit
execute if score #phase mtg matches 2 unless score #turn mtg matches 1 run function mtga:game/combat
