execute unless score #mana1 mtg matches 2.. run return 0
scoreboard players set #slot mtg 0
execute if score #slot mtg matches 0 if score #c1_1 mtg matches 0 run scoreboard players set #slot mtg 1
execute if score #slot mtg matches 0 if score #c1_2 mtg matches 0 run scoreboard players set #slot mtg 2
execute if score #slot mtg matches 0 if score #c1_3 mtg matches 0 run scoreboard players set #slot mtg 3
execute if score #slot mtg matches 0 if score #c1_4 mtg matches 0 run scoreboard players set #slot mtg 4
execute if score #slot mtg matches 0 if score #c1_5 mtg matches 0 run scoreboard players set #slot mtg 5
execute if score #slot mtg matches 0 run return 0
execute if score #slot mtg matches 1 run scoreboard players set #c1_1 mtg 3
execute if score #slot mtg matches 1 run scoreboard players set #p1_1 mtg 2
execute if score #slot mtg matches 1 run scoreboard players set #t1_1 mtg 1
execute if score #slot mtg matches 1 run scoreboard players set #r1_1 mtg 0
execute if score #slot mtg matches 1 run scoreboard players set #tap1_1 mtg 0
execute if score #slot mtg matches 1 run scoreboard players set #a1_1 mtg 0
execute if score #slot mtg matches 1 run scoreboard players set #b1_1 mtg 0
execute if score #slot mtg matches 1 run scoreboard players set #used1_1 mtg 0
execute if score #slot mtg matches 2 run scoreboard players set #c1_2 mtg 3
execute if score #slot mtg matches 2 run scoreboard players set #p1_2 mtg 2
execute if score #slot mtg matches 2 run scoreboard players set #t1_2 mtg 1
execute if score #slot mtg matches 2 run scoreboard players set #r1_2 mtg 0
execute if score #slot mtg matches 2 run scoreboard players set #tap1_2 mtg 0
execute if score #slot mtg matches 2 run scoreboard players set #a1_2 mtg 0
execute if score #slot mtg matches 2 run scoreboard players set #b1_2 mtg 0
execute if score #slot mtg matches 2 run scoreboard players set #used1_2 mtg 0
execute if score #slot mtg matches 3 run scoreboard players set #c1_3 mtg 3
execute if score #slot mtg matches 3 run scoreboard players set #p1_3 mtg 2
execute if score #slot mtg matches 3 run scoreboard players set #t1_3 mtg 1
execute if score #slot mtg matches 3 run scoreboard players set #r1_3 mtg 0
execute if score #slot mtg matches 3 run scoreboard players set #tap1_3 mtg 0
execute if score #slot mtg matches 3 run scoreboard players set #a1_3 mtg 0
execute if score #slot mtg matches 3 run scoreboard players set #b1_3 mtg 0
execute if score #slot mtg matches 3 run scoreboard players set #used1_3 mtg 0
execute if score #slot mtg matches 4 run scoreboard players set #c1_4 mtg 3
execute if score #slot mtg matches 4 run scoreboard players set #p1_4 mtg 2
execute if score #slot mtg matches 4 run scoreboard players set #t1_4 mtg 1
execute if score #slot mtg matches 4 run scoreboard players set #r1_4 mtg 0
execute if score #slot mtg matches 4 run scoreboard players set #tap1_4 mtg 0
execute if score #slot mtg matches 4 run scoreboard players set #a1_4 mtg 0
execute if score #slot mtg matches 4 run scoreboard players set #b1_4 mtg 0
execute if score #slot mtg matches 4 run scoreboard players set #used1_4 mtg 0
execute if score #slot mtg matches 5 run scoreboard players set #c1_5 mtg 3
execute if score #slot mtg matches 5 run scoreboard players set #p1_5 mtg 2
execute if score #slot mtg matches 5 run scoreboard players set #t1_5 mtg 1
execute if score #slot mtg matches 5 run scoreboard players set #r1_5 mtg 0
execute if score #slot mtg matches 5 run scoreboard players set #tap1_5 mtg 0
execute if score #slot mtg matches 5 run scoreboard players set #a1_5 mtg 0
execute if score #slot mtg matches 5 run scoreboard players set #b1_5 mtg 0
execute if score #slot mtg matches 5 run scoreboard players set #used1_5 mtg 0
scoreboard players remove #mana1 mtg 2
scoreboard players set #played mtg 1
tellraw @a[tag=mtga.player] {"text":"Seat 1 plays Goblin Piker.","color":"gold"}
