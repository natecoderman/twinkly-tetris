

class Frame:
    def __init__(self, matrix):
        self.matrix = matrix
    def read(self):
        if (DEFINE_PANELS == 2):
            # width = 8, height = 16
            return self.read8x16()
        
        elif (DEFINE_ROTATE == 0):
            # width = 8, height = 8
            return self.read8x8()
        
        elif (DEFINE_ROTATE == 1):
            # width = 8, height = 8
            return self.read8x8Rotate1()
        
        elif (DEFINE_ROTATE == 2):
            # width = 8, height = 8
            return self.read8x8Rotate2()
        
        elif (DEFINE_ROTATE == 3):
            # width = 8, height = 8
            return self.read8x8Rotate3()

        else:
            print("invalid height/width values")
            exit(1)
    
    def read8x8(self): #8 tall, 8 wide
        # Start from the bottom-right corner and snake up/down
        bin_string = b""
        
        for i in range(8):
            if i % 2 == 0:  # Even rows: traverse from right to left
                for j in range(7, -1, -1):
                    r, g, b = self.matrix[i][j]
                    bin_string += bytes([r, g, b])
            else:  # Odd rows: traverse from left to right
                for j in range(8):
                    r, g, b = self.matrix[i][j]
                    bin_string += bytes([r, g, b])
        
        return bin_string 
    
    def read8x8Rotate1(self): #rotate 90
        # Start from the bottom-right corner and snake up/down
        bin_string = b""
        
        for i in range(7, -1, -1):
            if i % 2 == 0:  # Even rows: traverse from right to left
                for j in range(8):
                    r, g, b = self.matrix[j][i]
                    bin_string += bytes([r, g, b])
            else:  # Odd rows: traverse from left to right
                for j in range(7, -1, -1):
                    r, g, b = self.matrix[j][i]
                    bin_string += bytes([r, g, b])
        
        return bin_string
    
    def read8x8Rotate2(self): #rotate 90
        # Start from the bottom-right corner and snake up/down
        bin_string = b""
        
        for i in range(8):
            if i % 2 == 0:  # Even rows: traverse from right to left
                for j in range(8):
                    r, g, b = self.matrix[j][i]
                    bin_string += bytes([r, g, b])
            else:  # Odd rows: traverse from left to right
                for j in range(7, -1, -1):
                    r, g, b = self.matrix[j][i]
                    bin_string += bytes([r, g, b])
        
        return bin_string
    
    def read8x8Rotate3(self): #8 tall, 8 wide
        # Start from the bottom-right corner and snake up/down
        bin_string = b""
        
        for i in range(7, -1, -1):
            if i % 2 == 0:  # Even rows: traverse from right to left
                for j in range(7, -1, -1):
                    r, g, b = self.matrix[i][j]
                    bin_string += bytes([r, g, b])
            else:  # Odd rows: traverse from left to right
                for j in range(8):
                    r, g, b = self.matrix[i][j]
                    bin_string += bytes([r, g, b])
        
        return bin_string

    def read8x16(self):
        #still snakes, but bottom panel is from left/right, top panel is down/up
        
        bin_string = b""
        
        #for the bottom panel
        for i in range(15, 7, -1): #traverse colomns
            if i % 2 == 0:  # even colomns: traverse from bottom to top
                for j in range(8): #traverse rows
                    r, g, b = self.matrix[j][i]
                    bin_string += bytes([r, g, b])
            else:  # Odd colomns: traverse from top to bottom
                for j in range(7, -1, -1):
                    r, g, b = self.matrix[j][i]
                    bin_string += bytes([r, g, b])
        
        #for the top panel
        for i in range(7, -1, -1): #traverse rows
            if i % 2 == 0:  
                for j in range(7, -1, -1): #even rows, traverse coloms from left to right
                    r, g, b = self.matrix[i][j]
                    bin_string += bytes([r, g, b])
            else:  
                for j in range(8): # Odd rows: colomn traverse from right to left
                    r, g, b = self.matrix[i][j]
                    bin_string += bytes([r, g, b])


        return bin_string

