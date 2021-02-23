import pygame
from pygame.locals import *
from app.snake_pk.snake_class import Snake
from app.apple_pk.apple_class import Apple

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Snake Game')

# directions keys
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
# directions keys

snake = Snake(LEFT)
apple = Apple()


def app():
    while True:
        # 7:07
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

        screen.fill((0, 0, 0))  # clean the screen

        screen.blit(apple.apple_skin, apple.init_pos)
        for pos in snake.snake_size:
            # print the snake on indicated position
            screen.blit(snake.snake_skin, pos)

        pygame.display.update()
