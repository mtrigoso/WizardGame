import pyxel
from manager.collisionmanager import CollisionManager
from object.rock import Rock

from player import Player
from scene import Scene

class FirstScene:
    def __init__(self, player: Player, rock: Rock):
        self.player = player
        self.rock = rock

        self.collisionManager = CollisionManager()

    def update(self):
        # self.rock.move_random()

        # print(f"Rock: {self.rock.x},{self.rock.y}")

        return self.update_player()

    def update_player(self):
        foo = self.collisionManager.test_collision(self.player, self.rock)

        if foo:
            print(f"colided? {foo}")
        else: 
            print()

        if self.player.y < 0:
            return Scene.SECOND_LEVEL

        if pyxel.btn(pyxel.KEY_LEFT):
            self.player.go_left()

        if pyxel.btn(pyxel.KEY_RIGHT):
            self.player.go_right()

        if pyxel.btn(pyxel.KEY_UP):
            self.player.go_up()

        if pyxel.btn(pyxel.KEY_DOWN):
            self.player.go_down()

    def draw(self):
        pyxel.cls(0)
        # blt(x, y, img, u, v, w, h, [colkey])

        #draw player
        pyxel.blt(
            self.player.x,
            self.player.y,
            0, 
            0,
            0,
            16,
            16,
        )

        #draw rock
        pyxel.blt(
            self.rock.x,
            self.rock.y,
            0, 
            16,
            0,
            16,
            16,
        )
