from game.action.gameaction import GameAction
from move.movevector import MoveVector


class MovementAction(GameAction):
    def __init__(self, from_x: int, from_y: int, to_x: int, to_y: int, vector: MoveVector) -> None:
        self.from_x = from_x
        self.from_y = from_y
        self.to_x = to_x
        self.to_y = to_y
        self.vector = vector