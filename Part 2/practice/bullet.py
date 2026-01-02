from pygame.sprite import Sprite
import pygame
class Bullet(Sprite):

    def __init__(self):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.color = 0, 0, 0
        self.width = 3
        self.height = 15
        self.speed_factor = 1

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)

        self.rect = self.image.get_rect()
    def update(self):
        self.rect.centerx = 500