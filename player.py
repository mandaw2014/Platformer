from mandaw import *

class PlatformerController2D(Entity):
    def __init__(self, window, x = 0, y = 0, centered = True):
        super().__init__(
            window,
            width = 15,
            height = 35,
            x = x,
            y = y,
            color = color["orange"]
        )

        if centered == True:
            self.center()
        else:
            pass
        
        self.window = window

        self.pos_x = 0

        self.pos = self.window.width / 2 - 15

        self.is_jumping = False
        self.jump_y = 500

        self.direction = None

        self.velocity_y = 1

        self.objects = []

        self.speed = 50
        self.maxspeed = 160

        self.ignore_speed = []

        self.lava = []
        self.xpos = []

        self.original_pos()

    def movement(self, dt):
        # Player movement
        if self.window.input.pressed[self.window.input.keys["A"]]:
            self.pos_x -= self.speed
            self.direction = 0

        if self.window.input.pressed[self.window.input.keys["D"]]:
            self.pos_x += self.speed
            self.direction = 1

        # Momentum
        if self.pos_x >= self.maxspeed:
            self.pos_x = self.maxspeed
        if self.pos_x <= -self.maxspeed:
            self.pos_x = -self.maxspeed

        for i in range(len(self.objects)):
            self.objects[i].x -= self.pos_x * dt
        
        for i in range(len(self.lava)):
            self.lava[i].x -= self.pos_x * dt

        if self.y <= 250:
            self.y += 100 * dt
            for i in range(len(self.objects)):
                self.objects[i].y += 100 * dt
        
        if self.y >= 400:
            self.y -= 100 * dt
            for i in range(len(self.objects)):
                self.objects[i].y -= 100 * dt
			
        if self.y <= 250:
            self.y += 100 * dt
            for i in range(len(self.lava)):
                self.lava[i].y += 100 * dt
        
        if self.y >= 400:
            self.y -= 100 * dt
            for i in range(len(self.lava)):
                self.lava[i].y -= 100 * dt
        

        # Gravity
        if not self.collidelist(self.objects) and self.is_jumping == False:
            self.y += 4 * self.velocity_y
            self.velocity_y += 2 * dt

        if self.collidelist(self.objects):
            self.velocity_y = 1

            if self.direction == 0 and not self.window.input.pressed[self.window.input.keys["A"]]:
                self.pos_x += 10

                if self.pos_x >= 0:
                    self.pos_x = 0
            
            if self.direction == 1 and not self.window.input.pressed[self.window.input.keys["D"]]:
                self.pos_x -= 10

                if self.pos_x <= 0:
                    self.pos_x = 0

        if not self.collidelist(self.objects):
            if self.direction == 0 and not self.window.input.pressed[self.window.input.keys["A"]]:
                self.pos_x += 0.1

                if self.pos_x >= 0:
                    self.pos_x = 0
            
            if self.direction == 1 and not self.window.input.pressed[self.window.input.keys["D"]]:
                self.pos_x -= 0.1

                if self.pos_x <= 0:
                    self.pos_x = 0

        self.jump(dt)

    def jump(self, dt):
        # Jumping
        if self.is_jumping == False and self.window.input.pressed[self.window.input.keys["SPACE"]]:
            self.is_jumping = True
            if not self.collidelist(self.objects):
                self.is_jumping = False

        if self.is_jumping == True:
            self.y -= self.jump_y * dt
            self.jump_y -= 50

            if self.jump_y < -250:
                self.is_jumping = False
                self.jump_y = 500

    def dead(self):
        for i in range(len(self.objects)):
            self.objects[i].x = self.xpos[i]
            for j in range(len(self.lava)):
                self.lava[j].x = self.xpos[j - 1]

        self.y = 300
        self.pos_x = 0

    def original_pos(self):
        for i in range(len(self.objects)):
            self.xpos.append(self.objects[i].x)
            for i in range(len(self.lava)):
                self.xpos.append(self.lava[i].x)
