from typing import overload

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
