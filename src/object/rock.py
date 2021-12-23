import random
from game.gameobject import GameObject
from move.action import Action

from move.coordinate import Coordinate

class Rock(GameObject):
    def __init__(self):
        super().__init__()
        self.x = 50
        self.y = 50
    
    def move_random(self) -> Action:
        x = 0
        y = 0
        if self.x > 0:
            x += random.randint(-1, 1)

        if self.y > 0:
            y += random.randint(-1, 1)

        return Action(self.x, self.y, self.x + x, self.y + y)

    def get_left_up_corner(self) -> Coordinate:
        return Coordinate(self.x, self.y)

    def get_left_down_corner(self) -> Coordinate:
        return Coordinate(self.x, self.y + self.OBJECT_WIDTH)

    def get_right_down_corner(self) -> Coordinate:
        return Coordinate(self.x + self.OBJECT_WIDTH, self.y + self.OBJECT_WIDTH)

    def get_right_up_corner(self) -> Coordinate:
        return Coordinate(self.x + self.OBJECT_WIDTH, self.y)

    def get_action(self) -> Action:
        return self.move_random()

    def apply_action(self, action: Action):
        self.x = action.to_x
        self.y = action.to_y