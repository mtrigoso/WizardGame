from typing import overload
from game.gameobject import GameObject
from move.coordinate import Coordinate


class Player(GameObject):
    def __init__(self):
        self.x = 0
        self.y = 0

    def go_left(self) Coor:
        # self.x = self.x - 1

    def go_right(self):
        self.x = self.x + 1

    def go_up(self):
        self.y = self.y - 1

    def go_down(self):
        self.y = self.y + 1
    
    def get_left_up_corner(self) -> Coordinate:
        return Coordinate(self.x, self.y)

    def get_left_down_corner(self) -> Coordinate:
        return Coordinate(self.x, self.y + 16)

    def get_right_down_corner(self) -> Coordinate:
        return Coordinate(self.x + 16, self.y + 16)

    def get_right_up_corner(self) -> Coordinate:
        return Coordinate(self.x + 16, self.y)