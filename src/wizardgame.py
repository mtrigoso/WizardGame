import pyxel
import game
from game.enemy.troll import Troll
from game.gamestate import GameState
from game.object.rock import Rock
from scene import Scene
from user.player import Player
from manager.scenemanager import SceneManager


class WizardGame:
    SCREEN_WIDTH = 128
    SCREEN_HEIGHT = 128
    def __init__(self):
        pyxel.init(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self._player = Player()
        self._game_state = GameState.instance()
        self._game_state = GameState.instance()
        # self._game_state = GameState()
        objects_in_scene = [
            Rock(100, 100),
            Rock(0, 90),
            Troll(25, 25),
            Troll(120, 75),
            Troll(90, 50),
            Troll(75, 75),
            Troll(120, 0),
        ]

        self._game_state.scene_settings[Scene.FIRST_SCENE] = {}
        self._game_state.scene_settings[Scene.FIRST_SCENE]["min_y"] = 0

        self._game_state.scene_settings[Scene.SECOND_SCENE] = {}
        self._game_state.scene_settings[Scene.SECOND_SCENE]["max_y"] = self.SCREEN_HEIGHT

        # load the scenes with their appropiate objects
        self._game_state.set_objects_in_scene(
            Scene.FIRST_SCENE, [self._player] + objects_in_scene)

        self._game_state.set_objects_in_scene(
            Scene.SECOND_SCENE, [])

        self._scene_manager = SceneManager(
            self._player, self._game_state, Scene.FIRST_SCENE)

        pyxel.load("assets/wizardgame.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        self._scene_manager.update()

    def draw(self):
        self._scene_manager.draw()


WizardGame()
