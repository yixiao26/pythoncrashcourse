from pygame.sprite import Sprite
import pygame
from pathlib import Path


class Alien(Sprite):
    def __init__(self, window):
        super().__init__()
        self.window = window

        folder = Path(__file__).parent.resolve()
        self.image = pygame.image.load(folder / "images" / "alien.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.moving_speed = 1

    def update(self):
        self.rect.x += self.moving_speed
