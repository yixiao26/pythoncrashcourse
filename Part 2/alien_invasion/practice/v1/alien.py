from pygame.sprite import Sprite
from utility import load_image


class Alien(Sprite):
    def __init__(self, x, y, settings):
        """Initialize the ship and set its starting position."""
        super().__init__()

        self.speed_factor = 1
        self.settings = settings
        # Load image
        self.image = load_image("alien.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y += self.speed_factor
        if self.rect.top > self.settings.window_height:
            self.rect.bottom = 0





def get_alien_coordinates(alien, window, ship):
        window_width = window.get_rect().width
        alien_width = alien.rect.width
        m = window_width // (2*alien_width)

        x = []
        for i in range(1, m + 1):
            x.append((i*((window_width - m*alien.rect.width)/(m+1)) + ((i-1)*alien.rect.width)))
    
        window_height = window.get_rect().height
        alien_height = alien.rect.height
        ship_height = ship.rect.height
        n = (window_height - 3*ship_height) // (2*alien_height)

        y = []
        for i in range(n):
            y.append(i * (2*alien.rect.height))

        return x, y
    
        
def create_fleet_aliens(aliens, window, ship, settings):
    alien = Alien(0, 0, settings)
    x_coor_list, y_coor_list = get_alien_coordinates(alien, window, ship)

    for x_coor in x_coor_list:
        for y_coor in y_coor_list:
            alien = Alien(x_coor, y_coor, settings)
            aliens.add(alien)