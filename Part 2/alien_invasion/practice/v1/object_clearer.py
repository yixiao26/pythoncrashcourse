def clear_bullet(bullets):
    for bullet in bullets.copy():
        if bullet.rect.top < 0:
            bullets.remove(bullet)
