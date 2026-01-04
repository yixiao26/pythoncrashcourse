import sys
import pygame
from bullet import Bullet


def check_events(ship, bullets, aliens, settings):
    """Respond to keypresses and mouse events."""

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        elif e.type == pygame.KEYDOWN:
            keydown_events(e, ship, bullets, aliens, settings)
        elif e.type == pygame.KEYUP:
            keyup_events(e, ship, bullets, aliens)


def keydown_events(e, ship, bullets, aliens, settings):
    if e.key == pygame.K_RIGHT:
        ship.moving_right = True

    elif e.key == pygame.K_LEFT:
        ship.moving_left = True

    elif e.key == pygame.K_SPACE:
        if len(bullets) < settings.bullets_allowed:
            bullet = Bullet(ship)
            bullets.add(bullet)
    
    elif e.key == pygame.K_q:
        sys.exit()




def keyup_events(e, ship, bullets, aliens):
    if e.key == pygame.K_RIGHT:
        ship.moving_right = False

    elif e.key == pygame.K_LEFT:
        ship.moving_left = False
