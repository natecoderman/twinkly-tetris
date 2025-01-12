class Opiece(Piece):
    #  INITIAL SHAPE
    #  b1  b2
    #  b3  b4

    def __init__(self, color):
        self.b1 = Block((DEFINE_WIDTH // 2), 0, color)
        self.b2 = Block(((DEFINE_WIDTH // 2) - 1), 0, color)
        self.b3 = Block((DEFINE_WIDTH // 2), 1, color)
        self.b4 = Block(((DEFINE_WIDTH // 2) - 1), 1, color)
        self.blockList = [self.b1, self.b2, self.b3, self.b4]
        self.rotAxis = [(DEFINE_WIDTH // 2), 0]

        self.b1.isTop = True
        self.b2.isTop = True
        self.b3.isBottom = True
        self.b4.isBottom = True
        self.b1.isLeft = True
        self.b3.isLeft = True
        self.b2.isRight = True
        self.b4.isRight = True
        

class Tpiece(Piece):
    #  INITIAL SHAPE
    #      b1
    #  b2  b3  b4
    
    def __init__(self, color):
        self.b1 = Block((DEFINE_WIDTH // 2), 0, color)
        self.b2 = Block(((DEFINE_WIDTH // 2) + 1), 1, color)
        self.b3 = Block((DEFINE_WIDTH // 2), 1, color)
        self.b4 = Block(((DEFINE_WIDTH // 2) - 1), 1, color)
        self.blockList = [self.b1, self.b2, self.b3, self.b4]
        self.rotAxis = [(DEFINE_WIDTH // 2), 1]

        self.b1.isTop = True
        self.b1.isLeft = True
        self.b1.isRight = True
        self.b2.isLeft = True
        self.b2.isBottom = True
        self.b3.isBottom = True
        self.b4.isBottom = True
        self.b4.isRight = True

class Ipiece(Piece):
    #  INITIAL SHAPE
    #  b1  b2  b3  b4

    def __init__(self, color):
        self.b1 = Block(((DEFINE_WIDTH // 2) + 1), 0, color)
        self.b2 = Block((DEFINE_WIDTH // 2), 0, color)
        self.b3 = Block(((DEFINE_WIDTH // 2) - 1), 0, color)
        self.b4 = Block(((DEFINE_WIDTH // 2) - 2), 0, color)
        self.blockList = [self.b1, self.b2, self.b3, self.b4]
        self.rotAxis = [(DEFINE_WIDTH // 2), 0]

        self.b1.isTop = True
        self.b1.isLeft = True
        self.b1.isBottom = True
        self.b2.isTop = True
        self.b2.isBottom = True
        self.b3.isTop = True
        self.b3.isBottom = True
        self.b4.isTop = True
        self.b4.isBottom = True
        self.b4.isRight = True

class Lpiece(Piece):
    #  INITIAL SHAPE
    #           b4
    #   b1  b2  b3  

    def __init__(self, color):
        self.b1 = Block(((DEFINE_WIDTH // 2) + 1), 1, color)
        self.b2 = Block((DEFINE_WIDTH // 2), 1, color)
        self.b3 = Block(((DEFINE_WIDTH // 2) - 1), 1, color)
        self.b4 = Block(((DEFINE_WIDTH // 2) - 1), 0, color)
        self.blockList = [self.b1, self.b2, self.b3, self.b4]
        self.rotAxis = [(DEFINE_WIDTH // 2), 0]

        self.b1.isBottom = True
        self.b1.isTop = True
        self.b1.isLeft = True
        self.b2.isBottom = True
        self.b2.isTop = True
        self.b3.isBottom = True
        self.b3.isRight = True
        self.b4.isTop = True
        self.b4.isRight= True
        self.b4.isLeft = True

class Jpiece(Piece):
    #  INITIAL SHAPE
    #   b4        
    #   b1  b2  b3  

    def __init__(self, color):
        self.b1 = Block(((DEFINE_WIDTH // 2) + 1), 1, color)
        self.b2 = Block((DEFINE_WIDTH // 2), 1, color)
        self.b3 = Block(((DEFINE_WIDTH // 2) - 1), 1, color)
        self.b4 = Block(((DEFINE_WIDTH // 2) + 1), 0, color)
        self.blockList = [self.b1, self.b2, self.b3, self.b4]
        self.rotAxis = [(DEFINE_WIDTH // 2), 0]

        self.b1.isBottom = True
        self.b1.isLeft = True
        self.b2.isBottom = True
        self.b2.isTop = True
        self.b3.isBottom = True
        self.b3.isTop = True
        self.b3.isRight = True
        self.b4.isTop = True
        self.b4.isRight = True
        self.b4.isLeft = True

class Zpiece(Piece):
    #  INITIAL SHAPE
    #  b1  b2
    #      b3  b4 

    def __init__(self, color):
        self.b1 = Block(((DEFINE_WIDTH // 2) + 1), 0, color)
        self.b2 = Block((DEFINE_WIDTH // 2), 0, color)
        self.b3 = Block((DEFINE_WIDTH // 2), 1, color)
        self.b4 = Block(((DEFINE_WIDTH // 2) - 1), 1, color)
        self.blockList = [self.b1, self.b2, self.b3, self.b4]
        self.rotAxis = [(DEFINE_WIDTH // 2), 1]

        self.b1.isTop = True
        self.b1.isLeft = True
        self.b1.isBottom = True
        self.b2.isTop = True
        self.b2.isRight = True
        self.b3.isLeft = True
        self.b3.isBottom = True
        self.b4.isTop = True
        self.b4.isBottom = True
        self.b4.isRight = True

class Spiece(Piece):
    #  INITIAL SHAPE
    #      b1  b2
    #  b3  b4

    def __init__(self, color):
        self.b1 = Block((DEFINE_WIDTH // 2), 0, color)
        self.b2 = Block(((DEFINE_WIDTH // 2) - 1), 0, color)
        self.b3 = Block(((DEFINE_WIDTH // 2) + 1), 1, color)
        self.b4 = Block((DEFINE_WIDTH // 2), 1, color)
        self.blockList = [self.b1, self.b2, self.b3, self.b4]
        self.rotAxis = [(DEFINE_WIDTH // 2), 1]

        self.b1.isTop = True
        self.b1.isLeft = True
        self.b2.isTop = True
        self.b2.isRight = True
        self.b2.isBottom = True
        self.b3.isTop = True
        self.b3.isLeft = True
        self.b3.isBottom = True
        self.b4.isBottom = True
        self.b4.isRight = True