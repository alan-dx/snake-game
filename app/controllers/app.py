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

snake = Snake()
apple = Apple()


clock = pygame.time.Clock()


def app():
    my_direction = LEFT  # initial direction
    while True:

        clock.tick(15)  # set frame rate

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if event.type == KEYDOWN:
                if event.key == K_UP:
                    my_direction = UP
                elif event.key == K_DOWN:
                    my_direction = DOWN
                elif event.key == K_RIGHT:
                    my_direction = RIGHT
                elif event.key == K_LEFT:
                    my_direction = LEFT

        if my_direction == UP:
            snake.move_up()

        if my_direction == DOWN:
            snake.move_down()

        if my_direction == RIGHT:
            snake.move_right()

        if my_direction == LEFT:
            snake.move_left()

        if (apple.pos == snake.snake_size[0]):
            apple.new_pos()
            snake.snake_size.append((0, 0))

        snake.movimentation()

        screen.fill((0, 0, 0))  # clean the screen every time

        screen.blit(apple.apple_skin, apple.pos)
        for pos in snake.snake_size:
            # prints the snake on indicated position
            screen.blit(snake.snake_skin, pos)

        pygame.display.update()
