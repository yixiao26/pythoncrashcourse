import sys
import pygame
def check_events(ships, bullets, aliens):
    """Respond to keypresses and mouse events."""
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        elif e.type == pygame.KEYDOWN:
            keydown_events(e, ships, bullets, aliens)
        elif e.type == pygame.KEYUP:
            keyup_events(e, ships, bullets, aliens)


def keydown_events(e, ships, bullets, aliens):
    if e.key == pygame.K_RIGHT:
        for ship in ships:
            ship.moving_right = True
        
    elif e.key == pygame.K_LEFT:
        for ship in ships:
            ship.moving_left = True
    elif e.key == pygame.K_SPACE:
        pass

    

def keyup_events(e, ships, bullets, aliens):
    if e.key == pygame.K_RIGHT:
        for ship in ships:
            ship.moving_right = False
        
    elif e.key == pygame.K_LEFT:
        for ship in ships:
            ship.moving_left = False
    elif e.key == pygame.K_SPACE:
        pass
