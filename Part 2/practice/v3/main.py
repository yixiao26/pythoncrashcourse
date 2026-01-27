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
from score import Score
from highscore import HighScore
from level import Level
from lives import Lives
from collision_manager import player_defeats_aliens


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
    scoreboard = Group()
    score = Score(settings)
    highscore = HighScore(settings)
    level = Level(settings)

    ship_lives_x_coor = [0, 30, 60]
    ship_icons = []
    for x in ship_lives_x_coor:
        lives = Lives(x)
        ship_icons.append(lives)

        scoreboard.add(lives)

    scoreboard.add(score)
    scoreboard.add(highscore)
    scoreboard.add(level)

    # Main loop
    while True:

        # Handle events
        if not settings.game_active:
            buttons.empty()
            buttons.add(button)

        ship = check_events(
            bullets, settings, button, buttons, window, ships, aliens, ship
        )

        player_defeats_aliens(settings, aliens, ship, bullets, ships)

        # Update ship lives display
        for icon in ship_icons:
            if icon not in scoreboard:
                scoreboard.add(icon)
        
        if settings.ship_lives == 0:
            for icon in ship_icons:
                scoreboard.remove(icon)
        elif settings.ship_lives == 1:
            scoreboard.remove(ship_icons[1])
            scoreboard.remove(ship_icons[2])
        elif settings.ship_lives == 2:
            scoreboard.remove(ship_icons[2])

        # Update ship reference to current ship in group
        if ships.sprites():
            ship = ships.sprites()[0]

        # Update object positions
        ships.update()
        bullets.update()
        alien_fleet_update(aliens, settings)
        buttons.update(settings)
        scoreboard.update()

        # Remove unneeded objects
        ship = ship_collision_aliens(ship, ships, aliens, settings, window, bullets)
        aliens_collision_bullets(aliens, bullets, settings)
        ship = aliens_screen_bottom(settings, aliens, ships, window, ship, bullets)
        destroy_game(settings, ships, aliens, bullets)

        # Fill screen
        window.fill(settings.bg_color)

        # Blit and flip to window
        ships.draw(window)
        bullets.draw(window)
        aliens.draw(window)
        buttons.draw(window)
        scoreboard.draw(window)

        pygame.display.flip()

        clock.tick(220)


main()
