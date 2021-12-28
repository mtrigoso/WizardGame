import random
from game.action.gameaction import GameAction
from game.gameobject import GameObject
from game.gamestate import GameState
from move.movementaction import MovementAction

from move.coordinate import Coordinate
from move.movevector import MoveVector
from scene import Scene


class Troll(GameObject):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self._speed = 1
        self._bitmap_x = 32
        self._bitmap_y = 0
        self._move_vector: MoveVector = MoveVector.LEFT

    def move_random(self) -> MovementAction:
        x = 0
        y = 0

        direction = random.choice(
            [MoveVector.LEFT, MoveVector.RIGHT, MoveVector.UP, MoveVector.DOWN])
        if direction == MoveVector.LEFT:
            x = -1
        elif direction == MoveVector.RIGHT:
            x = 1
        elif direction == MoveVector.UP:
            y = -1
        elif direction == MoveVector.DOWN:
            y = 1

        return MovementAction(
            self.x,
            self.y,
            self.x + x,
            self.y + y,
            direction,
        )

    def get_left_up_corner(self) -> Coordinate:
        return Coordinate(self.x, self.y)

    def get_left_down_corner(self) -> Coordinate:
        return Coordinate(self.x, self.y + self._object_width)

    def get_right_down_corner(self) -> Coordinate:
        return Coordinate(self.x + self._object_width, self.y + self._object_width)

    def get_right_up_corner(self) -> Coordinate:
        return Coordinate(self.x + self._object_width, self.y)

    def get_action(self, game_state: GameState, scene: Scene) -> GameAction:
        return self.move_random()

    def apply_action(self, action: MovementAction):
        self.x = action.to_x
        self.y = action.to_y
        self._move_vector = action.vector

    def bitmap_x(self) -> int:
        return self._bitmap_x

    def bitmap_y(self) -> int:
        return self._bitmap_y

    def get_obj_horiz_tilemap_size(self) -> int:
        if self._move_vector == MoveVector.LEFT:
            return -self._object_width
        if self._move_vector == MoveVector.RIGHT:
            return self._object_width
        return self._object_width

    def get_obj_vert_tilemap_size(self) -> int:
        return self._object_height
