import pygame
from pygame.sprite import Sprite
from pathlib import Path
from utility import load_image



class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, window):
        """Initialize the ship and set its starting position."""
        super().__init__()

        self.window = window

        # Load image
        self.image = load_image("ship.bmp")
        self.rect = self.image.get_rect()
        self.rect.centerx = window.get_rect().centerx
        self.rect.bottom = window.get_rect().bottom

        self.speed_factor = 2

        # Movement flags
        self.moving_left = False
        self.moving_right = False


    def update(self):
        if self.moving_right and self.rect.right < self.window.get_rect().right:
            self.rect.centerx += self.speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.speed_factor