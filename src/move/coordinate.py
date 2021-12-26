class Coordinate():
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        pass

    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Coordinate):
            return self.x == __o.x and self.y == __o.y
        raise Exception(f"You tried to comapre a coordinate and something else! Other type: {type(__o)}")


        


    