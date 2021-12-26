from typing import overload
from move.movementaction import MovementAction
from move.coordinate import Coordinate


class GameObject(object):
    def __init__(self) -> None:
        super().__init__()
        self.OBJECT_WIDTH: int = 16
        self._horizontal_direction = 1

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