import random
from game.gameobject import GameObject
from move.movementaction import MovementAction

from move.coordinate import Coordinate

class Rock(GameObject):
    def __init__(self):
        super().__init__()
        self.x = 50
        self.y = 50
        self._speed = 1
        self._bitmap_x = 16
        self._bitmap_y = 0

    def get_left_up_corner(self) -> Coordinate:
        return Coordinate(self.x, self.y)

    def get_left_down_corner(self) -> Coordinate:
        return Coordinate(self.x, self.y + self.OBJECT_WIDTH)

    def get_right_down_corner(self) -> Coordinate:
        return Coordinate(self.x + self.OBJECT_WIDTH, self.y + self.OBJECT_WIDTH)

    def get_right_up_corner(self) -> Coordinate:
        return Coordinate(self.x + self.OBJECT_WIDTH, self.y)

    def get_action(self) -> MovementAction:
        return None

    def apply_action(self, action: MovementAction):
        self.x = action.to_x
        self.y = action.to_y

    def bitmap_x(self) -> int:
        return self._bitmap_x

    def bitmap_y(self) -> int:
        return self._bitmap_y

    def get_obj_horiz_tilemap_size(self) -> int:
        return self.OBJECT_WIDTH