import pygame
from pygame.sprite import Sprite


class HighScore(Sprite):
    def __init__(self, settings):
        super().__init__()
        self.settings = settings
        font = pygame.font.SysFont(None, 48)
        self.image = font.render(
            str(self.settings.high_score), True, self.settings.text_color
        )
        self.rect = self.image.get_rect()

    def update(self):
        if self.settings.score > self.settings.high_score:
            self.settings.high_score = self.settings.score

        font = pygame.font.SysFont(None, 48)
        self.image = font.render(
            str(self.settings.high_score), True, self.settings.text_color
        )
        self.rect.right = self.settings.width - 60
        self.rect.top = 0
