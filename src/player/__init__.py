class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.player_vy = 0

    def go_left(self):
        self.x = self.x - 1

    def go_right(self):
        self.x = self.x + 1

    def go_up(self):
        self.y = self.y - 1

    def go_down(self):
        self.y = self.y + 1