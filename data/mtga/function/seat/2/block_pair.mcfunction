$execute unless score #a1_$(a) mtg matches 1 run return 0
$scoreboard players set #blocker mtg $(b)
$execute unless score #blocker mtg matches 0 unless score #c2_$(b) mtg matches 1.. run return 0
$execute unless score #blocker mtg matches 0 unless score #tap2_$(b) mtg matches 0 run return 0
$execute unless score #blocker mtg matches 0 unless score #used2_$(b) mtg matches 0 run return 0
$execute if score #b1_$(a) mtg matches 1 run scoreboard players set #used2_1 mtg 0
$execute if score #b1_$(a) mtg matches 2 run scoreboard players set #used2_2 mtg 0
$execute if score #b1_$(a) mtg matches 3 run scoreboard players set #used2_3 mtg 0
$execute if score #b1_$(a) mtg matches 4 run scoreboard players set #used2_4 mtg 0
$execute if score #b1_$(a) mtg matches 5 run scoreboard players set #used2_5 mtg 0
$scoreboard players set #b1_$(a) mtg $(b)
$execute unless score #blocker mtg matches 0 run scoreboard players set #used2_$(b) mtg 1
