import pygame
from alien_fleet import create_alien_fleet
from ship import Ship


def ship_collision_aliens(ship, ships, aliens, settings, window, bullets):
    # has ship collide aliens
    if pygame.sprite.groupcollide(ships, aliens, True, True):
        empty_ships_and_aliens(ships, aliens)
        bullets.empty()
        ship = create_new_ship_and_alien_fleet(settings, window, ships, aliens, ship)
    return ship


def empty_ships_and_aliens(ships, aliens):
    ships.empty()
    aliens.empty()


def create_new_ship_and_alien_fleet(settings, window, ships, aliens, ship):
    settings.ship_lives -= 1
    if settings.ship_lives > 0:
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
        return


def player_defeats_aliens(settings, aliens, ship, bullets, ships):
    print("player_defeats_aliens")
    if settings.game_active and len(aliens) == 0 and settings.ship_lives > 0:
        create_alien_fleet(settings, aliens, ship)
        settings.level += 1
        update_speed(settings, bullets, aliens, ships)
        return


def update_speed(settings, bullets, aliens, ships):
    for bullet in bullets:
        bullet.bullet_speed = bullet.bullet_speed + settings.level
        print(bullet.bullet_speed)

    for alien in aliens:
        alien.moving_speed = alien.moving_speed + settings.level
        print(alien.moving_speed)

    for ship in ships:
        ship.moving_speed = ship.moving_speed + settings.level
        print(ship.moving_speed)


def aliens_collision_bullets(aliens, bullets):
    for alien, bullet in aliens_bullets_collision_pairs(aliens, bullets).items():
        aliens.remove(alien)
        bullets.remove(bullet)


def aliens_bullets_collision_pairs(aliens, bullets):
    collision_pairs = pygame.sprite.groupcollide(aliens, bullets, False, False)
    return collision_pairs


def aliens_screen_bottom(settings, aliens, ships, window, ship, bullets):
    if alien_reach_bottom(settings, aliens):
        empty_ships_and_aliens(ships, aliens)
        bullets.empty()
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
    create_alien_fleet(settings, aliens, ship)
    ship = Ship(window)
    ships.add(ship)
    # pygame.mouse.set_visible(False)
    buttons.empty()
    return ship
