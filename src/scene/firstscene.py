from typing import List
import pyxel
from game.gameobject import GameObject
from game.gamestate import GameState
from game.projectile.lightningbolt import LightningBolt
from game.tempgameobject import TempGameObject
from manager.actionmanager import ActionManager
from manager.collisionmanager import CollisionManager
from move.movementaction import MovementAction
from game.object.rock import Rock

from user.player import Player
from scene import Scene
from scene.sceneobject import SceneObject


class FirstScene(SceneObject):
    SCENE_TYPE = Scene.FIRST_LEVEL

    def __init__(self, player: Player, enemies: List[GameObject], game_state: GameState):
        super().__init__()
        self.player = player
        self._game_state: GameState = game_state
        self._game_state.set_objects_in_scene(
            self.SCENE_TYPE, [self.player] + enemies)
        self._action_manager = ActionManager(self._game_state)

    def update(self) -> Scene | None:
        # 1: check to see if the player request to move to another scene
        if self.player.y < 0:
            return Scene.SECOND_LEVEL

        for game_object in self._game_state.objects_in_scene(self.SCENE_TYPE):
            # 2: handle input and construct an action from there
            action = game_object.get_action(self._game_state, self.SCENE_TYPE)

            if action:
                # 3: check if the action is valid - if it is, apply that action
                self._action_manager.parse_action(
                    game_object, action, Scene.FIRST_LEVEL)

    def draw(self):
        pyxel.cls(0)
        for obj in self._game_state.objects_in_scene(self.SCENE_TYPE):
            # if isinstance(obj, LightningBolt):
            #     print(f"{obj.get_left_up_corner().x}, {obj.get_left_up_corner().y}")
            pyxel.blt(
                obj.get_left_up_corner().x,
                obj.get_left_up_corner().y,
                0,
                obj.bitmap_x(),
                obj.bitmap_y(),
                obj.get_obj_horiz_tilemap_size(),
                obj.get_obj_vert_tilemap_size(),
            )
