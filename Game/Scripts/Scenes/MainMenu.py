import tkinter as tk
from Data.GameData import GameData

game_data = GameData()

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

        left_frame = tk.Frame(self.main_frame, bg="purple")
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        game_data.load()

        self.highscore_label = tk.Label(left_frame, text=f"Highscore: {game_data.highscore}", font=("Helvetica", 24), bg="purple", fg="white")
        self.highscore_label.pack(padx=20, pady=50, fill=tk.BOTH)

        self.coins_label = tk.Label(left_frame, text=f"Coins: {game_data.coins}", font=("Helvetica", 24), bg="purple", fg="white")
        self.coins_label.pack(padx=20, fill=tk.BOTH)


        right_frame = tk.Frame(self.main_frame, bg="purple")
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        start_icon = tk.PhotoImage(file="./Assets/icons/play.png")
        settings_icon = tk.PhotoImage(file="./Assets/icons/shop.png")
        reset_icon = tk.PhotoImage(file="./Assets/icons/reset.png")
        exit_icon = tk.PhotoImage(file="./Assets/icons/exit.png")

        start_button = tk.Button(right_frame, text="Start Game", command=self.start_game, width=button_width, height=button_height, font=button_font, image=start_icon, compound="left")
        start_button.image = start_icon
        start_button.pack(side=tk.TOP, pady=90)

        settings_button = tk.Button(right_frame, text="Shop", command=self.open_settings, width=button_width, height=button_height, font=button_font, image=settings_icon, compound="left")
        settings_button.image = settings_icon
        settings_button.pack(side=tk.TOP, pady=90)

        reset_button = tk.Button(right_frame, text="Reset Progress", command=self.reset_player, width=button_width, height=button_height, font=button_font, image=reset_icon, compound="left")
        reset_button.image = reset_icon
        reset_button.pack(side=tk.TOP, pady=90)

        exit_button = tk.Button(right_frame, text="Exit", command=root.quit, width=button_width, height=button_height, font=button_font, image=exit_icon, compound="left")
        exit_button.image = exit_icon
        exit_button.pack(side=tk.TOP, pady=90)

    def start_game(self):
        self.main_frame.destroy()
        self.start_game_callback()

    def reset_player(self):
        game_data.reset()
        game_data.save()
        self.update_player()

    def update_player(self):
        self.highscore_label.config(text=f"Highscore: {game_data.highscore}")
        self.coins_label.config(text=f"Coins: {game_data.coins}")

    def open_settings(self):
        pass

