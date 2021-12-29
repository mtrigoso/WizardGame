from typing import List
from game.action.gameaction import GameAction
from game.gameobject import GameObject
from game.gamestate import GameState
from game.projectile.lightningbolt import LightningBolt
from game.tempgameobject import TempGameObject
from manager.collisionmanager import CollisionManager
from move.movementaction import MovementAction
from battle.projectileaction import ProjectileAction
from scene import Scene


class ActionManager:
    def __init__(self, game_state: GameState) -> None:
        self._collision_manager = CollisionManager()
        self._game_state = game_state

    def take_action(self, game_object: GameObject, action: MovementAction, other_game_objects: List[GameObject]):
        anon_game_object = TempGameObject(
            action.to_x, action.to_y, game_object._object_width, game_object._object_height)
        # for each other game object, if the object in question is coliding with ONE of them, the action may not proceed
        for other_obj in other_game_objects:
            if self._collision_manager.are_colliding(anon_game_object, other_obj):
                # check if the object is killable
                if other_obj.removable():
                    other_obj.set_to_be_removed()
                return

        game_object.apply_action(action)

    def parse_action(self, game_object: GameObject, action: GameAction, scene: Scene):
        other_game_objects = [obj for obj in self._game_state.objects_in_scene(
            scene).copy() if obj != game_object]

        if isinstance(action, MovementAction):
            self.take_action(game_object, action, other_game_objects)
        elif isinstance(action, ProjectileAction):
            # remember that objects are passed by REFERENCE in python
            self._game_state.add_game_object(
                scene, action.build_projectile_object())
