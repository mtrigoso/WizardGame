import pyxel
from object.rock import Rock

from player import Player
from manager.scenemanager import SceneManager

class WizardGame:
    def __init__(self):
        pyxel.init(160, 120)
        self.player = Player()
        self.rock = Rock()
        self.scene_manager = SceneManager(self.player, self.rock)
        pyxel.load("assets/wizardgame.pyxres") 
        pyxel.run(self.update, self.draw)

    def update(self):
        self.scene_manager.update()

    def draw(self):
        self.scene_manager.draw()

WizardGame()