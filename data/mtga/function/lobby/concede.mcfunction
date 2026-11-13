execute unless entity @s[tag=mtga.player] run return 0
execute if score #active mtg matches 2 run return run function mtga:game/stop
execute unless score #active mtg matches 1 run return 0
execute if entity @s[tag=mtga.p1] run scoreboard players set #winner mtg 2
execute if entity @s[tag=mtga.p2] run scoreboard players set #winner mtg 1
function mtga:game/finish
