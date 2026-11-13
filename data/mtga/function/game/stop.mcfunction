scoreboard players set #active mtg 0
tellraw @a[tag=mtga.player] {"text":"Match / lobby closed. Open the menu to play again.","color":"gold"}
tag @a remove mtga.player
tag @a remove mtga.p1
tag @a remove mtga.p2
