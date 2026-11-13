scoreboard players set #deadA mtg 0
scoreboard players set #deadB mtg 0
$execute if score #p1_$(a) mtg >= #t2_$(b) mtg run scoreboard players set #deadB mtg 1
$execute if score #p2_$(b) mtg >= #t1_$(a) mtg run scoreboard players set #deadA mtg 1
$execute if score #deadA mtg matches 1 run function mtga:seat/1/die {"b":"$(a)"}
$execute if score #deadB mtg matches 1 run function mtga:seat/2/die {"b":"$(b)"}
