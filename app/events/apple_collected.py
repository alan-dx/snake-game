import math


def apple_collected(snake, apple, player, frame_rate, clock):

    if (apple.pos == snake.snake_size[0]):
        apple.new_pos()
        player.increase_score()
        frame_rate += 2
        # Snake.movimentation() automatically adjusts the snake pieces
        snake.snake_size.append((0, 0))

    return frame_rate
