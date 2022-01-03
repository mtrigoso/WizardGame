from typing import List, Tuple
import pyxel
from game.gameobject import GameObject
from game.gamestate import GameState
from game.object.rock import Rock
from game.tempgameobject import TempGameObject
from manager.actionmanager import ActionManager
from move.movementaction import MovementAction
from user.player import Player
from scene import Scene
from scene.sceneobject import SceneObject


class SecondScene(SceneObject):
    SCENE_TYPE = Scene.SECOND_SCENE

    def __init__(self, player: Player, game_state: GameState):
        super().__init__()
        self._player = player
        self._player.y = 120
        self._game_state: GameState = game_state
        self._action_manager = ActionManager(self._game_state)

    def update(self) -> Scene | None:
        # 1: check to see if the player request to move to another scene
        if self._player.y > 128:
            # move over any objects between scenes
            going_to = Scene.FIRST_SCENE
            rock = self._game_state.get_obj(self.SCENE_TYPE, Rock)[0]
            self._game_state.move_objs_between_scenes(
                [self._player, rock], self.SCENE_TYPE, going_to)
            return going_to

        for game_object in self._game_state.objects_in_scene(self.SCENE_TYPE):
            # 2: handle input and construct an action from there
            action = game_object.get_action(self._game_state, self.SCENE_TYPE)

            if action:
                # 3: check if the action is valid - if it is, apply that action
                self._action_manager.parse_action(
                    game_object, action, self.SCENE_TYPE)
        self._game_state.remove_all_removed_objects(self.SCENE_TYPE)

    def draw(self):
        pyxel.cls(1)
        for obj in self._game_state.objects_in_scene(self.SCENE_TYPE):
            pyxel.blt(
                obj.get_left_up_corner().x,
                obj.get_left_up_corner().y,
                0,
                obj.bitmap_x(),
                obj.bitmap_y(),
                obj.get_obj_horiz_tilemap_size(),
                obj.get_obj_vert_tilemap_size(),
            )
