class Player():
    def __init__(self, name):
        self.player_score = 0
        self.player_name = name

    def increase_score(self):
        self.player_score += 1

    def __str__(self):
        return f'Score: {self.player_score} Name: {self.player_name} '
