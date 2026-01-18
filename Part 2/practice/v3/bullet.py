from pygame.sprite import Sprite
import pygame


class Bullet(Sprite):
    def __init__(self, ship):
        super().__init__()

        self.bullet_height = 15
        self.bullet_width = 3
        self.bullet_color = (0, 0, 0)
        self.bullet_speed = 1

        self.image = pygame.Surface((self.bullet_width, self.bullet_height))
        self.image.fill(self.bullet_color)
        self.rect = self.image.get_rect()
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

    def update(self):
        self.rect.y -= self.bullet_speed
        if self.rect.bottom < 0:
            self.kill()
