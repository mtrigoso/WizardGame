class Player(object):
    x = 0
    y = 80
    speed = 1
    totalScore = 0
    _alive = True

    def moveRight(self):
        self.x = self.x + self.speed

    def moveLeft(self):
        self.x = self.x - self.speed

    def moveUp(self):
        self.y = self.y - self.speed

    def moveDown(self):
        self.y = self.y + self.speed

    def moveRightI(self):
        self.x = self.x + 20

    def moveLeftI(self):
        self.x = self.x - 20

    def moveUpI(self):
        self.y = self.y - 20

    def moveDownI(self):
        self.y = self.y + 20

    def goU(self):
        self.y -= 20

    def goD(self):
        self.y += 20

    def goL(self):
        self.x -= 20

    def goR(self):
        self.x += 20
