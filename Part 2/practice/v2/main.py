import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from ship import ship_collide_aliens as sca
import events
from bullet import Bullet
from alien import Alien
import alien
import bullet
from ship import aliens_meet_bottom as amb


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
    aliens = Group()

    alien.create_fleet_aliens(aliens, window, ship, settings)

    # Main loop
    while True:
        # Check and update events
        events.check_events(ships, bullets, settings, window)

        if settings.games_allowed >= 0:
            ships.update()
            bullets.update()
            aliens.update()
            bullet.bullet_collide_alien(bullets, aliens, window, ship, settings)
            sca(ships, aliens, window, settings)
            amb(ships, aliens, window, settings)

        # Fill and draw to window
        window.fill(settings.window_colour)
        ships.draw(window)
        bullets.draw(window, ships)
        aliens.draw(window)

        # Blit and flip to window
        pygame.display.flip()


main()
