import pyxel

from player import Player
from scene import Scene

class SecondScene:
    def __init__(self, player: Player):
        self.player = player
        self.player.y = 120

    def update(self):
        print(f"{self.player.x},{self.player.y}")
        return self.update_player()

    def update_player(self):
        if self.player.y > 120:
            return Scene.FIRST_LEVEL

        if pyxel.btn(pyxel.KEY_LEFT):
            self.player.go_left()

        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player.go_right()

        if pyxel.btn(pyxel.KEY_UP):
            self.player.go_up()

        if pyxel.btn(pyxel.KEY_DOWN):
            self.player.go_down()

    def draw(self):
        pyxel.cls(1)
        pyxel.blt(
            self.player.x,
            self.player.y,
            0, #index of the resource
            0,
            0,
            16,
            16,
            12,
        )
