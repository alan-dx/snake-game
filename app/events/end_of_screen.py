def end_of_screen(snake):
    # event function

    # end of screen
    if (snake.snake_size[0][0] == 0):  # x axis (0,y)
        # snake.movimentation() will automatically adjusts the snake pieces
        snake.snake_size[0] = (600, snake.snake_size[0][1])
    elif (snake.snake_size[0][0] == 600):  # x axis (600,y)
        snake.snake_size[0] = (0, snake.snake_size[0][1])
    elif (snake.snake_size[0][1] == 0):  # y axis (x,600)
        snake.snake_size[0] = (snake.snake_size[0][0], 600)
    elif (snake.snake_size[0][1] == 600):
        snake.snake_size[0] = (snake.snake_size[0][0], 0)
    # end of screen
