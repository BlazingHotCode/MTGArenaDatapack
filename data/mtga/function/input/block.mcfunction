scoreboard players operation #request mtg = @s mtg.block
scoreboard players set @s mtg.block 0
execute unless score #active mtg matches 1 run return 0
execute if entity @s[tag=mtga.p1] run function mtga:seat/1/block
execute if entity @s[tag=mtga.p2] run function mtga:seat/2/block
function mtga:game/check
function mtga:game/refresh
