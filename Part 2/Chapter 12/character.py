import pygame

class Character:
    """A class to manage a game character."""

    def __init__(self, screen):
        """Initialize the character and set its starting position."""
        self.screen = screen

        # Load the character image and get its rect.
        self.image = pygame.image.load('Part 2/alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new character at the center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):
        """Draw the character at its current location."""
        self.screen.blit(self.image, self.rect)
        