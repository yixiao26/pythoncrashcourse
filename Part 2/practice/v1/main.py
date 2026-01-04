import pygame
from pygame.sprite import Sprite
from pygame.sprite import Group
from screen import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from alien import create_fleet_aliens
import event
import object_clearer as oc


def main():
    # Standard pygame stuff
    pygame.init()
    pygame.display.set_caption("Version 1")

    # Create objects
    settings = Settings()
    window = pygame.display.set_mode((settings.window_width, settings.window_height))
    ships = Group()
    bullets = Group()
    aliens = Group()

    ship = Ship(window)
    ships.add(ship)


    create_fleet_aliens(aliens, window, ship)





    # Main loop
    while True:
        # Handle key events
        event.check_events(ship, bullets, aliens, settings)

        # Update object information
        ships.update()
        bullets.update()
        aliens.update()

        # Clear all unneeded objects
        oc.clear_bullet(bullets)


        # Fill screen
        window.fill(settings.window_color)
        ships.draw(window)
        bullets.draw(window)
        aliens.draw(window)

        # Blit and flip to window
        pygame.display.flip()


main()
