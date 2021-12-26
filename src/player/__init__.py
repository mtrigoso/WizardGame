from typing import overload

import pyxel
from game.gameobject import GameObject
from move.action import Action
from move.coordinate import Coordinate


class Player(GameObject):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self._speed = 5
        self._bitmap_x = 0
        self._bitmap_y = 0

    def go_left(self) -> Action:
        return Action(self.x, self.y, self.x-self._speed, self.y)

    def go_right(self) -> Action:
        return Action(self.x, self.y, self.x+self._speed, self.y)

    def go_up(self) -> Action:
        return Action(self.x, self.y, self.x, self.y-self._speed)

    def go_down(self) -> Action:
        return Action(self.x, self.y, self.x, self.y+self._speed)
    
    def get_left_up_corner(self) -> Coordinate:
        return Coordinate(self.x, self.y)

    def get_left_down_corner(self) -> Coordinate:
        return Coordinate(self.x, self.y + self.OBJECT_WIDTH)

    def get_right_down_corner(self) -> Coordinate:
        return Coordinate(self.x + self.OBJECT_WIDTH, self.y + self.OBJECT_WIDTH)

    def get_right_up_corner(self) -> Coordinate:
        return Coordinate(self.x + self.OBJECT_WIDTH, self.y)

    def get_action(self) -> Action:
        if pyxel.btn(pyxel.KEY_LEFT):
            return self.go_left()

        if pyxel.btn(pyxel.KEY_RIGHT):
            return self.go_right()

        if pyxel.btn(pyxel.KEY_UP):
            return self.go_up()

        if pyxel.btn(pyxel.KEY_DOWN):
            return self.go_down()
        return None

    def apply_action(self, action: Action):
        self.x = action.to_x
        self.y = action.to_y

    def bitmap_x(self) -> int:
        return self._bitmap_x

    def bitmap_y(self) -> int:
        return self._bitmap_y