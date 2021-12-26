
from game.gameobject import GameObject
from move.movementaction import MovementAction
from move.coordinate import Coordinate


class TempGameObject(GameObject):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.x = x
        self.y = y
        

    def get_left_up_corner(self) -> Coordinate:
        return Coordinate(self.x, self.y)

    def get_left_down_corner(self) -> Coordinate:
        return Coordinate(self.x, self.y + self._object_width)

    def get_right_down_corner(self) -> Coordinate:
        return Coordinate(self.x + self._object_width, self.y + self._object_width)

    def get_right_up_corner(self) -> Coordinate:
        return Coordinate(self.x + self._object_width, self.y)
