import pyxel
from game.enemy.troll import Troll
from game.object.rock import Rock
from game.projectile.lightningbolt import LightningBolt

from user.player import Player
from manager.scenemanager import SceneManager

class WizardGame:
    def __init__(self):
        pyxel.init(160, 120)
        self.player = Player()
        self.scene_manager = SceneManager(self.player, 
            [
                Rock(), 
                Troll(75, 75), 
                Troll(100, 100),
                LightningBolt(20, 50),
            ]
        )
        pyxel.load("assets/wizardgame.pyxres") 
        pyxel.run(self.update, self.draw)

    def update(self):
        self.scene_manager.update()

    def draw(self):
        self.scene_manager.draw()

WizardGame()