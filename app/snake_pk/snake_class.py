import pygame


class Snake:

    def __init__(self):
        self.snake_size = [(200, 200), (210, 200), (220, 200)]
        self.snake_skin = pygame.Surface((10, 10))  # set size of pieace snake

        self.snake_skin.fill((255, 255, 255))  # set fill of snake pieace

    def move_up(self):
        self.snake_size[0] = (
            self.snake_size[0][0], self.snake_size[0][1] - 10
        )
        return self

    def move_down(self):
        self.snake_size[0] = (
            self.snake_size[0][0], self.snake_size[0][1] + 10
        )
        return self

    def move_right(self):
        self.snake_size[0] = (
            self.snake_size[0][0] + 10, self.snake_size[0][1]
        )
        return self

    def move_left(self):
        self.snake_size[0] = (
            self.snake_size[0][0] - 10, self.snake_size[0][1]
        )
        return self

    # Snake.movimentation() automatically adjusts the snake pieces
    def movimentation(self):
        for i in range(len(self.snake_size) - 1, 0, -1):
            # makes the snake movimentation
            self.snake_size[i] = (
                self.snake_size[i-1][0], self.snake_size[i-1][1]
            )

    def reset_snake_size(self):
        print('resetou')
        # reset the snake_size when an colission ocurred
        self.snake_size = [(200, 200), (210, 200), (220, 200)]
