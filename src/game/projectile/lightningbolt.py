import random
from game.action.gameaction import GameAction
from game.gameobject import GameObject
from game.gamestate import GameState
from move.coordinate import Coordinate
from move.movementaction import MovementAction
from move.movevector import MoveVector
from scene import Scene


class LightningBolt(GameObject):
    def __init__(self, direction: MoveVector, x: int, y: int):
        super().__init__()
        self.x = x
        self.y = y
        self._speed = 2
        self._bitmap_y = 0
        self._object_width = 8
        self._move_vector = direction
    
    def move_in_direction(self) -> MovementAction:
        if self._move_vector == MoveVector.RIGHT:
            return MovementAction(self.x, self.y, self.x + self._speed, self.y, self._move_vector)

        if self._move_vector == MoveVector.LEFT:
            return MovementAction(self.x, self.y, self.x - self._speed, self.y, self._move_vector)

        if self._move_vector == MoveVector.UP:
            return MovementAction(self.x, self.y, self.x, self.y - self._speed, self._move_vector)

        if self._move_vector == MoveVector.DOWN:
            return MovementAction(self.x, self.y, self.x, self.y + self._speed, self._move_vector)


    def get_left_up_corner(self) -> Coordinate:
        return Coordinate(self.x, self.y)

    def get_left_down_corner(self) -> Coordinate:
        return Coordinate(self.x, self.y + self._object_height)

    def get_right_down_corner(self) -> Coordinate:
        return Coordinate(self.x + self._object_width, self.y + self._object_height)

    def get_right_up_corner(self) -> Coordinate:
        return Coordinate(self.x + self._object_width, self.y)

    def get_action(self, game_state: GameState, scene: Scene) -> GameAction:
        return self.move_in_direction()

    def apply_action(self, action: MovementAction):
        self.x = action.to_x
        self.y = action.to_y
        self._move_vector = action.vector

        #depending on the direction the object is moving, we may need to get a different square from the bitmap
        if self._move_vector in [MoveVector.DOWN, MoveVector.UP]:
            self._object_height = 16
            self._object_width = 8
            self._bitmap_x = 64
        elif self._move_vector in [MoveVector.LEFT, MoveVector.RIGHT]:
            self._object_height = 8
            self._object_width = 16
            self._bitmap_x = 48

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
        if self._move_vector == MoveVector.UP:
            return self._object_height
        if self._move_vector == MoveVector.DOWN:
            return -self._object_height
        return self._object_height