execute unless score #active mtg matches 2 run return run tellraw @s {"text":"No open PvP lobby.","color":"gray"}
execute if entity @s[tag=mtga.p1] run return run tellraw @s {"text":"Wait for another player to join.","color":"gray"}
scoreboard players operation @s mtg.session = #session mtg
tag @s add mtga.p2
tag @s add mtga.player
function mtga:game/start
