import pygame
import random
from pygame.locals import RLEACCEL
from abc import ABC, abstractmethod


class GameSprite(ABC,pygame.sprite.Sprite):

    @abstractmethod
    def clone(self):
        pass