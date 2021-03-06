def apple_collected(snake, apple, player):
    if (apple.pos == snake.snake_size[0]):
        apple.new_pos()
        player.increase_score()
        # Snake.movimentation() automatically adjusts the snake pieces
        snake.snake_size.append((0, 0))
