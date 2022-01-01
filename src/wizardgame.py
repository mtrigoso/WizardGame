import pyxel
import game
from game.enemy.troll import Troll
from game.gamestate import GameState
from game.object.rock import Rock
from scene import Scene
from user.player import Player
from manager.scenemanager import SceneManager


class WizardGame:
    SCREEN_WIDTH = 160
    SCREEN_HEIGHT = 120
    def __init__(self):
        pyxel.init(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        self._player = Player()
        self._game_state = GameState.instance()
        enemies = [
            Rock(50, 50),
            Troll(25, 25),
            Troll(120, 75),
            Troll(90, 50),
            Troll(75, 75),
            Troll(100, 100),
        ]

        # load the scenes with their appropiate objects
        self._game_state.set_objects_in_scene(
            Scene.FIRST_SCENE, [self._player] + enemies)

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
