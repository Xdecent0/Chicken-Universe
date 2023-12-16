# import pickle

# class GameData:
#     _instance = None

#     def __new__(cls):
#         if cls._instance is None:
#             cls._instance = super(GameData, cls).__new__(cls)
#             cls._instance._initialize()
#         return cls._instance

#     def _initialize(self):
#         self.highscore = 0
#         self.coins = 0
#         self.lives = 1
#         self.player_color = "purple"
#         self.outline_color = "black"
#         self.name = "Player"

#     def save(self):
#         with open("./Game/Scripts/Data/game_data.pkl", "wb") as file:
#             pickle.dump(self, file)

#     def load(self):
#         try:
#             with open("./Game/Scripts/Data/game_data.pkl", "rb") as file:
#                 game_data = pickle.load(file)
#                 self.highscore = game_data.highscore
#                 self.coins = game_data.coins
#                 self.lives = game_data.lives
#                 self.player_color = game_data.player_color
#                 self.outline_color = game_data.outline_color
#                 self.name = game_data.name
#         except (FileNotFoundError, EOFError):
#             self._initialize()

#     def reset(self):
#         current_name = self.name
#         self._initialize()
#         self.name = current_name



import pickle

class Player:
    def __init__(self, name):
        self.name = name
        self.highscore = 0
        self.coins = 0
        self.lives = 1
        self.player_color = "purple"
        self.outline_color = "black"

class GameData:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GameData, cls).__new__(cls)
            cls._instance._initialize()
        return cls._instance

    def _initialize(self):
        self.players = {
            "Player1": Player("Player1"),
            "Player2": Player("Player2"),
            "Player3": Player("Player3")
        }
        self.current_player = "Player1"

    def save(self):
        with open("./Game/Scripts/Data/game_data.pkl", "wb") as file:
            pickle.dump(self, file)

    def load(self):
        try:
            with open("./Game/Scripts/Data/game_data.pkl", "rb") as file:
                game_data = pickle.load(file)
                self.players = game_data.players
                self.current_player = game_data.current_player
        except (FileNotFoundError, EOFError):
            self._initialize()

    def switch_player(self, player_name):
        if player_name in self.players:
            self.current_player = player_name

    def get_current_player_info(self):
        return self.players[self.current_player].__dict__

    def get_coins(self):
        return self.players[self.current_player].coins

    def get_highscore(self):
        return self.players[self.current_player].highscore

    def get_lives(self):
        return self.players[self.current_player].lives

    def get_name(self):
        return self.players[self.current_player].name

    def get_player_color(self):
        return self.players[self.current_player].player_color

    def get_outline_color(self):
        return self.players[self.current_player].outline_color

    def set_coins(self, value):
        self.players[self.current_player].coins = value

    def set_highscore(self, value):
        self.players[self.current_player].highscore = value

    def set_lives(self, value):
        self.players[self.current_player].lives = value

    def set_name(self, value):
        self.players[self.current_player].name = value

    def set_player_color(self, value):
        self.players[self.current_player].player_color = value

    def set_outline_color(self, value):
        self.players[self.current_player].outline_color = value
    
    def reset(self):
        current_player = self.players[self.current_player]
        current_player.highscore = 0
        current_player.coins = 0
        current_player.lives = 1
        current_player.player_color = "purple"
        current_player.outline_color = "black"


