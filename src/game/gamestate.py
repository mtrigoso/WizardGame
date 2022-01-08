from typing import Dict, List, Tuple
from game import gameobject
from game.gameobject import GameObject
from scene import Scene
import scene
import game

class GameState(object):
    INITIALIZED = False
    SINGLE_INSTANCE = None
    def __init__(self) -> None:
        if GameState.INITIALIZED:
            raise TypeError("You may not init the game state more than once! Call .instance() if you want the singleton instance")

        GameState.INITIALIZED = True
        GameState.SINGLE_INSTANCE = self

        self.current_scene: Scene = None
        self._object_map: Dict[Scene, List[GameObject]] = {}
        self._to_be_killed: List[GameObject] = []
        self.scene_settings: Dict[Scene, Dict[str, str]] = {} 

        self.saved_state = {"player_y": []};

    def get_first_obj(self, scene: Scene, obj_type: type) -> GameObject:
        return [obj for obj in self._object_map[scene] if type(obj) == obj_type].pop()

    def objects_in_scene(self, scene: Scene) -> List[GameObject]:
        return self._object_map[scene]

    def set_objects_in_scene(self, scene: Scene, objects: List[GameObject]):
        self._object_map[scene] = objects

    def add_game_object(self, scene: Scene, object: GameObject):
        self._object_map[scene].append(object)

    def set_to_be_killed(self, object: GameObject):
        self._to_be_killed.append(object)

    def remove_game_object(self, scene: Scene, object: GameObject):
        self._object_map[scene].remove(object)

    def objects_for_removal(self, scene: Scene) -> List[GameObject]:
        # in theory we could + another list here (say of objects like walls that were broken)
        return [obj for obj in self.objects_in_scene(scene) if obj.to_be_removed()]

    def remove_all_removed_objects(self, scene: Scene):
        for obj in self.objects_for_removal(scene):
            self.remove_game_object(scene, obj)

    def move_objs_between_scenes(self, objs_in_scene1: List[GameObject], scene1: Scene, scene2: Scene):
        for obj in objs_in_scene1:
            self.remove_game_object(scene1, obj)
            self.add_game_object(scene2, obj)

    @staticmethod
    def instance():
        """
        Returns the singleton instance. Upon its first call, it creates a
        new instance of the decorated class and calls its `__init__` method.
        On all subsequent calls, the already created instance is returned.
        """
        if GameState.INITIALIZED:
            return GameState.SINGLE_INSTANCE
        else:
            return GameState()

    