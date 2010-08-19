'''
Created on Jun 5, 2009

@author: John

@todo: bug in settle_block
'''
import pygame
from constants import *
from Grid import Grid

class Map():
    LEFT = -2
    RIGHT = 2
    DOWN = 1
    UP = -1
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.block = None
        
        self.grid = Grid(width, height)
        self.__add_borders(self.grid)
        self.background = Grid(width, height)
        self.grid.copy_content_into(self.background)

    def add_block(self, block, pos = (5, 0), grid = None, settling = False):
        '''places a Block object into a Grid object'''
        if self.block == None:
            print 'adding block', block.shape
        temp = Grid(self.width, self.height)
        if grid == None:
            grid = self.grid
            
        grid.copy_content_into(temp)
        self.block = block
        self.block.pos = pos
        for y in range(pos[1], pos[1] + self.block.size[1]):
            for x in range(pos[0], pos[0] + self.block.size[0]):
                if self.block.grid[y - pos[1]][x - pos[0]] > 0:
                    if settling and temp.content[y][x] == 10:
                        pygame.event.post(pygame.event.Event(GAME_OVER))
                    temp.content[y][x] = self.block.grid[y - pos[1]][x - pos[0]]
        temp.copy_content_into(grid)
        
    def move_current_block(self, direction):
        '''moves Block at direction'''
        ok = 0
        if self.block != None:
            if direction == Map.DOWN:
                #check if move is valid
                ok = self.__check_move(self.block, (self.block.pos[0], self.block.pos[1] + 1))
                if ok == 1:
                    self.background.copy_content_into(self.grid)
                    self.block.pos = (self.block.pos[0], self.block.pos[1] + 1)
                    self.add_block(self.block, self.block.pos, self.grid)
                else:
                    print 'not ok to move (DOWN)'
                    if ok == HIT_BLOCK or ok == HIT_FLOOR:
                        pygame.event.post(pygame.event.Event(ok))
                    
            elif direction == Map.RIGHT:
                ok = self.__check_move(self.block, (self.block.pos[0] + 1, self.block.pos[1]))
                if ok == 1:
                    self.background.copy_content_into(self.grid)
                    self.block.pos = (self.block.pos[0] + 1, self.block.pos[1])
                    self.add_block(self.block, self.block.pos, self.grid)
                else:
                    print 'not ok to move (RIGHT)'
            elif direction == Map.LEFT:
                ok = self.__check_move(self.block, (self.block.pos[0] - 1, self.block.pos[1]))
                if ok == 1:
                    self.background.copy_content_into(self.grid)
                    self.block.pos = (self.block.pos[0] - 1, self.block.pos[1])
                    self.add_block(self.block, self.block.pos, self.grid)
                else:
                    print 'not ok to move (LEFT)'
            elif direction == Map.UP:
                rotation = self.block.rotation
                self.block.rotate()
                ok = self.__check_move(self.block, self.block.pos)
                if ok == 1:
                    print 'rotating'
                    self.background.copy_content_into(self.grid)
                    self.add_block(self.block, self.block.pos, self.grid)
                else:
                    self.block.rotate(rotation)
                    print 'not ok to rotate (ROTATE)'
        else:
            print 'NO BLOCK'
    
    def settle_block(self):
        #@todo: just add the block into background, instead of copying grid into background
        self.add_block(self.block, self.block.pos, self.background, True)
        self.block = None
        #check if a block row is completed
        rows_to_collapse = self.check_grid(self.background)
        
        if len(rows_to_collapse) > 0:
            print rows_to_collapse
            self.collapse_rows(self.background, rows_to_collapse)
            
    def collapse_rows(self, grid, rows):
        j = 0
        for i in rows:
            for y in range(i + j, 3, -1):
                grid.content[y] = grid.get_row(y - 1)
            j += 1
        pygame.event.post(pygame.event.Event(ROW_COLLAPSED))    
    
    def check_grid(self, grid):
        rows = []
        for y in range (len(grid.content) - 1):
            if 0 in grid.content[y] or 10 in grid.content[y]:
                continue
            else:
                rows.append(y)
                pygame.event.post(pygame.event.Event(ROW_COMPLETED))
        rows.reverse()
        return rows
         
    def __check_move(self, block, pos):
        temp = Grid(self.width, self.height)
        self.background.copy_content_into(temp)
        
        area = temp.get_area(block.size, pos)
        if area == None:
            print 'out of bounds'
            return 0
        
        for y in range(len(area)):
            for x in range(len(area[y])):
                if block.grid[y][x] > 0:
                    cell = area[y][x]
                    if cell == 9:
                        return 0
                    elif cell == 8:
                        return HIT_FLOOR
                    elif cell == 10:
                        pass
                    elif cell > 0:
                        return HIT_BLOCK
        return 1
    
    def __add_borders(self, grid):
        grid.content[-1] = [8] * self.width
        grid.content[0] = [10] * self.width
        grid.content[1] = [10] * self.width
        grid.content[2] = [10] * self.width
        for i in grid.content:
            i[0] = 9
            i[-1] = 9
        
    def __repr__(self):
        repr = ''
        for y in range(self.height):
            for x in range(self.width):
                repr += '%x ' % self.grid[y][x]
            repr += '\n'
        return repr
    def __str__(self):
        repr = ''
        for y in range(self.height):
            for x in range(self.width):
                repr += '%x  ' % self.grid[y][x]
            repr += '\n'
        return repr
