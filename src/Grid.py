'''
Created on Jun 5, 2009

@author: John
'''
class Grid():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.content = [[0 for x in range(width)] for y in range(height)]
        
    def get_row(self, row):
        return self.content[row][:]
    
    def copy_content_into(self, target):
        for y in range(len(self.content)):
            for x in range(len(self.content[y])):
                target.content[y][x] = self.content[y][x]
    
    def get_area(self, size, pos):
        area = [[0 for x in range(size[0])] for y in range(size[1])]
        for y in range(pos[1], pos[1] + size[1]):
            for x in range(pos[0], pos[0] + size[0]):
                try:
                    area[y - pos[1]][x - pos[0]] = self.content[y][x]
                except IndexError:
                    return None
        return area
    
    def __repr__(self):
        repr = ''
        for y in range(self.height):
            for x in range(self.width):
                repr += '%x ' % self.content[y][x]
            repr += '\n'
        return repr
    def __str__(self):
        repr = ''
        for y in range(self.height):
            for x in range(self.width):
                repr += '%x  ' % self.content[y][x]
            repr += '\n'
        return repr
