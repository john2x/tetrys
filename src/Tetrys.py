
#@todo: add sound
#@todo: change next block algorithm

import pygame
import sys
from random import randint
from Map import Map
from Block import Block
from View import View
from constants import *
################################################################
class Tetrys():
    def __init__(self, size):
        self.size = size
        self.falling = False
        self.playing = False
        self.speed = 1000
        self.falling_speed = 20
        self.normal_speed = self.speed
        self.score = 0
        self.level = 1
        self.combo = 1
        self.next = randint(1, 7)
        self.next_block = Block(self.next)
        self.collapsing = False
        
        self.clock = pygame.time.Clock()
        self.map = Map(self.size[0], self.size[1])
        self.block = None
        
        
    def new_game(self):
        self.next = randint(1, 7)
        self.map = Map(self.size[0], self.size[1])
        self.block = Block(self.next)

        self.playing = True
        self.collapsing = False
        self.falling = False

        self.speed = 1000
        self.normal_speed = self.speed
        self.combo = 1
        self.score = 0
        self.level = 1
        self.next = randint(1, 7) 
        
        self.map.add_block(self.block, (self.size[0] / 2, 0))
        pygame.time.set_timer(TIMER, self.speed)
    
    def update(self):
        if (self.score / 500) >= self.level:
            if self.normal_speed > 100:
                self.normal_speed -= 100
                self.speed = self.normal_speed
                self.level += 1
                pygame.time.set_timer(TIMER, self.speed)
                print '>>', self.normal_speed
            
    def unpause(self):
        self.playing = True
    def pause(self):
        self.playing = False
        
    def run(self, event):
        if self.playing:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and not self.falling:
                    self.map.move_current_block(Map.DOWN)
                elif event.key == pygame.K_RIGHT and not self.falling:
                    self.map.move_current_block(Map.RIGHT)
                elif event.key == pygame.K_LEFT and not self.falling:
                    self.map.move_current_block(Map.LEFT)
                elif event.key == pygame.K_UP and not self.falling:
                    self.map.move_current_block(Map.UP)
                elif event.key == pygame.K_SPACE or event.key == pygame.K_RETURN:
                    self.speed = self.falling_speed
                    pygame.time.set_timer(TIMER, self.speed)
                    self.falling = True
            elif event.type == HIT_BLOCK:
                print 'HIT BLOCK!'
                self.score += self.block.score
                self.speed = self.normal_speed
                pygame.time.set_timer(TIMER, self.speed)
                self.map.settle_block()
                self.falling = False            
                pygame.event.post(pygame.event.Event(BLOCK_REMOVED))
            elif event.type == HIT_FLOOR:
                print 'HIT FLOOR!'
                self.score += self.block.score
                self.speed = self.normal_speed
                pygame.time.set_timer(TIMER, self.speed)
                self.map.settle_block()
                self.falling = False
                pygame.event.post(pygame.event.Event(BLOCK_REMOVED))
            elif event.type == ROW_COMPLETED:
                print 'ROW COMPLETED!'
                self.collapsing = True
                self.score += 100 * self.combo
                self.combo += 1
            elif event.type == ROW_COLLAPSED:
                print 'ROW COLLAPSED!'
                self.collapsing = False
                self.combo = 1
            elif event.type == BLOCK_REMOVED:
                self.map.add_block(Block(self.next))
                self.next = randint(1, 7)
            elif event.type == TIMER:
                if not self.collapsing:
                    self.map.move_current_block(Map.DOWN)
            elif event.type == GAME_OVER:
                print 'GAME OVER!'
                self.playing == False
###########################################################################
