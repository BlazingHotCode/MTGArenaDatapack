scoreboard players operation #request mtg = @s mtg.end
scoreboard players set @s mtg.end 0
execute unless score #active mtg matches 1 run return 0
execute if entity @s[tag=mtga.p1] run function mtga:seat/1/end
execute if entity @s[tag=mtga.p2] run function mtga:seat/2/end
function mtga:game/check
function mtga:game/refresh
