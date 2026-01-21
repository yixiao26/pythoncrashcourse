from pathlib import Path
import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    def __init__(self, window):
        super().__init__()
        self.window = window

        folder = Path(__file__).parent.resolve()
        self.image = pygame.image.load(folder / "images" / "ship.bmp")
        self.rect = self.image.get_rect()

        self.rect.centerx = window.get_rect().centerx
        self.rect.bottom = window.get_rect().bottom

        self.moving_right = False
        self.moving_left = False

        self.moving_speed = 2
        self.bullets_allowed = 3


    def update(self):
        if self.moving_right and self.rect.right < self.window.get_rect().right:
            self.rect.x += self.moving_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.moving_speed
