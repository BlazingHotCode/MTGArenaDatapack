scoreboard players operation #request mtg = @s mtg.attack
scoreboard players set @s mtg.attack 0
execute unless score #active mtg matches 1 run return 0
execute if entity @s[tag=mtga.p1] run function mtga:seat/1/attack
execute if entity @s[tag=mtga.p2] run function mtga:seat/2/attack
function mtga:game/check
function mtga:game/refresh
