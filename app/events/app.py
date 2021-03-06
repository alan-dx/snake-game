import pygame
import pygame_menu
from pygame.locals import *
from app.snake_pk.snake_class import Snake
from app.apple_pk.apple_class import Apple
from app.menu_pk.menu_class import Menu
from app.player_pk.player_class import Player
from app.events.end_of_screen import end_of_screen
from app.events.collision import collision
from app.events.apple_collected import apple_collected


def app():
    # the app function was created just for a better understanding of the code
    # when import this file on game file

    # pygame
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Snake Game')
    # pygame

    # directions keys
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
    # directions keys

    snake = Snake()
    apple = Apple()
    player = Player('Player')

    clock = pygame.time.Clock()

    def start_the_game():
        my_direction = LEFT  # initial direction
        frame_rate = 11

        while True:
            # set frame rate, cause a limitation on while
            clock.tick(frame_rate)

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

            # apple collected verificator
            frame_rate = apple_collected(  # primitive type of python isn't OOP
                snake, apple, player, frame_rate, clock)
            # apple collected verificator

            # end of screen verificator
            end_of_screen(snake)
            # end of screen verificator

            # colision verificator
            collision(snake, menu, player)
            # colision verificator

            snake.movimentation()

            # clear the screen and then print the new position of the elements
            screen.fill((0, 0, 0))

            screen.blit(apple.apple_skin, apple.pos)
            for pos in snake.snake_size:
                # prints the snake on indicated position
                screen.blit(snake.snake_skin, pos)

            pygame.display.update()

    menu = Menu(start_the_game, screen)

    menu.show_menu()
