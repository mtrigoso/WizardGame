import random
from game.action.gameaction import GameAction
from game.gameobject import GameObject
from move.coordinate import Coordinate
from move.movementaction import MovementAction
from move.movevector import MoveVector


class LightningBolt(GameObject):
    def __init__(self, direction: MoveVector):
        super().__init__()
        self.x = 20
        # self.y = y
        self._speed = 1
        self._bitmap_x = 48
        self._bitmap_y = 0
        self._object_height = 8
        self._move_vector = direction
    
    def move_in_direction(self) -> MovementAction:
        if self._move_vector == MoveVector.RIGHT:
            return MovementAction(self.x, self.y, self.x + self._speed, self.y)

    def get_left_up_corner(self) -> Coordinate:
        return Coordinate(self.x, self.y)

    def get_left_down_corner(self) -> Coordinate:
        return Coordinate(self.x, self.y + self._object_height)

    def get_right_down_corner(self) -> Coordinate:
        return Coordinate(self.x + self._object_width, self.y + self._object_height)

    def get_right_up_corner(self) -> Coordinate:
        return Coordinate(self.x + self._object_width, self.y)

    def get_action(self) -> GameAction:
        return self.move_in_direction()

    def apply_action(self, action: MovementAction):
        self.x = action.to_x
        self.y = action.to_y

    def bitmap_x(self) -> int:
        return self._bitmap_x

    def bitmap_y(self) -> int:
        return self._bitmap_y

    def get_obj_horiz_tilemap_size(self) -> int:
        return self._object_width

    def get_obj_vert_tilemap_size(self) -> int:
        return self._object_height