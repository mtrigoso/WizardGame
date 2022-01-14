from typing import List, Tuple, overload
from game.gameobject import GameObject

from scene import Scene


class SceneObject(object):
    SCENE_TYPE: Scene
    def __init__(self) -> None:
        super().__init__()

    def update(self) -> Scene | None:
        pass

    def draw(self):
        pass
