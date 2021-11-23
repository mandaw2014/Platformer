from mandaw import *
from player import PlatformerController2D

from levels.level01 import Level01

mandaw = Mandaw(title = "Platformer", width = 800, height = 600, bg_color = (125, 255, 255, 255))

player = PlatformerController2D(mandaw, x = 0, y = 0)

level01 = Level01(mandaw, player)

@mandaw.draw
def draw():
    player.draw()

    level01.draw()

@mandaw.update
def update(dt):
    player.movement(dt)
    
    if player.collide(level01.platform_7):
        player.jump_y = 1000 

    level01.update(dt)

mandaw.loop()
