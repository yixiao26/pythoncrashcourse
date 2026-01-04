import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, settings, window, ship):
        super().__init__()
        self.settings = settings
        self.window = window
        self.ship = ship

        self.image = pygame.Surface(
            (self.settings.bullet_width, self.settings.bullet_height)
        )
        self.image.fill(self.settings.bullet_colour)

        self.rect = self.image.get_rect()
        self.rect.centerx = self.ship.rect.centerx
        self.rect.top = self.ship.rect.top

        self.bullet_speed_factor = self.settings.bullet_speed_factor
    
    def update(self):
        self.rect.y -= self.bullet_speed_factor
        if self.rect.top < 0:
            self.kill()