class Background(object):
    def __init__(self) -> None:
        super().__init__()
        self._bitmap_x = 0
        self._bitmap_y = 0
        self._object_width: int = 160
        self._object_height: int = 120
        self._image_num = 1

    