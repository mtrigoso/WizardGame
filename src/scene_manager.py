import pyxel
from firstscene import FirstScene
from player import Player
# import mission_select
# import menu
from scene import Scene
# import mission_manager
# import missions
import sys

from secondscene import SecondScene

class SceneManager():

    def __init__(self, player: Player):
        self.scene = FirstScene(player)
        self.player = player

    def update(self):
        scene_transition = self.scene.update()
        if scene_transition == Scene.SECOND_LEVEL: 
            self.scene = SecondScene(self.player)
        elif scene_transition == Scene.FIRST_LEVEL:
            self.scene = FirstScene(self.player)
        elif scene_transition == Scene.NO_SCENE_CHANGE:
            pass
        elif scene_transition == None: 
            pass
        else:
            raise Exception("I have no clue what went wrong")

    def draw(self):
        self.scene.draw()
