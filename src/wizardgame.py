import pyxel

from player import Player
from scene_manager import SceneManager

class WizardGame:
    def __init__(self):
        pyxel.init(160, 120)
        self.player = Player("assets/whatever.pyxres")
        self.scene_manager = SceneManager(self.player)
        pyxel.load(self.player.asset) 
        pyxel.run(self.update, self.draw)

    def update(self):
        print(f"{self.player.x},{self.player.y}")
        self.scene_manager.update()


    def draw(self):
        self.scene_manager.draw()

        # pyxel.cls(0)
        # pyxel.blt(
        #     self.player.x,
        #     self.player.y,
        #     0, #index of the resource
        #     16 if self.player.player_vy > 0 else 0,
        #     0,
        #     16,
        #     16,
        #     12,
        # )

WizardGame()