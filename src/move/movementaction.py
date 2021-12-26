class MovementAction:
    def __init__(self, from_x: int, from_y: int, to_x: int, to_y: int, horiz_dir: int) -> None:
        self.from_x = from_x
        self.from_y = from_y
        self.to_x = to_x
        self.to_y = to_y
        self.horiz_dir = horiz_dir