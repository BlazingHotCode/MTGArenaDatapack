scoreboard players operation #request mtg = @s mtg.play
scoreboard players set @s mtg.play 0
execute unless score #active mtg matches 1 run return 0
execute if entity @s[tag=mtga.p1] run function mtga:seat/1/play
execute if entity @s[tag=mtga.p2] run function mtga:seat/2/play
function mtga:game/check
function mtga:game/refresh
