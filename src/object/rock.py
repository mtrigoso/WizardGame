import random

from move.coordinate import Coordinate

class Rock:
    def __init__(self):
        self.x = 50
        self.y = 50
    
    def move_random(self):
        if self.x > 0:
            self.x += random.randint(-1, 1)

        if self.y > 0:
            self.y += random.randint(-1, 1)

    def get_left_up_corner(self) -> Coordinate:
        return Coordinate(self.x, self.y)

    def get_left_down_corner(self) -> Coordinate:
        return Coordinate(self.x, self.y + 16)

    def get_right_down_corner(self) -> Coordinate:
        return Coordinate(self.x + 16, self.y + 16)

    def get_right_up_corner(self) -> Coordinate:
        return Coordinate(self.x + 16, self.y)