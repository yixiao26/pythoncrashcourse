import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group
from screen import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
import event


def main():
    # Standard pygame stuff
    pygame.init()
    pygame.display.set_caption("Alien Invasion")

    # Create objects
    settings = Settings()
    window = pygame.display.set_mode((settings.window_width, settings.window_height))
    ships = Group()
    bullets = Group()
    aliens = Group()

    ship = Ship(window)
    ships.add(ship)

    bullet = Bullet()
    bullets.add(bullet)

    alien = Alien()
    aliens.add(alien)

    # Main loop
    while True:
        # Handle key events
        event.check_events(ships, bullets, aliens)

        # Update object information
        ships.update()
        bullets.update()
        aliens.update()

        # Fill screen
        window.fill(settings.window_color)
        ships.draw(window)
        bullets.draw(window)
        aliens.draw(window)

        # Blit and flip to window
        pygame.display.flip()


main()
