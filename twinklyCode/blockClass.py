class Block:
    #used for pieces moving left/right/down
    isTop = False #used for rotations
    isBottom = False
    isLeft = False
    isRight = False

    def __init__(self, xLoc, yLoc, color):
        self.xLoc = xLoc
        self.yLoc = yLoc
        self.color = color
        matTest[self.xLoc][self.yLoc] = self.color
        if (matStore[self.xLoc][self.yLoc] != None):
            print(f"game end! score: {score}")
            gameEnd(self)
            sys.exit()
        else:
            matStore[self.xLoc][self.yLoc] = self
    
    def __str__(self):
        return f"color {self.color} at ({self.xLoc}, {self.yLoc})"

    def checkMoveLeft(self):
        if (self.xLoc < (DEFINE_WIDTH - 1)):
            return (matStore[self.xLoc + 1][self.yLoc] == None)
        else:
            return False

    def moveLeft(self):
        self.xLoc += 1
        matTest[self.xLoc][self.yLoc] = self.color
        matStore[self.xLoc][self.yLoc] = self
    
    def checkMoveRight(self):
        return ((self.xLoc > 0) and (matStore[self.xLoc - 1][self.yLoc] == None))
    
    def delCurrent(self):
        matTest[self.xLoc][self.yLoc] = (0, 0, 0)
        matStore[self.xLoc][self.yLoc] = None

    def moveRight(self):
        self.xLoc -= 1
        matTest[self.xLoc][self.yLoc] = self.color
        matStore[self.xLoc][self.yLoc] = self

    def checkFall(self):
        if (self.yLoc >= (DEFINE_HEIGHT - 1)):
            return False
        elif (matStore[self.xLoc][self.yLoc + 1] != None):
            return False
        else:
            return True
    
    def fall(self):
        self.yLoc += 1
        matTest[self.xLoc][self.yLoc] = self.color
        matStore[self.xLoc][self.yLoc] = self
