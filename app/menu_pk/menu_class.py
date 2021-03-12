import pygame_menu
from app.database.list_score import list_score


class Menu():
    def __init__(self, game_function, screen):
        self.menu_layout = pygame_menu.Menu(
            400, 500, 'Snake Game', theme=pygame_menu.themes.THEME_DARK)
        self.menu_start_btn = self.menu_layout.add_button(
            'Play', game_function)
        self.menu_start_btn = self.menu_layout.add_button(
            'Quit', pygame_menu.events.EXIT)
        self.menu_input_name = self.menu_layout.add_text_input(
            'Player: ', default="Fulano", textinput_id='name_input')
        self.game_screen = screen

    def show_menu(self, game_over=False):

        if game_over:
            self.menu_layout.set_title('Game Over, Try again!')
            list_score()

        self.menu_layout.mainloop(self.game_screen)
        # self.menu_layout.remove_widget()

    def get_player_name(self):
        return self.menu_layout.get_input_data()
