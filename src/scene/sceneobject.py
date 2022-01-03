from typing import List, Tuple, overload
from game.gameobject import GameObject

from scene import Scene


class SceneObject(object):
    def __init__(self) -> None:
        super().__init__()

    @overload
    def update(self) -> Scene | None:
        pass

    @overload
    def draw(self):
        pass
