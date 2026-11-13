scoreboard objectives add mtg dummy
scoreboard objectives add mtg.session dummy
scoreboard objectives add mtg.menu trigger
scoreboard objectives add mtg.play trigger
scoreboard objectives add mtg.attack trigger
scoreboard objectives add mtg.block trigger
scoreboard objectives add mtg.end trigger
scoreboard players set #installed mtg 1
scoreboard players set #active mtg 0
scoreboard players set #bot mtg 0
scoreboard players set #session mtg 0
data modify storage mtga:meta installed set value 1b
