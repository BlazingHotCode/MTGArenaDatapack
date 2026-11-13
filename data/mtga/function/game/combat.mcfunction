execute if score #turn mtg matches 1 if score #a1_1 mtg matches 1 run function mtga:seat/1/combat {"a":1}
execute if score #turn mtg matches 1 if score #a1_2 mtg matches 1 run function mtga:seat/1/combat {"a":2}
execute if score #turn mtg matches 1 if score #a1_3 mtg matches 1 run function mtga:seat/1/combat {"a":3}
execute if score #turn mtg matches 1 if score #a1_4 mtg matches 1 run function mtga:seat/1/combat {"a":4}
execute if score #turn mtg matches 1 if score #a1_5 mtg matches 1 run function mtga:seat/1/combat {"a":5}
execute if score #turn mtg matches 2 if score #a2_1 mtg matches 1 run function mtga:seat/2/combat {"a":1}
execute if score #turn mtg matches 2 if score #a2_2 mtg matches 1 run function mtga:seat/2/combat {"a":2}
execute if score #turn mtg matches 2 if score #a2_3 mtg matches 1 run function mtga:seat/2/combat {"a":3}
execute if score #turn mtg matches 2 if score #a2_4 mtg matches 1 run function mtga:seat/2/combat {"a":4}
execute if score #turn mtg matches 2 if score #a2_5 mtg matches 1 run function mtga:seat/2/combat {"a":5}
function mtga:game/check
execute if score #active mtg matches 1 run function mtga:game/next
