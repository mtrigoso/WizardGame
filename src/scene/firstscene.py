from typing import List
import pyxel
from game.gameobject import GameObject
from game.projectile.lightningbolt import LightningBolt
from game.tempgameobject import TempGameObject
from manager.actionmanager import ActionManager
from manager.collisionmanager import CollisionManager
from move.movementaction import MovementAction
from game.object.rock import Rock

from user.player import Player
from scene import Scene
from scene.sceneobject import SceneObject

class FirstScene(SceneObject):
    def __init__(self, player: Player, enemies: List[GameObject]):
        super().__init__()
        self.player = player
        self.game_objects: List[GameObject] = [self.player] + enemies
        self.action_manager = ActionManager()


    def update(self) -> Scene | None:
        #1: check to see if the player request to move to another scene
        if self.player.y < 0:
            return Scene.SECOND_LEVEL

        for game_object in self.game_objects:
            #2: handle input and construct an action from there
            action = game_object.get_action()

            if action:
                # get all the other game objects to test for collisions against
                other_game_objects = [obj for obj in self.game_objects.copy() if obj != game_object]
                #3: check if the action is valid - if it is, apply that action
                self.action_manager.parse_action(game_object, action, other_game_objects, self.game_objects)

    def draw(self):
        pyxel.cls(0)
        for obj in self.game_objects:
            pyxel.blt(
                obj.get_left_up_corner().x,
                obj.get_left_up_corner().y,
                0,
                obj.bitmap_x(),
                obj.bitmap_y(),
                obj.get_obj_horiz_tilemap_size(),
                obj.get_obj_vert_tilemap_size(),
            )
