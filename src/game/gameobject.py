from typing import overload
from move.coordinate import Coordinate


class GameObject(object):
    def __init__(self) -> None:
        super().__init__()

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