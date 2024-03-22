import pygame
import random
from pygame.locals import RLEACCEL
from gamesprite import GameSprite

class FactorySprites():

    def __init__(self, periods, event_types,prototypes):
        self._periods = periods
        self._event_types = event_types
        self._prototypes = prototypes

    def make(self):
        return self._prototypes[event_type - self._event_types[0]].clone()