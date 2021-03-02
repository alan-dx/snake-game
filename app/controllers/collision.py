import pygame_menu


def collision(snake_size):
    for segment in snake_size[1:]:
        # print(segment)
        if (snake_size[0] == segment):
            # i will make alert box using pgu module in future
            # to show a game over alert
            print('=============== GAME OVER ===============')
            # pygame.display.flip()
