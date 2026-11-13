$execute unless score #a2_$(a) mtg matches 1 run return 0
$scoreboard players set #blocker mtg $(b)
$execute unless score #blocker mtg matches 0 unless score #c1_$(b) mtg matches 1.. run return 0
$execute unless score #blocker mtg matches 0 unless score #tap1_$(b) mtg matches 0 run return 0
$execute unless score #blocker mtg matches 0 unless score #used1_$(b) mtg matches 0 run return 0
$execute if score #b2_$(a) mtg matches 1 run scoreboard players set #used1_1 mtg 0
$execute if score #b2_$(a) mtg matches 2 run scoreboard players set #used1_2 mtg 0
$execute if score #b2_$(a) mtg matches 3 run scoreboard players set #used1_3 mtg 0
$execute if score #b2_$(a) mtg matches 4 run scoreboard players set #used1_4 mtg 0
$execute if score #b2_$(a) mtg matches 5 run scoreboard players set #used1_5 mtg 0
$scoreboard players set #b2_$(a) mtg $(b)
$execute unless score #blocker mtg matches 0 run scoreboard players set #used1_$(b) mtg 1
