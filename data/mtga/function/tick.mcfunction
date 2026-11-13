execute as @a[tag=mtga.player] unless score @s mtg.session = #session mtg run function mtga:lobby/clear_tags
execute if score #active mtg matches 0 as @a[tag=mtga.player] run function mtga:lobby/clear_tags
execute as @a[scores={mtg.menu=1..}] run function mtga:input/menu
execute as @a[scores={mtg.play=1..}] run function mtga:input/play
execute as @a[scores={mtg.attack=1..}] run function mtga:input/attack
execute as @a[scores={mtg.block=1..}] run function mtga:input/block
execute as @a[scores={mtg.end=1..}] run function mtga:input/end
execute as @a[scores={mtg.menu=..-1}] run scoreboard players set @s mtg.menu 0
execute as @a[scores={mtg.play=..-1}] run scoreboard players set @s mtg.play 0
execute as @a[scores={mtg.attack=..-1}] run scoreboard players set @s mtg.attack 0
execute as @a[scores={mtg.block=..-1}] run scoreboard players set @s mtg.block 0
execute as @a[scores={mtg.end=..-1}] run scoreboard players set @s mtg.end 0
scoreboard players enable @a mtg.menu
scoreboard players enable @a mtg.play
scoreboard players enable @a mtg.attack
scoreboard players enable @a mtg.block
scoreboard players enable @a mtg.end
execute if score #active mtg matches 1 if score #bot mtg matches 1 run function mtga:bot/tick
