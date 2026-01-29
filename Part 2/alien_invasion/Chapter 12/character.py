import pygame
from pathlib import Path
from pygame.sprite import Sprite


class Character:
    """A class to manage a game character."""

    def __init__(self, screen):
        """Initialize the character and set its starting position."""
        self.screen = screen

        # Load the character image and get its rect.

        folder_name = Path(__file__).resolve().parent.parent
        image_path = folder_name / 'alien_invasion/images/ship.bmp'
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new character at the center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.speed_factor = 1.5
    
    def update(self):
        """Update the character's position based on the movement flags."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.speed_factor
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= self.speed_factor 
        if self.moving_up and self.rect.top > 0:
            self.rect.centery -= self.speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery += self.speed_factor
        self.blitme()

        
    
    def move_right(self):
        """Move the character to the right."""
        self.moving_right = True

    def move_left(self):
        """Move the character to the left."""
        self.moving_left = True

    def move_up(self):
        """Move the character up."""
        self.moving_up = True

    def move_down(self):
        """Move the character down."""
        self.moving_down = True
        
    def stop_moving_right(self):
        """Stop moving the character to the right."""
        self.moving_right = False

    def stop_moving_left(self):
        """Stop moving the character to the left."""
        self.moving_left = False

    def stop_moving_up(self):
        """Stop moving the character up."""
        self.moving_up = False

    def stop_moving_down(self):
        """Stop moving the character down."""
        self.moving_down = False

    def fire_bullet(self, bullets):
        """Fire a bullet if limit not reached yet."""
        # Create a new bullet and add it to the bullets group.
        new_bullet = Bullet(self.screen, self)
        bullets.add(new_bullet)




    def blitme(self):
        """Draw the character at its current location."""
        self.screen.blit(self.image, self.rect)
        
class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""
    
    def __init__(self, screen, character):
        """Create a bullet object at the ship's current position."""
        super(Bullet, self).__init__()
        self.screen = screen
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = 60, 60, 60
        self.bullet_speed_factor = 1
        
        # Create a bullet rect at (0, 0) and then set current position.
        self.rect = pygame.Rect(0, 0, self.bullet_width,
            self.bullet_height)
        self.x = float(character.rect.x)
        self.rect.centery = character.rect.centery
        self.rect.top = character.rect.top
        
        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)
        
        self.color = self.bullet_color
        self.speed_factor = self.bullet_speed_factor

    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet
        self.x += self.speed_factor
        # Update the rect position
        self.rect.x = self.x
        
    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)