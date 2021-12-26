from typing import overload
from move.movementaction import MovementAction
from move.coordinate import Coordinate


class GameObject(object):
    def __init__(self) -> None:
        super().__init__()
        self._object_width: int = 16
        self._object_height: int = 16
        self._horizontal_direction = 1 # positive one is no filp, -1 is flip
        self._vertical_direction = 1 # positive one is no filp, -1 is flip
        self.x = 0
        self.y = 0
        self._speed = 1
        self._bitmap_x = 64
        self._bitmap_y = 0

    @overload
    def get_left_up_corner(self) -> Coordinate:
        pass

    @overload
    def get_left_down_corner(self) -> Coordinate:
        pass

    @overload
    def get_right_down_corner(self) -> Coordinate:
        pass

    @overload
    def get_right_up_corner(self) -> Coordinate:
        pass

    @overload 
    def get_action(self) -> MovementAction:
        pass

    @overload 
    def apply_action(self, action: MovementAction):
        pass

    @overload 
    def bitmap_x(self) -> int:
        pass

    @overload 
    def bitmap_y(self) -> int:
        pass

    @overload 
    def get_obj_horiz_tilemap_size(self) -> int:
        pass

    @overload 
    def get_obj_vert_tilemap_size(self) -> int:
        pass