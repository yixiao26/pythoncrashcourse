import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import events
from bullet import Bullet
from alien import Alien
import alien


def main():
    # Pygame stuff
    pygame.init()
    settings = Settings()

    window = pygame.display.set_mode((settings.window_width, settings.window_height))
    pygame.display.set_caption("Version 2")

    # Create objects
    ships = Group()
    ship = Ship(settings, window)
    ships.add(ship)

    bullets = Group()

    alien.create_fleet_aliens(ships, window, ship)

    # Main loop
    while True:
        # Check and update events
        events.check_events(ships, bullets, settings, window)

        ships.update()
        bullets.update()

        # Fill and draw to window
        window.fill(settings.window_colour)
        ships.draw(window)
        bullets.draw(window, ships)

        # Blit and flip to window
        pygame.display.flip()


main()
