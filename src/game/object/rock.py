import random
from game.action.gameaction import GameAction
from game.gameobject import GameObject
from game.gamestate import GameState
from move.movementaction import MovementAction

from move.coordinate import Coordinate
from scene import Scene

class Rock(GameObject):
    def __init__(self, x, y):
        super().__init__()
        # self.x = 50
        # self.y = 50
        self.x = x
        self.y = y
        self._speed = 1
        self._bitmap_x = 16
        self._bitmap_y = 0

    def get_left_up_corner(self) -> Coordinate:
        return Coordinate(self.x, self.y)

    def get_left_down_corner(self) -> Coordinate:
        return Coordinate(self.x, self.y + self._object_height)

    def get_right_down_corner(self) -> Coordinate:
        return Coordinate(self.x + self._object_width, self.y + self._object_height)

    def get_right_up_corner(self) -> Coordinate:
        return Coordinate(self.x + self._object_width, self.y)

    def get_action(self, game_state: GameState, scene: Scene) -> GameAction:
        return None

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