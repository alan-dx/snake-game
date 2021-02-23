import pygame
import random


class Apple:
    def __init__(self):
        self.apple_skin = pygame.Surface((10, 10))
        self.apple_skin.fill((255, 0, 0))

        self.init_pos = (random.randint(0, 590), random.randint(0, 590))
