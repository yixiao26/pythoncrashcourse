from alien import Alien


def aliens_per_row(settings):
    alien = Alien(settings, 0, 0)
    alien_width = alien.rect.width
    settings_width = settings.width
    aliens_per_row = []
    row = settings_width // (2 * alien_width)
    for i in range(row):
        aliens_per_row.append(i * 2 * alien_width)
    print(aliens_per_row)
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
    print(aliens_per_column)
    return aliens_per_column


def create_alien_fleet(settings, aliens, ship):
    alien = Alien(settings, 0, 0)
    for x in aliens_per_column(settings, ship):
        for y in aliens_per_row(settings):
            alien = Alien(settings, y, x)
            aliens.add(alien)


def alien_fleet_update():
    pass
