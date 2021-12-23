import pyxel
from scene.firstscene import FirstScene
from object.rock import Rock
from player import Player
from scene import Scene
from scene.secondscene import SecondScene

class SceneManager():

    def __init__(self, player: Player, rock: Rock):
        self.scene = FirstScene(player, rock)
        self.player = player
        self.rock = rock

    def update(self):
        scene_transition = self.scene.update()
        if scene_transition == Scene.SECOND_LEVEL: 
            self.scene = SecondScene(self.player)
        elif scene_transition == Scene.FIRST_LEVEL:
            self.scene = FirstScene(self.player, self.rock)
        elif scene_transition == Scene.NO_SCENE_CHANGE:
            pass
        elif scene_transition == None: 
            pass
        else:
            raise Exception("I have no clue what went wrong")

    def draw(self):
        self.scene.draw()
