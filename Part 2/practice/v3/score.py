import pygame
from pygame.sprite import Sprite


class Score(Sprite):
    def __init__(self, settings):
        super().__init__()
        self.settings = settings
        self.score = self.settings.score
        font = pygame.font.SysFont(None, 48)
        self.image = font.render(str(self.score), True, self.settings.text_color)
        self.rect = self.image.get_rect()

    def update(self):
        font = pygame.font.SysFont(None, 48)
        self.image = font.render(str(self.settings.score), True, self.settings.text_color)
        self.rect.centerx = self.settings.width // 2
        self.rect.top = 0
