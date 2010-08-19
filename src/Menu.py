'''
Created on Jun 7, 2009

@author: John

@todo: disable continue if no game is playing
'''
import pygame
import sys
from constants import *
class Menu():
    def __init__(self, screen):
        self.selected = 1
        #self.screen = screen
        self.continue_enabled = False
        self.canvas = pygame.Surface(WINDOW_SIZE)
        self.draw_background()
        self.draw_menu()
        
    def draw_background(self):
        self.background = pygame.image.load('../assets/menubg.png').convert()
        self.title = pygame.image.load('../assets/tetryslogo.png').convert_alpha()
        self.canvas.blit(self.background,(0,0))
        self.canvas.blit(self.title, (46, 24))
        
    def draw_menu(self):
        self.continue_btn = pygame.image.load('../assets/continue-disabled.gif').convert()
        self.newgame_btn = pygame.image.load('../assets/newgame-over.gif').convert()
        self.exit_btn = pygame.image.load('../assets/exit-up.gif').convert()
        self.canvas.blit(self.continue_btn, (53, 100))
        self.canvas.blit(self.newgame_btn, (48, 120))
        self.canvas.blit(self.exit_btn, (66, 140))
    
    def disable_continue(self):
        self.continue_enabled = False
        
        self.selected = 1
    def enable_continue(self):
        self.continue_enabled = True
    
    def update(self):
        if self.selected == 0:
            #load up image of newgame
            self.continue_btn = pygame.image.load('../assets/continue-over.gif').convert()
            self.newgame_btn = pygame.image.load('../assets/newgame-up.gif').convert()
            self.exit_btn = pygame.image.load('../assets/exit-up.gif').convert()
            self.canvas.blit(self.continue_btn, (53, 100))
            self.canvas.blit(self.newgame_btn, (48, 120))
            self.canvas.blit(self.exit_btn, (66, 140))
        elif self.selected == 1:
            #load up image of continue
            if self.continue_enabled:
                self.continue_btn = pygame.image.load('../assets/continue-up.gif').convert()
            else:
                self.continue_btn = pygame.image.load('../assets/continue-disabled.gif').convert()
            self.newgame_btn = pygame.image.load('../assets/newgame-over.gif').convert()
            self.exit_btn = pygame.image.load('../assets/exit-up.gif').convert()
            self.canvas.blit(self.continue_btn, (53, 100))
            self.canvas.blit(self.newgame_btn, (48, 120))
            self.canvas.blit(self.exit_btn, (66, 140))
        elif self.selected == 2:
            #load up image of exit
            if self.continue_enabled:
                self.continue_btn = pygame.image.load('../assets/continue-up.gif').convert()
            else:
                self.continue_btn = pygame.image.load('../assets/continue-disabled.gif').convert()
            self.newgame_btn = pygame.image.load('../assets/newgame-up.gif').convert()
            self.exit_btn = pygame.image.load('../assets/exit-over.gif').convert()
            self.canvas.blit(self.continue_btn, (53, 100))
            self.canvas.blit(self.newgame_btn, (48, 120))
            self.canvas.blit(self.exit_btn, (66, 140))
    def execute(self):
        if self.selected == 1:
            #start new game
            pygame.event.post(pygame.event.Event(NEW_GAME))
        elif self.selected == 0:
            pygame.event.post(pygame.event.Event(CONTINUE))
        elif self.selected == 2:
            sys.exit()
        print self.selected
            
    def run(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if self.selected > 0:
                    if self.selected == 1 and not self.continue_enabled:
                        return
                    self.selected -= 1
            elif event.key == pygame.K_DOWN:
                if self.selected < 2:
                    self.selected += 1
            elif event.key == pygame.K_RETURN:
                self.execute()
                    