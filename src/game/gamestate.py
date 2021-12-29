from typing import Dict, List
from etc.singleton import Singleton
from scene import Scene
import scene

"""
you'll notice that there isn't any strong typing in this class, that's because in order to use the types, 
    the module need to be initialized. However, each module depends on one another, causing a circular dependency
    : (
    I hope we can find a way around this
"""


@Singleton
class GameState(object):
    def __init__(self) -> None:
        from game.gameobject import GameObject
        self.current_scene: Scene = None
        self._object_map: Dict[Scene, List[GameObject]] = {}
        self._to_be_killed: List[GameObject] = []

    # def objects_in_scene_temp(self, scene: Scene) -> List[game.gameobject.GameObject]:
    #     return self._object_map[scene]

    # def set_objects_in_scene(self, scene: Scene, objects: List[game.gameobject.GameObject]):
    #     self._object_map[scene] = object

    # def add_game_object(self, scene: Scene, object: game.gameobject.GameObject):
    #     self._object_map[scene].append(object)

    def objects_in_scene(self, scene: Scene):
        return self._object_map[scene]

    def set_objects_in_scene(self, scene: Scene, objects: List):
        self._object_map[scene] = objects

    def add_game_object(self, scene: Scene, object):
        self._object_map[scene].append(object)

    def set_to_be_killed(self, object):
        self._to_be_killed.append(object)

    def remove_game_object(self, scene: Scene, object):
        self._object_map[scene].remove(object)
        # self._to_be_killed.remove(object)

    def objects_for_removal(self, scene: Scene):
        # in theory we could + another list here (say of objects like walls that were broken)
        return [obj for obj in self.objects_in_scene(scene) if obj.to_be_removed()]
    
    def remove_all_removed_objects(self, scene: Scene):
        for obj in self.objects_for_removal(scene):
            self.remove_game_object(scene, obj)

