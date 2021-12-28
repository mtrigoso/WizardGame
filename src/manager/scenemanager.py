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
    def __init__(self, player: Player, enemies: List[GameObject], game_state: GameState):
        self.player = player
        self.enemies = enemies
        self._game_state = game_state
        self.scene: SceneObject = FirstScene(player, enemies, self._game_state)

    def update(self):
        scene_transition = self.scene.update()
        if scene_transition == Scene.SECOND_LEVEL: 
            self.scene = SecondScene(self.player)
        elif scene_transition == Scene.FIRST_LEVEL:
            self.scene = FirstScene(self.player, self.enemies, self._game_state)
        elif scene_transition == Scene.NO_SCENE_CHANGE:
            pass
        elif scene_transition == None: 
            pass
        else:
            raise Exception("I have no clue what went wrong")

    def draw(self):
        self.scene.draw()
