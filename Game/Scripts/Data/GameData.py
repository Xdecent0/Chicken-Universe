import pickle

class GameData:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GameData, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.highscore = 0
        self.coins = 0
        self.lives = 1
        self.player_color = "purple"
        self.outline_color = "black"

    def save(self):
        with open("./Game/Scripts/Data/game_data.pkl", "wb") as file:
            pickle.dump(self, file)

    def load(self):
        try:
            with open("./Game/Scripts/Data/game_data.pkl", "rb") as file:
                game_data = pickle.load(file)
                self.highscore = game_data.highscore
                self.coins = game_data.coins
                self.lives = game_data.lives
                self.player_color = game_data.player_color
                self.outline_color = game_data.outline_color
        except (FileNotFoundError, EOFError):
            self._initialize()

    def reset(self):
        self._initialize()
