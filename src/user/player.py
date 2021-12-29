from math import modf
from typing import Tuple
import pyxel
from battle.projectileaction import ProjectileAction
from game.action.gameaction import GameAction
from game.gameobject import GameObject
from game.gamestate import GameState
from game.projectile.lightningbolt import LightningBolt
from move.movementaction import MovementAction
from move.coordinate import Coordinate
from move.movevector import MoveVector
from scene import Scene


class Player(GameObject):
    def __init__(self):
        super().__init__()
        self.x = 0
        self.y = 0
        self._speed = 4
        self._bitmap_x = 0
        self._bitmap_y = 0
        self._move_vector = MoveVector.RIGHT

    def go_left(self) -> MovementAction:
        return MovementAction(self.x, self.y, self.x-self._speed, self.y, MoveVector.LEFT)

    def go_right(self) -> MovementAction:
        return MovementAction(self.x, self.y, self.x+self._speed, self.y, MoveVector.RIGHT)

    def go_up(self) -> MovementAction:
        return MovementAction(self.x, self.y, self.x, self.y-self._speed, MoveVector.UP)

    def go_down(self) -> MovementAction:
        return MovementAction(self.x, self.y, self.x, self.y+self._speed, MoveVector.DOWN)

    def get_left_up_corner(self) -> Coordinate:
        return Coordinate(self.x, self.y)

    def get_left_down_corner(self) -> Coordinate:
        return Coordinate(self.x, self.y + self._object_width)

    def get_right_down_corner(self) -> Coordinate:
        return Coordinate(self.x + self._object_width, self.y + self._object_width)

    def get_right_up_corner(self) -> Coordinate:
        return Coordinate(self.x + self._object_width, self.y)

    def get_projectile_action(self, game_state: GameState, scene: Scene) -> GameAction:
        if any(obj for obj in game_state.objects_in_scene(scene) if type(obj) == LightningBolt):
            return

        if pyxel.btn(pyxel.KEY_H):
            return ProjectileAction(LightningBolt, MoveVector.LEFT, self.x - 16, self.y)

        if pyxel.btn(pyxel.KEY_J):
            return ProjectileAction(LightningBolt, MoveVector.DOWN, self.x, self.y + 16)

        if pyxel.btn(pyxel.KEY_K):
            return ProjectileAction(LightningBolt, MoveVector.UP, self.x, self.y - 16)

        if pyxel.btn(pyxel.KEY_L):
            return ProjectileAction(LightningBolt, MoveVector.RIGHT, self.x + 16, self.y)

    def get_action(self, game_state: GameState, scene: Scene) -> GameAction:
        if pyxel.btn(pyxel.KEY_LEFT):
            return self.go_left()

        if pyxel.btn(pyxel.KEY_RIGHT):
            return self.go_right()

        if pyxel.btn(pyxel.KEY_UP):
            return self.go_up()

        if pyxel.btn(pyxel.KEY_DOWN):
            return self.go_down()
        
        return self.get_projectile_action(game_state, scene)

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
            return self._object_width
        if self._move_vector == MoveVector.RIGHT:    
            return -self._object_width
        return self._object_width

    def get_obj_vert_tilemap_size(self) -> int:
        if self._move_vector == MoveVector.UP:
            return self._object_height
        if self._move_vector == MoveVector.DOWN:
            return self._object_height
        return self._object_height
