import pygame
from pygame.sprite import Sprite
from settings import Settings
from pygame.sprite import Group
from ship import Ship
from object_manager import check_events
from bullet import Bullet
from alien import Alien
from alien_fleet import create_alien_fleet
from alien_fleet import alien_fleet_update
from collision_manager import ship_collision_aliens
from collision_manager import aliens_collision_bullets
from collision_manager import aliens_screen_bottom
from collision_manager import destroy_game
from button import Button

clock = pygame.time.Clock()


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
    alien = Alien(window, 0, 0)
    aliens.add(alien)

    button = Button(settings)
    buttons = Group()
    buttons.add(button)

    create_alien_fleet(settings, aliens, ship)

    # Main loop
    while True:

        # Handle events
        check_events(bullets, settings, button, buttons, window, ships, aliens, ship)

        # Update object positions
        ships.update()
        bullets.update()
        alien_fleet_update(aliens, settings)
        buttons.update(settings)

        # Remove unneeded objects
        ship = ship_collision_aliens(ship, ships, aliens, settings, window)
        aliens_collision_bullets(aliens, bullets)
        ship = aliens_screen_bottom(settings, aliens, ships, window, ship)
        destroy_game(settings, ships, aliens, bullets)

        # Fill screen
        window.fill(settings.bg_color)

        # Blit and flip to window
        ships.draw(window)
        bullets.draw(window)
        aliens.draw(window)
        buttons.draw(window)

        pygame.display.flip()

        clock.tick(220)


main()
