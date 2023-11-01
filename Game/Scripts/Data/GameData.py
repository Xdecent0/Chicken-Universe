import pickle

class GameData:
    def __init__(self):
        self.highscore = 0
        self.coins = 0
        self.player_color = "Purple"
        self.outline_color = "Black"

    def save(self):
        with open("game_data.pkl", "wb") as file:
            pickle.dump(self, file)

    def load(self):
        try:
            with open("game_data.pkl", "rb") as file:
                game_data = pickle.load(file)
                self.highscore = game_data.highscore
                self.coins = game_data.coins
                self.player_color = game_data.player_color
                self.outline_color = game_data.outline_color
        except (FileNotFoundError, EOFError):
            self.highscore = 0
            self.coins = 0
            self.player_color = "Purple"
            self.outline_color = "Black"
    
    def reset(self):
        self.highscore = 0
        self.coins = 0
        self.player_color = "Purple"
        self.outline_color = "Black"
