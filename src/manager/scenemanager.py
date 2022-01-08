from typing import List
import pyxel
from game.gameobject import GameObject
from game.gamestate import GameState
from scene.firstscene import FirstScene
from game.object.rock import Rock
from user.player import Player
from scene import Scene
from scene.sceneobject import SceneObject
from scene.secondscene import SecondScene


class SceneManager():
    def __init__(self, player: Player, game_state: GameState, starting_scene: Scene):
        self._player = player
        self._game_state = game_state
        self._scene = self.init_scene(starting_scene)

    def update(self):
        scene_transition = self._scene.update()

        if scene_transition == Scene.SECOND_SCENE:
            self._game_state.saved_state["player_y"].append(0)
            self._scene = SecondScene(self._player, self._game_state)
        elif scene_transition == Scene.FIRST_SCENE:
            self._player.y = self._game_state.saved_state["player_y"].pop()
            self._scene = FirstScene(self._player, self._game_state)
        elif scene_transition == Scene.NO_SCENE_CHANGE:
            pass
        elif scene_transition == None:
            pass
        else:
            raise Exception("I have no clue what went wrong")

    def draw(self):
        self._scene.draw()

    def init_scene(self, scene: Scene) -> SceneObject:
        scene_obj = [scn for scn in [FirstScene, SecondScene]
                     if scn.SCENE_TYPE == scene].pop()
        return scene_obj(self._player, self._game_state)
