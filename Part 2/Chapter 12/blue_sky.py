import pygame
import sys
from character import Character
from pygame.sprite import Group



def handle_key_event(event, character, bullets):
    """Respond to keypresses."""
    try:
        print(event.key)
    except:
        pass
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            character.move_right()
        elif event.key == pygame.K_LEFT:
            character.move_left()
        elif event.key == pygame.K_UP:
            character.move_up()
        elif event.key == pygame.K_DOWN:
            character.move_down()
        elif event.key == pygame.K_SPACE:
            character.fire_bullet(bullets)

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            character.stop_moving_right()
        elif event.key == pygame.K_LEFT:
            character.stop_moving_left()
        elif event.key == pygame.K_UP:
            character.stop_moving_up()
        elif event.key == pygame.K_DOWN:
            character.stop_moving_down()

def remove_bullet(bullets, screen):
    for bullet in bullets.copy():
        if bullet.rect.right >= screen.get_rect().right:
            bullets.remove(bullet)
    
def run_blue_sky():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Blue Sky")
    bg_color = (230, 230, 230)  # Sky blue color
    character = Character(screen)
    bullets = Group()
    while True:
        screen.fill(bg_color)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit() 
            handle_key_event(event, character, bullets)
        for bullet in bullets:
            bullet.draw_bullet()
            bullet.update()
        remove_bullet(bullets, screen)
        print(len(bullets))
        character.update()

        
        

        pygame.display.flip()


run_blue_sky()