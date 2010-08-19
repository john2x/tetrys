'''
Created on Jun 7, 2009

@author: John

'''

import pygame
from constants import *
from Block import Block
class View():
    def __init__(self, game, screen):
        self.background = pygame.Surface(WINDOW_SIZE)
        #self.screen = screen
        self.font_color = (243, 242, 233)
        self.bg_color = (49, 49, 49)
        self.game = game
        self.map = game.map
        self.font = pygame.font.Font('../assets/Monaco.TTF', 9)
        self.canvas = pygame.Surface(WINDOW_SIZE)
        self.block = self.game.next
        self.draw_background()
        self.draw_next_block()
        
    def draw_background(self):
        self.background = pygame.Surface(WINDOW_SIZE)
        self.title = pygame.image.load('../assets/tetryslogo.png').convert_alpha()
        self.game_container = pygame.Surface((72, 160))
        self.block_container = pygame.Surface((32, 32))
        self.score_label = pygame.Surface((32, 12))
        self.level_label = pygame.Surface((32, 12))
        self.score_container = pygame.Surface((32, 12))
        self.level_container = pygame.Surface((32, 12))
        self.top1_container = pygame.Surface((32, 36))
        self.top2_container = pygame.Surface((32, 36))
        self.top3_container = pygame.Surface((32, 36))
        
        self.background.fill(self.bg_color)
        self.score_label = self.font.render('Score: ', False, self.font_color, self.bg_color)
        self.level_label = self.font.render('Level: ', False, self.font_color, self.bg_color)
        self.top_label = self.font.render('Top 3: ', False, self.font_color, self.bg_color)
        
        self.canvas.blit(self.background,(0,0))
        self.canvas.blit(self.title, (46, 24))
        self.canvas.blit(self.game_container, (15, 50))
        self.canvas.blit(self.block_container, (116, 50))
        self.canvas.blit(self.score_label, (110, 80))
        self.canvas.blit(self.level_label, (110, 112))
        self.canvas.blit(self.top_label, (110, 144))
    
    def draw_game(self):
        self.game_container.fill(self.font_color)
        for y in range(self.map.height):
            for x in range(self.map.width):
                if self.map.grid.content[y][x] > 0 \
                and self.map.grid.content[y][x] <= 7:
                    n = self.map.grid.content[y][x]
                    block = pygame.image.load('../assets/' + str(n) + '.gif').convert()
                    self.game_container.blit(block, ((x - 1) * 8, (y - 1) * 8))
        self.canvas.blit(self.game_container, (15, 50))
        
    def draw_next_block(self):
        self.block_container.fill(self.bg_color)
        next_block = Block(self.block)
        for y in range(len(next_block.grid)):
            for x in range(len(next_block.grid[y])):
                if next_block.grid[y][x] > 0:
                    n = next_block.shape
                    block = pygame.image.load('../assets/' + str(n) + '.gif').convert()
                    self.block_container.blit(block, (x * 8, y * 8))
        self.canvas.blit(self.block_container, (116, 50))
        
    def draw_stats(self):
        self.score_container.fill(self.bg_color)
        self.level_container.fill(self.bg_color)
        
        self.score_container = self.font.render(str(self.game.score), False, self.font_color, self.bg_color)
        self.level_container = self.font.render(str(self.game.level), False, self.font_color, self.bg_color)
        
        self.canvas.blit(self.score_container, (116, 92))
        self.canvas.blit(self.level_container, (116, 124))
    
    def draw_scores(self, scores):
        self.top1_container = self.font.render(str(scores[0]), False, self.font_color, self.bg_color)
        self.top2_container = self.font.render(str(scores[1]), False, self.font_color, self.bg_color)
        self.top3_container = self.font.render(str(scores[2]), False, self.font_color, self.bg_color)
        
        self.canvas.blit(self.top1_container, (116, 156))
        self.canvas.blit(self.top2_container, (116, 168))
        self.canvas.blit(self.top3_container, (116, 180))
    
    def draw_game_over(self, place = 0):
        game_over_container = pygame.image.load('../assets/gameover.png').convert_alpha()
        
        self.canvas.blit(game_over_container, (20, 100))
        
        if place > 0:
            place_container = pygame.image.load('../assets/place' + str(place) + '.png').convert_alpha()
            self.canvas.blit(place_container, (25, 152))
    
    def update(self):
        self.draw_game()
        self.draw_stats()
        if self.block != self.game.next:
            self.block = self.game.next
            self.draw_next_block()