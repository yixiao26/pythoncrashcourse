import pygame
from alien_fleet import create_alien_fleet
from ship import Ship


def ship_collision_aliens(ship, ships, aliens, settings, window):
    # has ship collide aliens
    if pygame.sprite.groupcollide(ships, aliens, True, True):
        empty_ships_and_aliens(ships, aliens)
        ship = create_new_ship_and_alien_fleet(settings, window, ships, aliens, ship)
    return ship


def empty_ships_and_aliens(ships, aliens):
    ships.empty()
    aliens.empty()


def create_new_ship_and_alien_fleet(settings, window, ships, aliens, ship):
    if settings.ship_lives > 0:
        settings.ship_lives -= 1
        create_alien_fleet(settings, aliens, ship)
        ship = Ship(window)
        ships.add(ship)
        return ship
    else:
        settings.game_active = False
        return ship


def destroy_game(settings, ships, aliens, bullets):
    if settings.game_active == False:
        empty_ships_and_aliens(ships, aliens)
        bullets.empty()
        print("Game is inactive")
        return


def aliens_collision_bullets(aliens, bullets):
    for alien, bullet in aliens_bullets_collision_pairs(aliens, bullets).items():
        aliens.remove(alien)
        bullets.remove(bullet)


def aliens_bullets_collision_pairs(aliens, bullets):
    collision_pairs = pygame.sprite.groupcollide(aliens, bullets, False, False)
    return collision_pairs


def aliens_screen_bottom(settings, aliens, ships, window, ship):
    if alien_reach_bottom(settings, aliens):
        empty_ships_and_aliens(ships, aliens)
        return create_new_ship_and_alien_fleet(settings, window, ships, aliens, ship)
    return ship


def alien_reach_bottom(settings, aliens):
    for alien in aliens.sprites():
        if alien.rect.bottom >= settings.height:
            return True
    return False


def on_click(settings, buttons, window, ships, aliens, ship):
    settings.ship_lives = 3
    settings.game_active = True
    create_new_ship_and_alien_fleet(settings, window, ships, aliens, ship)
    # pygame.mouse.set_visible(False)
    # buttons.empty()
