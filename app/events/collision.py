from app.database.add_user_on_table import add_user_on_table


def collision(snake, menu, player):
    # event function
    for segment in snake.snake_size[1:]:
        # print(segment)
        if (snake.snake_size[0] == segment):
            print('=============== GAME OVER ===============')
            add_user_on_table(menu.get_player_name()[
                              'name_input'], str(player))
            snake.reset_snake_size()  # the position of this line is very important
            # put it below of menu.show_menu() cause bugs
            # since snake.reset_snake_size() will not be called
            menu.show_menu(True)
            break
