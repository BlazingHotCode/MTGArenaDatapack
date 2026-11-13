$execute unless score #c2_$(b) mtg matches 1.. run return 0
$execute unless score #r2_$(b) mtg matches 1 run return 0
$execute unless score #tap2_$(b) mtg matches 0 run return 0
$scoreboard players operation #old mtg = #a2_$(b) mtg
$scoreboard players set #a2_$(b) mtg 1
$execute if score #old mtg matches 1 run scoreboard players set #a2_$(b) mtg 0
