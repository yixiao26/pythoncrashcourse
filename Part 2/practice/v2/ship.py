import pygame
from pygame.sprite import Sprite
from settings import Settings
from common import get_image_path as gip
from alien import create_fleet_aliens as cfa


class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, settings, window):
        """Initialize the ship and set its starting position."""
        super().__init__()

        self.window = window
        self.settings = settings

        self.moving_right = False
        self.moving_left = False
        self.speed_factor = settings.ship_speed_factor

        self.image = pygame.image.load(gip("ship.bmp"))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.window.get_rect().centerx
        self.rect.bottom = self.window.get_rect().bottom

    def update(self):
        if self.moving_right and self.rect.right < self.window.get_rect().right:
            self.rect.centerx += self.speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.speed_factor

def ship_collide_aliens(ships, aliens, window, settings):
    collisions = pygame.sprite.groupcollide(ships, aliens, True, True)
    if collisions:
        aliens.empty()
        new_ship = Ship(settings, window)
        ships.add(new_ship)
        cfa(aliens, window, new_ship, settings)
        pygame.time.delay(500)
        settings.games_allowed -= 1

def aliens_meet_bottom(ships, aliens, window, settings):
    for alien in aliens:
        if alien.rect.bottom >= settings.window_height:
            aliens.empty()
            ships.empty()

            new_ship = Ship(settings, window)
            ships.add(new_ship)

            cfa(aliens, window, new_ship, settings)
            pygame.time.delay(500)
            settings.games_allowed -= 1
            return