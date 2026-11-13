execute unless score #active mtg matches 0 run return run tellraw @s {"text":"A match or lobby already exists. Finish it or have its host cancel.","color":"gray"}
tag @a remove mtga.p1
tag @a remove mtga.p2
tag @a remove mtga.player
scoreboard players add #session mtg 1
scoreboard players operation @s mtg.session = #session mtg
tag @s add mtga.p1
tag @s add mtga.player
scoreboard players set #bot mtg 0
scoreboard players set #active mtg 2
tellraw @a [{"text":"[MTG] A PvP lobby is open. ","color":"gold"},{"text":"[Join Green deck]","color":"aqua","click_event":{"action":"run_command","command":"/trigger mtg.menu set 4"}}]
