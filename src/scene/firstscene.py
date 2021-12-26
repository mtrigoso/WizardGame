from typing import List
import pyxel
from game.gameobject import GameObject
from game.tempgameobject import TempGameObject
from manager.collisionmanager import CollisionManager
from move.movementaction import MovementAction
from game.object.rock import Rock

from player import Player
from scene import Scene
from scene.sceneobject import SceneObject

class FirstScene(SceneObject):
    def __init__(self, player: Player, enemies: List[GameObject]):
        super().__init__()
        self.player = player
        self.game_objects: List[GameObject] = [self.player] + enemies
        self.collisionManager = CollisionManager()

    def take_action(self, game_object: GameObject, action: MovementAction, other_game_objects: List[GameObject]): 
        anon_game_object = TempGameObject(action.to_x, action.to_y)
        # for each other game object, if the object in question is coliding with ONE of them, the action may not proceed
        for other_obj in other_game_objects:
            if self.collisionManager.are_colliding(anon_game_object, other_obj):
                return

        game_object.apply_action(action)

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
                self.take_action(game_object, action, other_game_objects)

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
                obj.OBJECT_WIDTH,
            )
