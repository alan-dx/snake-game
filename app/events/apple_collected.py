import math
from app.utils.draw_text import draw_text


def apple_collected(snake, apple, player, frame_rate, clock, screen):

    if (apple.pos == snake.snake_size[0]):
        apple.new_pos()
        player.increase_score()
        frame_rate += 1

        # draw_text(screen, str(player), 18, 300, 10)

        # Snake.movimentation() automatically adjusts the NEW snake piece
        snake.snake_size.append((0, 0))

    return frame_rate  # return because primitive type of python isn't OOP
