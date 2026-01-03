from pygame.sprite import Sprite
import pygame
class Bullet(Sprite):

    def __init__(self, ship):
        """Initialize the bullet and set its starting position."""
        super().__init__()
        self.color = 0, 0, 0
        self.width = 3
        self.height = 15
        self.speed_factor = 1

        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)

        self.rect = self.image.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        


    def update(self):
        y_coordinate = self.rect.y
        y_coordinate -= self.speed_factor
        self.rect.y = y_coordinate