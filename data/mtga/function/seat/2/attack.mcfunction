execute unless score #turn mtg matches 2 run return 0
execute unless score #phase mtg matches 1 run return 0
execute if score #request mtg matches 1 run function mtga:seat/2/toggle {"b":1}
execute if score #request mtg matches 2 run function mtga:seat/2/toggle {"b":2}
execute if score #request mtg matches 3 run function mtga:seat/2/toggle {"b":3}
execute if score #request mtg matches 4 run function mtga:seat/2/toggle {"b":4}
execute if score #request mtg matches 5 run function mtga:seat/2/toggle {"b":5}
