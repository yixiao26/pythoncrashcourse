import pygame
import sys
from ship import Ship
from bullet import Bullet
from pygame.sprite import Group


def check_events(ships, bullets, settings, window):
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        elif e.type == pygame.KEYDOWN:
            key_down_events(e, ships, bullets, settings, window)
        elif e.type == pygame.KEYUP:
            key_up_events(e, ships)


def key_down_events(e, ships, bullets, settings, window):
    if e.key == pygame.K_RIGHT:
        for ship in ships:
            ship.moving_right = True
    elif e.key == pygame.K_LEFT:
        for ship in ships:
            ship.moving_left = True
    elif e.key == pygame.K_q:
        sys.exit()
    elif e.key == pygame.K_SPACE:
        for ship in ships:
            if len(bullets) < settings.bullets_allowed:
                bullet = Bullet(settings, window, ship)
                bullets.add(bullet)
        



def key_up_events(e, ships):
    if e.key == pygame.K_RIGHT:
        for ship in ships:
            ship.moving_right = False
    elif e.key == pygame.K_LEFT:
        for ship in ships:
            ship.moving_left = False


