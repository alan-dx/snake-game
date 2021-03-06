import math


def apple_collected(snake, apple, player, frame_rate, clock):

    if (apple.pos == snake.snake_size[0]):
        apple.new_pos()
        player.increase_score()
        frame_rate += 1
        print(clock.get_fps(), frame_rate)
        # Snake.movimentation() automatically adjusts the snake pieces
        snake.snake_size.append((0, 0))

    return frame_rate
