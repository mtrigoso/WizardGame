class TileMap(object):
    def __init__(self) -> None:
        super().__init__()
        self._bitmap_x = 0
        self._bitmap_y = 0
        self._object_width: int = 128
        self._object_height: int = 128
        self._tile_num = 0

    