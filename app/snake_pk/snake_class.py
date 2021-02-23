import pygame


class Snake:

    def __init__(self, init_direction):
        self.snake_size = [(200, 200), (210, 200), (220, 200)]
        self.snake_direction = init_direction
        self.snake_skin = pygame.Surface((10, 10))  # set size of pieace snake

        self.snake_skin.fill((255, 255, 255))  # set fill of pieace snake
