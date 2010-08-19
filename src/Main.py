'''
Created on Jun 7, 2009

@author: John
'''

# @todo: global variables not changed in functions

import pygame

import sys
from constants import *
from Menu import Menu
from View import View
from Tetrys import Tetrys

scores_file = None
top_scores = [0, 0, 0]
screen = pygame.display.set_mode(WINDOW_SIZE)
state = 'menu'
already_playing = False
saved = False
place = 0

clock = pygame.time.Clock()

def read_scores():
    try:
        scores_file = open('../assets/top_scores.txt', 'r')
        i = 0
        for line in scores_file:
            top_scores[i] = int(line)
            i += 1
            
    except IOError:
        print 'FILE NOT FOUND'
    
def add_score(score):
    top_scores.sort(reverse=True)
    
    beaten = False
    
    for i in range(len(top_scores)):
        if score > top_scores[i]:
            #remove smallest score
            top_scores[len(top_scores) - 1] = score
            beaten = True
            saved = True
            top_scores.sort(reverse=True)
            break
        
    if beaten:
        try:
            scores_file = open('../assets/top_scores.txt', 'w')
            for i in top_scores:
                scores_file.write(str(i) + '\n')
            saved = True
            return top_scores.index(score) + 1
        except IOError:
            print 'FILE NOT FOUND'
    return 0

def create_menu():
    return Menu(screen)
    
def create_view(map):
    return View(map, screen)

def create_game():
    return Tetrys((11, 22))
    
if __name__ == '__main__':
    pygame.init()
    read_scores()
    print top_scores
    
    menu = create_menu()
    game = create_game()
    view = create_view(game)
    menu.disable_continue()
    
    
    while 1:
        for event in pygame.event.get():
            if state == 'menu':
                menu.run(event)
                menu.update()
                
            elif state == 'game':
                if not already_playing:
                    game.new_game()
                    view = create_view(game)
                    already_playing = True
                    saved = False
                    menu.enable_continue()
                game.unpause()
                game.run(event)
                game.update()
                view.draw_scores(top_scores)
                view.update()
                
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == NEW_GAME:
                state = 'game'
                already_playing = False
            elif event.type == CONTINUE:
                state = 'game'
            elif event.type == GAME_OVER:
                state = 'game over'
                already_playing = False
                game.pause()
                if not saved:
                    place = add_score(game.score)
                    saved = True
                view.draw_game_over(place)
                menu.disable_continue()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    print 'MAIN MENU'
                    state = 'menu'
                    game.pause()
                
        if state == 'menu':
            screen.blit(menu.canvas,(0,0))
        else:
            screen.blit(view.canvas, (0,0))
        clock.tick(60)
        pygame.display.update()