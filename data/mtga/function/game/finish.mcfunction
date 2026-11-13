execute if score #winner mtg matches 1 run tellraw @a[tag=mtga.player] {"text":"Red wins the duel!","color":"gold"}
execute if score #winner mtg matches 2 run tellraw @a[tag=mtga.player] {"text":"Green wins the duel!","color":"gold"}
function mtga:game/stop
