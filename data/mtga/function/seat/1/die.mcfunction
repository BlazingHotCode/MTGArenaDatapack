$scoreboard players set #c1_$(b) mtg 0
$scoreboard players set #p1_$(b) mtg 0
$scoreboard players set #t1_$(b) mtg 0
$scoreboard players set #r1_$(b) mtg 0
$scoreboard players set #tap1_$(b) mtg 0
$scoreboard players set #a1_$(b) mtg 0
$scoreboard players set #b1_$(b) mtg 0
$scoreboard players set #used1_$(b) mtg 0
scoreboard players add #grave1 mtg 1
$tellraw @a[tag=mtga.player] {"text":"Seat 1's creature in slot $(b) dies.","color":"gold"}
