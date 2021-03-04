import pygame_menu


class Menu():
    def __init__(self, game_function):
        self.menu_layout = pygame_menu.Menu(
            300, 300, 'Snake Game', theme=pygame_menu.themes.THEME_DARK)
        self.menu_start_btn = self.menu_layout.add_button(
            'Play', game_function)
        self.menu_start_btn = self.menu_layout.add_button(
            'Quit', pygame_menu.events.EXIT)

    def show_menu(self, screen):
        self.menu_layout.mainloop(screen)
