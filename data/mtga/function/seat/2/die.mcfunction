$scoreboard players set #c2_$(b) mtg 0
$scoreboard players set #p2_$(b) mtg 0
$scoreboard players set #t2_$(b) mtg 0
$scoreboard players set #r2_$(b) mtg 0
$scoreboard players set #tap2_$(b) mtg 0
$scoreboard players set #a2_$(b) mtg 0
$scoreboard players set #b2_$(b) mtg 0
$scoreboard players set #used2_$(b) mtg 0
scoreboard players add #grave2 mtg 1
$tellraw @a[tag=mtga.player] {"text":"Seat 2's creature in slot $(b) dies.","color":"gold"}
