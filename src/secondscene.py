import pyxel

from player import Player
from scene import Scene

class SecondScene:
    def __init__(self, player: Player):
        # pyxel.init(160, 120)
        self.player = player
        self.player.y = 120
        # pyxel.load(self.player.asset)
        # pyxel.run(self.update, self.draw)

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
            16 if self.player.player_vy > 0 else 0,
            0,
            16,
            16,
            12,
        )
