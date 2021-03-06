from typing import List, Tuple
import pyxel
from game.projectile.lightningbolt import LightningBolt
from game.gameobject import GameObject
from game.gamestate import GameState
from game.object.rock import Rock
from manager.actionmanager import ActionManager
from scene import tilemap
from scene.tilemap import TileMap
from user.player import Player
from scene import Scene
from scene.sceneobject import SceneObject


class FirstScene(SceneObject):
    SCENE_TYPE = Scene.FIRST_SCENE

    def __init__(self, player: Player, game_state: GameState):
        super().__init__()
        self._player = player
        self._game_state = game_state
        self._action_manager = ActionManager(self._game_state)
        self._background = TileMap()

    def update(self) -> Scene | None:
        # 1: check to see if the player request to move to another scene
        if self._player.y < int(self._game_state.scene_settings[self.SCENE_TYPE]["min_y"]):
            # move over any objects between scenes
            going_to = Scene.SECOND_SCENE
            rock = self._game_state.get_first_obj(self.SCENE_TYPE, Rock)
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
    
        return None

    def draw(self):
        # draw the tile map for background
        pyxel.bltm(
            0,
            0,
            self._background._tile_num,
            self._background._bitmap_x,
            self._background._bitmap_y,
            self._background._object_width,
            self._background._object_height,
        )


        # draw each object
        for obj in self._game_state.objects_in_scene(self.SCENE_TYPE):
            pyxel.blt(
                obj.get_left_up_corner().x,
                obj.get_left_up_corner().y,
                obj.image_num,
                obj.bitmap_x(),
                obj.bitmap_y(),
                obj.get_obj_horiz_tilemap_size(),
                obj.get_obj_vert_tilemap_size(),
                colkey=obj.get_transparent_color()
            )
