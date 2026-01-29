import pygame
from pygame.sprite import Sprite
from pathlib import Path


class Lives(Sprite):
    def __init__(self, x):
        super().__init__()
        self.x = x
        folder = Path(__file__).parent.resolve()
        self.ship_image = pygame.image.load(folder / "images" / "ship.bmp")
        self.image = pygame.transform.scale(self.ship_image, (30, 30))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x = self.x
        self.rect.y = 0
