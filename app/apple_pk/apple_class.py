import pygame
import random


class Apple:
    def __init__(self):
        self.apple_skin = pygame.Surface((10, 10))
        self.apple_skin.fill((255, 0, 0))

        self.pos = (
            # // 10 * 10 generates numbers spaced every 10
            # the Surface is of 10px X 10px
            # 221 // 10 = 22 * 10 = 220
            random.randint(0, 590) // 10 * 10,
            random.randint(0, 590) // 10 * 10
        )

    def new_pos(self):
        self.pos = (
            # // 10 * 10 generates numbers spaced every 10
            # the Surface is of 10px X 10px
            # 221 // 10 = 22 * 10 = 220
            random.randint(0, 590) // 10 * 10,
            random.randint(0, 590) // 10 * 10
        )
