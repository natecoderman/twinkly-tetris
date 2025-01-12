class Piece:    
    def __init__(self, color):
        self.b1 = Block((DEFINE_WIDTH // 2), 0, color)
        self.b1.isTop = True
        self.b1.isBottom = True
        self.b1.isLeft = True
        self.b1.isRight = True
        self.rotAxis = [(DEFINE_WIDTH // 2), 0]

    def checkMoveLeft(self):
        for b in self.blockList:
            if (b.isLeft):
                if (not b.checkMoveLeft()):                   
                    return False
        return True

    def checkMoveRight(self):
        for b in self.blockList:
            if (b.isRight):
                if (not b.checkMoveRight()):
                    return False
        return True

    def delCurrent(self):
        for b in self.blockList:
            b.delCurrent()

    def moveRight(self):
        for b in self.blockList:
            b.moveRight()
        self.rotAxis[0] -= 1
    
    def moveLeft(self):
        for b in self.blockList:
            b.moveLeft()
        self.rotAxis[0] += 1
    
    def checkFall(self):
        for b in self.blockList:
            if (b.isBottom):
                if (not b.checkFall()):
                    return False
        return True

    def fall(self):
        for b in self.blockList:
            b.fall()
        self.rotAxis[1] += 1

    def rightRotateCheck(self):
        
        #ignore current piece when checking rotation
        for b in self.blockList:
            matStore[b.xLoc][b.yLoc] = None


        for b in self.blockList:
            #set coords to origin
            testxLoc = b.xLoc
            testxLoc -= self.rotAxis[0]
            testyLoc = b.yLoc
            testyLoc -= self.rotAxis[1]
            
            #rotate clockwise
            temp = testxLoc
            testxLoc = testyLoc
            testyLoc = -temp

            #offset back to real position
            testyLoc += self.rotAxis[1]
            testxLoc += self.rotAxis[0]

            #test if new rotation is valid
            if ((testxLoc < 0) or (testxLoc > (DEFINE_WIDTH - 1))):
                for b in self.blockList:#put blocks back
                    matStore[b.xLoc][b.yLoc] = b
                return False

            if ((testyLoc < 0) or (testyLoc > (DEFINE_HEIGHT - 1))):
                for b in self.blockList:#put blocks back
                    matStore[b.xLoc][b.yLoc] = b
                return False

            if (matStore[testxLoc][testyLoc] != None):
                for b in self.blockList: #put blocks back
                    matStore[b.xLoc][b.yLoc] = b
                return False
        
        for b in self.blockList: #put blocks back
                    matStore[b.xLoc][b.yLoc] = b
        return True

    def rightRotate(self):
        for b in self.blockList:          
            b.xLoc -= self.rotAxis[0]
            b.yLoc -= self.rotAxis[1]

            #rotate clockwise
            temp = b.xLoc
            b.xLoc = b.yLoc
            b.yLoc = -temp
            b.yLoc += self.rotAxis[1]
            b.xLoc += self.rotAxis[0]
            
            #update visual/data
            matTest[b.xLoc][b.yLoc] = b.color
            matStore[b.xLoc][b.yLoc] = b
            
            #check current
            top = False
            right = False
            left = False
            bottom = False

            if (b.isTop):
                b.isTop = False
                right = True
            
            if (b.isRight):
                b.isRight = False
                bottom = True
            
            if (b.isBottom):
                b.isBottom = False
                left = True
            
            if (b.isLeft):
                b.isLeft = False
                top = True

            #update current all at once
            if (right):
                b.isRight = True
            
            if (bottom):
                b.isBottom = True
            
            if (left):
                b.isLeft = True
            
            if (top):
                b.isTop = True
    
    def checkLineHelper(self): #check for lines of blocks
        maxLine = -1 #max since higher yVal = lower line
        for j in range(DEFINE_HEIGHT):
            line = True
            for i in range(DEFINE_WIDTH):
                if (matStore[i][j] == None):
                    line = False
            
            if (line and j > maxLine):
                maxLine = j
        
        return maxLine #returns lowest line
    
    def adjustBlocks(self, fullLine): #delete line of blocks, update any blocks above to move down one

        #delete every block in (bottom) complete line
        for i in range(DEFINE_WIDTH):
            b = matStore[i][fullLine]
            b.delCurrent()
            del b
            matStore[i][fullLine] = None

        #for every block above fullLine (from bottom to top), fall once
        for j in range((fullLine - 1), -1, -1): #should be decrementing ---------
            for k in range(DEFINE_WIDTH):
                if (matStore[k][j] != None):
                    b = matStore[k][j]
                    b.delCurrent()
                    b.fall()
    
    def checkLine(self): #delete current line, move blocks down
        lineCleared = False
        line = self.checkLineHelper()
        while (line != -1):
            self.adjustBlocks(line)
            line = self.checkLineHelper()
            lineCleared = True
        return lineCleared