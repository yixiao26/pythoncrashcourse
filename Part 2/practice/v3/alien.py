from pygame.sprite import Sprite
import pygame
from pathlib import Path


class Alien(Sprite):
    def __init__(self, settings, x, y):
        super().__init__()
        self.settings = settings

        folder = Path(__file__).parent.resolve()
        self.image = pygame.image.load(folder / "images" / "alien.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y

        self.moving_speed = 1
        self.dropping_speed = 50

    def update(self):
        self.rect.x += self.moving_speed
