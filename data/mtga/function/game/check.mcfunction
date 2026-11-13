execute unless score #active mtg matches 1 run return 0
execute if score #life1 mtg matches ..0 run scoreboard players set #winner mtg 2
execute if score #life2 mtg matches ..0 run scoreboard players set #winner mtg 1
execute if score #winner mtg matches 1..2 run function mtga:game/finish
