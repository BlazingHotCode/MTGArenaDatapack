$execute if score #b2_$(a) mtg matches 0 run return run scoreboard players operation #life1 mtg -= #p2_$(a) mtg
$execute if score #b2_$(a) mtg matches 1 run function mtga:seat/2/fight {"a":"$(a)","b":1}
$execute if score #b2_$(a) mtg matches 2 run function mtga:seat/2/fight {"a":"$(a)","b":2}
$execute if score #b2_$(a) mtg matches 3 run function mtga:seat/2/fight {"a":"$(a)","b":3}
$execute if score #b2_$(a) mtg matches 4 run function mtga:seat/2/fight {"a":"$(a)","b":4}
$execute if score #b2_$(a) mtg matches 5 run function mtga:seat/2/fight {"a":"$(a)","b":5}
