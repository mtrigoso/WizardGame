from typing import Dict, List
from etc.singleton import Singleton
from scene import Scene

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
