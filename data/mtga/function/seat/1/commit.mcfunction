scoreboard players set #attackers mtg 0
execute if score #a1_1 mtg matches 1 run scoreboard players add #attackers mtg 1
execute if score #a1_2 mtg matches 1 run scoreboard players add #attackers mtg 1
execute if score #a1_3 mtg matches 1 run scoreboard players add #attackers mtg 1
execute if score #a1_4 mtg matches 1 run scoreboard players add #attackers mtg 1
execute if score #a1_5 mtg matches 1 run scoreboard players add #attackers mtg 1
execute if score #a1_1 mtg matches 1 run scoreboard players set #tap1_1 mtg 1
execute if score #a1_2 mtg matches 1 run scoreboard players set #tap1_2 mtg 1
execute if score #a1_3 mtg matches 1 run scoreboard players set #tap1_3 mtg 1
execute if score #a1_4 mtg matches 1 run scoreboard players set #tap1_4 mtg 1
execute if score #a1_5 mtg matches 1 run scoreboard players set #tap1_5 mtg 1
execute if score #attackers mtg matches 0 run return run function mtga:game/next
scoreboard players set #phase mtg 2
scoreboard players set #delay mtg 0
tellraw @a[tag=mtga.player] {"text":"Seat 1 attacks. Seat 2: assign blockers, then click Resolve blocks.","color":"gold"}
