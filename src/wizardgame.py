import pyxel

class App:
    def __init__(self):
        pyxel.init(160, 120)
        self.x = 0
        self.player_vy = 0
        pyxel.load("assets/player.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        self.x = (self.x + 1) % pyxel.width

    def draw(self):
        pyxel.cls(0)
        # pyxel.rect(self.x, 0, 8, 8, 9)
        pyxel.blt(
            self.x,
            0,
            0,
            16 if self.player_vy > 0 else 0,
            0,
            16,
            16,
            12,
        )

App()