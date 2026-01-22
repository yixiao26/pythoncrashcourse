import pygame
import sys
from bullet import Bullet
from collision_manager import on_click
from button import Button
from pygame.sprite import Group


def check_events(bullets, settings, button, buttons, window, ships, aliens, ship):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            handle_keydown(event, ship, bullets, settings)
        if event.type == pygame.KEYUP:
            handle_keyup(event, ship, settings)
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            handle_mouse_click(settings, button, buttons, window, ships, aliens, ship)


def handle_mouse_click(settings, button, buttons, window, ships, aliens, ship):
    if not settings.game_active and button.rect.collidepoint(pygame.mouse.get_pos()):
        print("Button clicked")
        on_click(settings, buttons, window, ships, aliens, ship)


def handle_keydown(event, ship, bullets, settings):
    if event.key == pygame.K_q:
        sys.exit()
    if not settings.game_active:
        return
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        shoot_bullet(ship, bullets, settings)


def shoot_bullet(ship, bullets, settings):
    if not settings.game_active:
        return
    if len(bullets) < ship.bullets_allowed:
        new_bullet = Bullet(ship)
        bullets.add(new_bullet)


def handle_keyup(event, ship, settings):
    if not settings.game_active:
        return
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
