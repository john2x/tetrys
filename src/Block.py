from constants import *
class Block():
    
    def __init__(self, shape, pos = (0, 0)):
        self.shape = shape
        self.grid = [[0 for x in range(4)] for y in range(4)]
        self.start = 0
        self.pos = pos
        self.rotation = 0
        self.score = 0
        self.maxRotations = 0
        self.size = (4,4)
        self.__create_shape(self.shape)
    def rotate(self, rotation = None):
        if rotation == None:
            if self.rotation < self.maxRotations:
                self.rotation += 1
            else:
                self.rotation = 0
        else:
            if rotation <= self.maxRotations:
                self.rotation = rotation
                    
        if self.shape == L:
            if self.rotation == 0:
                self.grid = [[L, 0, 0, 0], \
                             [L, 0, 0, 0], \
                             [L, L, 0, 0], \
                             [0, 0, 0, 0]]
                self.size = (2, 3)
            elif self.rotation == 1:
                self.grid = [[L, L, L, 0], \
                             [L, 0, 0, 0], \
                             [0, 0, 0, 0], \
                             [0, 0, 0, 0]]
                self.size = (3, 2)
            elif self.rotation == 2:
                self.grid = [[L, L, 0, 0], \
                             [0, L, 0, 0], \
                             [0, L, 0, 0], \
                             [0, 0, 0, 0]]
                self.size = (2, 3)
            elif self.rotation == 3:
                self.grid = [[0, 0, L, 0], \
                             [L, L, L, 0], \
                             [0, 0, 0, 0], \
                             [0, 0, 0, 0]]
                self.size = (3, 2)
        elif self.shape == J:
            if self.rotation == 0:
                self.grid = [[0, J, 0, 0], \
                             [0, J, 0, 0], \
                             [J, J, 0, 0], \
                             [0, 0, 0, 0]]
                self.size = (2, 3)
            elif self.rotation == 1:
                self.grid = [[J, 0, 0, 0], \
                             [J, J, J, 0], \
                             [0, 0, 0, 0], \
                             [0, 0, 0, 0]]
                self.size = (3, 2)
            elif self.rotation == 2:
                self.grid = [[J, J, 0, 0], \
                             [J, 0, 0, 0], \
                             [J, 0, 0, 0], \
                             [0, 0, 0, 0]]
                self.size = (2, 3)
            elif self.rotation == 3:
                self.grid = [[J, J, J, 0], \
                             [0, 0, J, 0], \
                             [0, 0, 0, 0], \
                             [0, 0, 0, 0]]
                self.size = (3, 2)
        elif self.shape == I:
            if self.rotation == 0:
                self.grid = [[I, I, I, I], \
                             [0, 0, 0, 0], \
                             [0, 0, 0, 0], \
                             [0, 0, 0, 0]]
                self.size = (4, 1)
                self.pos = (self.pos[0] - 1, self.pos[1])
            elif self.rotation == 1:
                self.grid = [[I, 0, 0, 0], \
                             [I, 0, 0, 0], \
                             [I, 0, 0, 0], \
                             [I, 0, 0, 0]]
                self.size = (1, 4)
                self.pos = (self.pos[0] + 1, self.pos[1])
        elif self.shape == Z:
            if self.rotation == 0:
                self.grid = [[Z, Z, 0, 0], \
                             [0, Z, Z, 0], \
                             [0, 0, 0, 0], \
                             [0, 0, 0, 0]]
                self.size = (3, 2)
            elif self.rotation == 1:
                self.grid = [[0, Z, 0, 0], \
                             [Z, Z, 0, 0], \
                             [Z, 0, 0, 0], \
                             [0, 0, 0, 0]]
                self.size = (2, 3)
        elif self.shape == S:
            if self.rotation == 0:
                self.grid = [[0, S, S, 0], \
                             [S, S, 0, 0], \
                             [0, 0, 0, 0], \
                             [0, 0, 0, 0]]
                self.size = (3, 2)
            elif self.rotation == 1:
                self.grid = [[S, 0, 0, 0], \
                             [S, S, 0, 0], \
                             [0, S, 0, 0], \
                             [0, 0, 0, 0]]
                self.size = (2, 3)    
        elif self.shape == T:
            if self.rotation == 0:
                self.grid = [[0, T, 0, 0], \
                             [T, T, T, 0], \
                             [0, 0, 0, 0], \
                             [0, 0, 0, 0]]
                self.size = (3, 2)
            elif self.rotation == 1:
                self.grid = [[T, 0, 0, 0], \
                             [T, T, 0, 0], \
                             [T, 0, 0, 0], \
                             [0, 0, 0, 0]]
                self.size = (2, 3)
            elif self.rotation == 2:
                self.grid = [[T, T, T, 0], \
                             [0, T, 0, 0], \
                             [0, 0, 0, 0], \
                             [0, 0, 0, 0]]
                self.size = (3, 2)
            elif self.rotation == 3:
                self.grid = [[0, T, 0, 0], \
                             [T, T, 0, 0], \
                             [0, T, 0, 0], \
                             [0, 0, 0, 0]]
                self.size = (2, 3)
    def copy(self):
        block =  Block(self.shape, self.pos)
        block.rotate(self.rotation)
        return block
    
    def __create_shape(self, shape):
        if self.shape == L:
            self.grid = [[L, 0, 0, 0], \
                         [L, 0, 0, 0], \
                         [L, L, 0, 0], \
                         [0, 0, 0, 0]]
            self.size = (2, 3)
            self.maxRotations = 3
            self.score = 7
        elif self.shape == J:
            self.grid = [[0, J, 0, 0], \
                         [0, J, 0, 0], \
                         [J, J, 0, 0], \
                         [0, 0, 0, 0]]
            self.size = (2, 3)
            self.maxRotations = 3
            self.score = 7
        elif self.shape == O:
            self.grid = [[O, O, 0, 0], \
                         [O, O, 0, 0], \
                         [0, 0, 0, 0], \
                         [0, 0, 0, 0]]
            self.size = (2, 2)
            self.maxRotations = 0
            self.score = 5
        elif self.shape == I:
            self.grid = [[I, I, I, I], \
                         [0, 0, 0, 0], \
                         [0, 0, 0, 0], \
                         [0, 0, 0, 0]]
            self.size = (4, 1)
            self.maxRotations = 1
            self.score = 5
        elif self.shape == Z:
            self.grid = [[Z, Z, 0, 0], \
                         [0, Z, Z, 0], \
                         [0, 0, 0, 0], \
                         [0, 0, 0, 0]]
            self.size = (3, 2)
            self.maxRotations = 1
            self.score = 9
        elif self.shape == S:
            self.grid = [[0, S, S, 0], \
                         [S, S, 0, 0], \
                         [0, 0, 0, 0], \
                         [0, 0, 0, 0]]
            self.size = (3, 2)
            self.maxRotations = 1
            self.score = 9
        elif self.shape == T:
            self.grid = [[0, T, 0, 0], \
                         [T, T, T, 0], \
                         [0, 0, 0, 0], \
                         [0, 0, 0, 0]]
            self.size = (3, 2)
            self.maxRotations = 3
            self.score = 10
        