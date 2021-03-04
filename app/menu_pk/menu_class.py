import pygame_menu


class Menu():
    def __init__(self, game_function, screen):
        self.menu_layout = pygame_menu.Menu(
            400, 500, 'Snake Game', theme=pygame_menu.themes.THEME_DARK)
        self.menu_start_btn = self.menu_layout.add_button(
            'Play', game_function)
        self.menu_start_btn = self.menu_layout.add_button(
            'Quit', pygame_menu.events.EXIT)
        self.game_screen = screen

    def show_menu(self, game_over=False):

        if game_over:
            self.menu_layout.set_title('Game Over, Try again!')

        self.menu_layout.mainloop(self.game_screen)
        # self.menu_layout.remove_widget()
