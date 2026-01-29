import pygame
from pygame.sprite import Sprite


class Button(Sprite):
    def __init__(self, settings):
        super().__init__()
        self.settings = settings

        self.image = pygame.Surface(
            (self.settings.button_width, self.settings.button_height)
        )
        self.image.fill(self.settings.button_color)
        font = pygame.font.SysFont(None, 48)
        self.image = font.render(
            "Play", True, self.settings.text_color, self.settings.button_color
        )

        self.rect = self.image.get_rect()

    def update(self, settings):
        self.settings = settings
        self.rect.centerx = self.settings.width // 2
        self.rect.centery = self.settings.height // 2
