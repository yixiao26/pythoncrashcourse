import pygame
import sys
from character import Character

def run_blue_sky():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Blue Sky")
    bg_color = (230, 230, 230)  # Sky blue color
    screen.fill(bg_color)
    character = Character(screen)
    character.blitme()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() 
        pygame.display.flip()


run_blue_sky()