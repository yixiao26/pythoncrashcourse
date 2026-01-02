from pygame.sprite import Sprite
from utility import load_image


class Alien(Sprite):
    def __init__(self):
        """Initialize the ship and set its starting position."""
        super().__init__()

        # Load image
        self.image = load_image("alien.bmp")
        self.rect = self.image.get_rect()

    def update(self):
        pass
