import random
from game.action.gameaction import GameAction
from game.gameobject import GameObject
from game.gamestate import GameState
from move.movementaction import MovementAction

from move.coordinate import Coordinate

class Troll(GameObject):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self._speed = 1
        self._bitmap_x = 32
        self._bitmap_y = 0
    
    def move_random(self) -> MovementAction:
        x = 0
        y = 0
        if self.x > 0:
            x += random.randint(-self._speed, self._speed)

        if self.y > 0:
            y += random.randint(-self._speed, self._speed)

        return MovementAction(self.x, self.y, self.x + x, self.y + y, self._horizontal_direction)

    def get_left_up_corner(self) -> Coordinate:
        return Coordinate(self.x, self.y)

    def get_left_down_corner(self) -> Coordinate:
        return Coordinate(self.x, self.y + self._object_width)

    def get_right_down_corner(self) -> Coordinate:
        return Coordinate(self.x + self._object_width, self.y + self._object_width)

    def get_right_up_corner(self) -> Coordinate:
        return Coordinate(self.x + self._object_width, self.y)

    def get_action(self, game_state: GameState) -> GameAction:
        return self.move_random()

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