import pygame
import sys
from bullet import Bullet


def check_events(ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            handle_keydown(event, ship, bullets)
        if event.type == pygame.KEYUP:
            handle_keyup(event, ship)
        if event.type == pygame.QUIT:
            sys.exit()


def handle_keydown(event, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()
    elif event.key == pygame.K_SPACE:
        shoot_bullet(ship, bullets)


def shoot_bullet(ship, bullets):
    if len(bullets) < ship.bullets_allowed:
        new_bullet = Bullet(ship)
        bullets.add(new_bullet)


def handle_keyup(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
