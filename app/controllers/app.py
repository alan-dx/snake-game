import pygame
import pygame_menu
from pygame.locals import *
from app.snake_pk.snake_class import Snake
from app.apple_pk.apple_class import Apple
from app.menu_pk.menu_class import Menu
from app.player_pk.player_class import Player
from app.controllers.end_of_screen import end_of_screen
from app.controllers.collision import collision


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
                # to do: create a function for when the apple was collected
                apple.new_pos()
                player.increase_score()
                # Snake.movimentation() automatically adjusts the snake pieces
                snake.snake_size.append((0, 0))

            # end of screen verificator
            end_of_screen(snake)
            # end of screen verificator

            # colision verificator
            if collision(snake.snake_size):
                print(player)
                snake.reset_snake_size()  # the position of this line is very important
                # put it below of menu.show_menu() cause bugs
                # since snake.reset_snake_size() will not be called
                menu.show_menu(True)
                break
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
