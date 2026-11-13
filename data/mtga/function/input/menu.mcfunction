scoreboard players operation #request mtg = @s mtg.menu
scoreboard players set @s mtg.menu 0
execute if score #request mtg matches 1 run function mtga:menu
execute if score #request mtg matches 2 run function mtga:lobby/solo
execute if score #request mtg matches 3 run function mtga:lobby/host
execute if score #request mtg matches 4 run function mtga:lobby/join
execute if score #request mtg matches 5 run function mtga:lobby/concede
execute if score #request mtg matches 6 run function mtga:view
