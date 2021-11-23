from mandaw import *

class Ground(Entity):
    def __init__(self, window, width = 100, height = 1000, x = 0, y = 500):
        super().__init__(
            window,
            width = width,
            height = height,
            x = x,
            y = y,
            color = (150, 150, 150, 255)
        )

class Lava(Entity):
    def __init__(self, window, width = 1000, height = 1000, x = 0, y = 525):
        super().__init__(
            window,
            width = width,
            height = height,
            x = x,
            y = y,
            color = (255, 100, 0, 255)
        )

class Platform(Entity):
    def __init__(self, window, x = 0, y = 0):
        super().__init__(
            window,
            width = 80,
            height = 10,
            x = x,
            y = y,
            color = (80, 255, 80, 255)
        )

class JumpPlatform(Entity):
    def __init__(self, window, player, jump_height, x = 0, y = 0):
        super().__init__(
            window,
            width = 80,
            height = 10,
            x = x,
            y = y,
            color = color["orange"]
        )

        self.player = player
        self.jump_height = jump_height

    def update(self):
        if self.player.collide(self):
            self.player.jump_y = self.jump_height
        else:
            self.player.jump_y = 500
