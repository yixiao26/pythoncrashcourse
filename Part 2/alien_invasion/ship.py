import pygame
from pathlib import Path
import math

class Ship():
    """A class to manage the ship."""

    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect.
        file_folder = Path(__file__).resolve().parent
        image_path = file_folder / 'images/ship.bmp'
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.moving_right = False
        self.moving_left = False

    
    def update(self):
        """Update the ship's position based on the movement flag."""
        # Update the ship's center value, not the rect.
        new_center = self.rect.centerx
        if self.moving_right and self.rect.right < self.screen_rect.right:
            new_center += math.ceil(self.ai_settings.ship_speed_factor)
        
        if self.moving_left and self.rect.left > 0:
            new_center -= math.ceil(self.ai_settings.ship_speed_factor)
    
        self.rect.centerx = new_center


    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.centerx = self.screen_rect.centerx