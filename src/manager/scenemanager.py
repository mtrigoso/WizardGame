from typing import List
import pyxel
from game.gameobject import GameObject
from scene.firstscene import FirstScene
from game.object.rock import Rock
from player import Player
from scene import Scene
from scene.sceneobject import SceneObject
from scene.secondscene import SecondScene

class SceneManager():
    def __init__(self, player: Player, enemies: List[GameObject]):
        self.scene: SceneObject = FirstScene(player, enemies)
        self.player = player
        self.enemies = enemies

    def update(self):
        scene_transition = self.scene.update()
        if scene_transition == Scene.SECOND_LEVEL: 
            self.scene = SecondScene(self.player)
        elif scene_transition == Scene.FIRST_LEVEL:
            self.scene = FirstScene(self.player, self.enemies)
        elif scene_transition == Scene.NO_SCENE_CHANGE:
            pass
        elif scene_transition == None: 
            pass
        else:
            raise Exception("I have no clue what went wrong")

    def draw(self):
        self.scene.draw()
