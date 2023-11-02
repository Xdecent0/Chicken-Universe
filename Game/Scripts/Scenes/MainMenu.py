import tkinter as tk
from Data.GameData import GameData

class MainMenu:
    def __init__(self, root, start_game_callback):
        self.root = root
        self.root.title("Main Menu")
        self.root.attributes("-fullscreen", True) 

        self.start_game_callback = start_game_callback

        self.main_frame = tk.Frame(root, bg="purple")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        button_width = 200
        button_height = 60
        button_font = ("Helvetica", 16)

        left_frame = tk.Frame(self.main_frame, bg="purple")  # Левый фрейм с фоном такого же цвета
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        game_data = GameData()
        game_data.load()

        self.create_labels(left_frame, game_data.highscore, game_data.coins)

        right_frame = tk.Frame(self.main_frame, bg="purple")
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


        start_icon = tk.PhotoImage(file="./Assets/icons/play.png")
        settings_icon = tk.PhotoImage(file="./Assets/icons/shop.png")
        reset_icon = tk.PhotoImage(file="./Assets/icons/reset.png")
        exit_icon = tk.PhotoImage(file="./Assets/icons/exit.png")

        self.create_button(right_frame, "Start Game", self.start_game, start_icon, button_width, button_height)
        self.create_button(right_frame, "Shop", self.open_shop, settings_icon, button_width, button_height)
        self.create_button(right_frame, "Reset Progress", self.reset_player, reset_icon, button_width, button_height)
        self.create_button(right_frame, "Exit", root.quit, exit_icon, button_width, button_height)

    def create_labels(self, frame, highscore, coins):
        labels_frame = tk.Frame(frame, bg="darkviolet")
        labels_frame.pack(padx=20, pady=90, fill=tk.BOTH)

        highscore_icon = tk.PhotoImage(file="./Assets/icons/score.png")
        coin_icon = tk.PhotoImage(file="./Assets/Obstacle/coin.png")

        self.highscore_label = tk.Label(labels_frame, text=f"Highscore: {highscore}", font=("Helvetica", 24), fg="black", bg="darkviolet", image=highscore_icon, compound="left")
        self.highscore_label.image = highscore_icon
        self.highscore_label.pack(pady=90, fill=tk.BOTH)

        self.coins_label = tk.Label(labels_frame, text=f"Coins: {coins}", font=("Helvetica", 24), fg="black", bg="darkviolet", image=coin_icon, compound="left")
        self.coins_label.image = coin_icon
        self.coins_label.pack(pady=90, fill=tk.BOTH)

    def create_button(self, frame, text, command, image, width, height):
        button = tk.Button(frame, text=text, command=command, width=width, height=height, font=("Helvetica", 16), image=image, compound="left")
        button.image = image
        button.pack(pady=90)

    def start_game(self):
        self.main_frame.destroy()
        self.start_game_callback()

    def reset_player(self):
        game_data = GameData()
        game_data.reset()
        game_data.save()
        self.update_player()

    def update_player(self):
        game_data = GameData()
        game_data.load()
        self.highscore_label.config(text=f"Highscore: {game_data.highscore}")
        self.coins_label.config(text=f"Coins: {game_data.coins}")

    def open_shop(self):
        pass
