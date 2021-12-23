from typing import List
import pyxel
from game.gameobject import GameObject
from game.tempgameobject import TempGameObject
from manager.collisionmanager import CollisionManager
from move.action import Action
from object.rock import Rock

from player import Player
from scene import Scene

class FirstScene:
    def __init__(self, player: Player, rock: Rock):
        self.player = player
        self.rock = rock
        self.game_objects: List[GameObject] = [self.player, self.rock]
        self.collisionManager = CollisionManager()

    def take_action(self, game_object: GameObject, action: Action, other_game_objects: List[GameObject]): 
        anon_game_object = TempGameObject(action.to_x, action.to_y)
        # for each other game object, if the object in question is coliding with ONE of them, the action may not proceed
        for other_obj in other_game_objects:
            col = self.collisionManager.are_colliding(anon_game_object, other_obj)
            if col:
                return

        game_object.apply_action(action)

    def update(self):
        #1: check to see if the player request to move to another scene
        if self.player.y < 0:
            return Scene.SECOND_LEVEL

        for go in self.game_objects:
            #2: handle input and construct an action from there
            action = go.get_action()
            if action:
                # get all the other game objects to test for collisions against
                other_game_objects = [obj for obj in self.game_objects.copy() if obj != go]
                #3: check if the action is valid - if it is, apply that action
                self.take_action(go, action, other_game_objects)

    def draw(self):
        pyxel.cls(0)

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
