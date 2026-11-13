execute unless score #active mtg matches 0 run return run tellraw @s {"text":"A match or lobby already exists. Finish it or have its host cancel.","color":"gray"}
tag @a remove mtga.p1
tag @a remove mtga.p2
tag @a remove mtga.player
scoreboard players add #session mtg 1
scoreboard players operation @s mtg.session = #session mtg
tag @s add mtga.p1
tag @s add mtga.player
scoreboard players set #bot mtg 1
function mtga:game/start
