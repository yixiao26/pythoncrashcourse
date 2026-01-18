import pygame
from pygame.sprite import Sprite
from settings import Settings
from pygame.sprite import Group
from ship import Ship
from object_manager import check_events
from bullet import Bullet
from alien import Alien


def main():
    pygame.init()
    pygame.display.set_caption("Alien Invasion Pygame")

    # Create all objects
    settings = Settings()
    window = pygame.display.set_mode((settings.width, settings.height))

    ships = Group()
    ship = Ship(window)
    ships.add(ship)

    bullets = Group()

    aliens = Group()
    alien = Alien(window)
    aliens.add(alien)

    # Main loop
    while True:
        # Handle events
        check_events(ship, bullets)

        # Update object information
        ships.update()
        bullets.update()
        aliens.update()

        # Remove unneeded objects

        # Fill screen
        window.fill(settings.bg_color)

        # Blit and flip to window
        ships.draw(window)
        bullets.draw(window)
        aliens.draw(window)
        pygame.display.flip()


main()
