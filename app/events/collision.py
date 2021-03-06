def collision(snake, menu, player):
    # event function
    for segment in snake.snake_size[1:]:
        # print(segment)
        if (snake.snake_size[0] == segment):
            print('=============== GAME OVER ===============')
            print(player)
            snake.reset_snake_size()  # the position of this line is very important
            # put it below of menu.show_menu() cause bugs
            # since snake.reset_snake_size() will not be called
            menu.show_menu(True)
            break
