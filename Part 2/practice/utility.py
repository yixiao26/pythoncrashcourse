import pygame
from pathlib import Path
def load_image(file_name):
    file_folder = Path(__file__).resolve().parent
    image_path = file_folder / f'images/{file_name}'
    return pygame.image.load(image_path)