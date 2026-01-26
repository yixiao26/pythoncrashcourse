import pygame
from pygame.sprite import Sprite


class HighScore(Sprite):
    def __init__(self, settings):
        super().__init__()
        self.high_score = 0
        self.settings = settings
        font = pygame.font.SysFont(None, 48)
        self.image = font.render(str(self.high_score), True, self.settings.text_color)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.centerx = self.settings.width - 20
        self.rect.top = 0
