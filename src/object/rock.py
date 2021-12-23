import random

class Rock:
    def __init__(self):
        self.x = 50
        self.y = 50
        self.player_vy = 0
    
    def move_random(self):
        if self.x > 0:
            self.x += random.randint(-1, 1)

        if self.y > 0:
            self.y += random.randint(-1, 1)
