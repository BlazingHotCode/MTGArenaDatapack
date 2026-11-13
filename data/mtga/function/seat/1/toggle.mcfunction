$execute unless score #c1_$(b) mtg matches 1.. run return 0
$execute unless score #r1_$(b) mtg matches 1 run return 0
$execute unless score #tap1_$(b) mtg matches 0 run return 0
$scoreboard players operation #old mtg = #a1_$(b) mtg
$scoreboard players set #a1_$(b) mtg 1
$execute if score #old mtg matches 1 run scoreboard players set #a1_$(b) mtg 0
