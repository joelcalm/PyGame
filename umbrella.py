import pygame
import random
import math
from pygame.locals import RLEACCEL
from gamesprite import GameSprite

from screen import Screen


# Define the cloud object extending pygame.sprite.Sprite
# Use an image for a better looking sprite
class Umbrella(GameSprite):

    Max_Speed = 10
    Min_Speed = 5

    def __init__(self):
        super(Umbrella, self).__init__()
        self.surf = pygame.image.load("icons/umbrella.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        # The starting position is randomly generated, as is the speed
        self.rect = self.surf.get_rect(
            center=(
                random.randint(Screen.width + 20, Screen.width + 100),
                random.randint(0, Screen.height),
            )
        )
        self.speed = random.randint(self.Min_Speed, self.Max_Speed)
        self.time = 0

    # Move the cloud based on a constant speed
    # Remove it when it passes the left edge of the screen.py
    def update(self):
        self.time += 1
        speed_x = -self.Min_Speed
        speed_y = self.speed/4
        self.rect.move_ip(speed_x, speed_y)
        if self.rect.right < 0:
            self.kill()
    
    def clone(self):
        return Umbrella()