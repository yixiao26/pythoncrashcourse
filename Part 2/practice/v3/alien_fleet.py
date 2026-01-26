from alien import Alien


def aliens_per_row(settings):
    alien = Alien(settings, 0, 0)
    alien_width = alien.rect.width
    settings_width = settings.width
    aliens_per_row = []
    row = settings_width // (2 * alien_width)
    for i in range(row):
        aliens_per_row.append(i * 2 * alien_width)
    return aliens_per_row


def aliens_per_column(settings, ship):
    alien = Alien(settings, 0, 0)
    alien_height = alien.rect.height
    settings_height = settings.height
    ship_height = ship.rect.height
    aliens_per_column = []
    column = (settings_height - 3 * ship_height) // (2 * alien_height)
    for i in range(column):
        aliens_per_column.append(i * 2 * alien_height)
    return aliens_per_column


def create_alien_fleet(settings, aliens, ship):
    for y in aliens_per_column(settings, ship):
        for x in aliens_per_row(settings):
            alien = Alien(settings, x, y)
            aliens.add(alien)


def alien_fleet_update(aliens, settings):
    if has_hit_edge(aliens, settings):
        print("HIT EDGE - DROPPING")
        change_direction(aliens)
        drop(aliens)
    aliens.update()


def change_direction(aliens):
    for alien in aliens.sprites():
        alien.moving_speed *= -1


def drop(aliens):
    for alien in aliens.sprites():
        alien.rect.y += alien.dropping_speed


def has_hit_edge(aliens, settings):
    for alien in aliens.sprites():
        if alien.rect.right > settings.width or alien.rect.left < 0:
            return True
    return False
