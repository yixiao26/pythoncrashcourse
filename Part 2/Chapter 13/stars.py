import pygame
import sys
from pygame.sprite import Sprite 
from pathlib import Path
from pygame.sprite import Group



class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # Load the alien image and set its rect attribute
        file_folder = Path(__file__).resolve().parent.parent
        image_path = file_folder / './alien_invasion/images/alien.bmp'
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        
        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store the alien's exact position
        self.x = float(self.rect.x)
        
    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)


def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = ai_settings.screen_height - (3 * alien_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in the row."""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, aliens):
    """Create a full fleet of aliens."""
    # Create an alien and find the number of aliens in a row.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, alien.rect.height)

    # Create the fleet of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            for alien_number in range(number_aliens_x):
                create_alien(ai_settings, screen, aliens, alien_number, row_number)







def run():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Stars")
    bg_color = (230, 230, 230)  
    aliens = Group()
    ai_settings = Settings()
    while True:
        screen.fill(bg_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() 
        create_fleet(ai_settings, screen, aliens)
        aliens.draw(screen)

        pygame.display.flip()


run()