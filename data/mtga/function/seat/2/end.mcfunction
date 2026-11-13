execute if score #phase mtg matches 1 if score #turn mtg matches 2 run return run function mtga:seat/2/commit
execute if score #phase mtg matches 2 unless score #turn mtg matches 2 run function mtga:game/combat
