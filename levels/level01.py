from mandaw import *
from platforms import *

class Level01:
    def __init__(self, window, player):
        self.window = window
        self.player = player

        self.ground = Ground(self.window, 200, 1000, 250, 500)

        self.lava = Lava(self.window, 2000, 1000, 400, 525)

        self.platform_1 = Platform(self.window, 505, 480)
        self.platform_2 = Platform(self.window, 625, 480)
        self.platform_3 = Platform(self.window, 745, 480)
        self.platform_4 = Platform(self.window, 865, 480)
        self.platform_5 = Platform(self.window, 985, 460)
        self.platform_6 = Platform(self.window, 1105, 430)

        self.platform_7 = JumpPlatform(self.window, self.platform_1, 8000, 1225, 480)

        self.enable()

    def enable(self):
        self.player.objects.append(self.ground)
        self.player.lava.append(self.lava)

        self.player.objects.append(self.platform_1)
        self.player.objects.append(self.platform_2)
        self.player.objects.append(self.platform_3)
        self.player.objects.append(self.platform_4)
        self.player.objects.append(self.platform_5)
        self.player.objects.append(self.platform_6)
        self.player.objects.append(self.platform_7)

        self.player.original_pos()

    def disable(self):
        self.player.objects.remove(self.ground)
        self.player.lava.remove(self.lava)

        self.player.objects.remove(self.platform_1)
        self.player.objects.remove(self.platform_2)
        self.player.objects.remove(self.platform_3)
        self.player.objects.remove(self.platform_4)
        self.player.objects.remove(self.platform_5)
        self.player.objects.remove(self.platform_6)
        self.player.objects.remove(self.platform_7)

    def draw(self):
        self.lava.draw()
        self.ground.draw()

        self.platform_1.draw()
        self.platform_2.draw()
        self.platform_3.draw()
        self.platform_4.draw()
        self.platform_5.draw()
        self.platform_6.draw()
        self.platform_7.draw()

    def update(self, dt):
        self.platform_7.update()
