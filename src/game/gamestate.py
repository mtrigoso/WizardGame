from typing import Dict, List
from etc.singleton import Singleton
from scene import Scene
import game

@Singleton
class GameState(object):
    def __init__(self) -> None:
        super().__init__()
        # from game.gameobject import GameObject
        # have to define full name to avoice circular dependency

        # self.objects_in_scene: List[game.gameobject.GameObject] = []
        from game.gameobject import GameObject
        self.current_scene: Scene = None

        self._object_map: Dict[Scene, List[game.gameobject.GameObject]] = {}

    # def objects_in_scene(self, scene: Scene) -> List[game.gameobject.GameObject]:
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
