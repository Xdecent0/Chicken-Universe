import tkinter as tk
import random
from Data.GameData import GameData

AVAILABLE_COLORS = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange", "Pink", "Cyan", "Magenta", "Brown", "Lime", "Teal", "Lavender", "Maroon", "Navy", "Olive", "Gold", "Indigo", "Silver", "Turquoise", "Violet", "Beige", "Crimson", "Plum"]

game_data = GameData()
game_data.load()

class MainMenu:
    def __init__(self, root, start_game_callback):
        self.root = root
        self.root.title("Main Menu")

        self.start_game_callback = start_game_callback

        self.main_frame = tk.Frame(root, bg="purple")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        button_width = 200
        button_height = 60
        button_font = ("Helvetica", 16)

        left_frame = tk.Frame(self.main_frame, bg="purple")
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        game_data.load()

        self.create_labels(left_frame, game_data.highscore, game_data.coins)

        right_frame = tk.Frame(self.main_frame, bg="purple")
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        start_icon = tk.PhotoImage(file="./Game/Assets/icons/play.png")
        settings_icon = tk.PhotoImage(file="./Game/Assets/icons/shop.png")
        reset_icon = tk.PhotoImage(file="./Game/Assets/icons/reset.png")
        exit_icon = tk.PhotoImage(file="./Game/Assets/icons/exit.png")

        self.create_button(right_frame, "Start Game", self.start_game, start_icon, button_width, button_height)
        self.create_button(right_frame, "Shop", self.open_shop, settings_icon, button_width, button_height)
        self.create_button(right_frame, "Reset Progress", self.reset_player, reset_icon, button_width, button_height)
        self.create_button(right_frame, "Exit", root.quit, exit_icon, button_width, button_height)

    def create_labels(self, frame, highscore, coins):
        labels_frame = tk.Frame(frame, bg="darkviolet", bd=8, relief=tk.GROOVE)
        labels_frame.pack(padx=20, pady=90, fill=tk.BOTH)

        highscore_icon = tk.PhotoImage(file="./Game/Assets/icons/score.png")
        coin_icon = tk.PhotoImage(file="./Game/Assets/Obstacle/coin.png")

        self.highscore_label = tk.Label(labels_frame, text=f"Highscore: {highscore}", font=("Helvetica", 24), fg="black", bg="darkviolet", image=highscore_icon, compound="left")
        self.highscore_label.image = highscore_icon
        self.highscore_label.pack(pady=90, fill=tk.BOTH)

        self.coins_label = tk.Label(labels_frame, text=f"Coins: {coins}", font=("Helvetica", 24), fg="black", bg="darkviolet", image=coin_icon, compound="left")
        self.coins_label.image = coin_icon
        self.coins_label.pack(pady=90, fill=tk.BOTH)

    def create_button(self, frame, text, command, image, width, height):
        button = tk.Button(frame, text=text, command=command, width=width, height=height, font=("Helvetica", 16), image=image, compound="left", bg = "maroon4", bd = 5, highlightcolor = "black")
        button.image = image
        button.pack(pady=90)

    def start_game(self):
        game_data.load()
        self.main_frame.destroy()
        self.start_game_callback()

    def reset_player(self):
        game_data.reset()
        game_data.save()
        self.update_player()

    def update_player(self):
        game_data.load()
        self.highscore_label.config(text=f"Highscore: {game_data.highscore}")
        self.coins_label.config(text=f"Coins: {game_data.coins}")

    def open_shop(self):
        self.main_frame.destroy()
        shop_menu = ShopMenu(self.root, self.return_to_main_menu, self.start_game_callback)

    def return_to_main_menu(self):
        self.root.title("Main Menu")
        for widget in self.root.winfo_children():
            widget.destroy()

        main_menu = MainMenu(self.root, self.start_game_callback)

class ShopMenu:
    def __init__(self, root, return_callback, start_game_callback):
        self.root = root
        self.root.title("Shop")

        self.return_callback = return_callback
        self.start_game_callback = start_game_callback

        self.shop_frame = tk.Frame(root, bg="purple")
        self.shop_frame.pack(fill=tk.BOTH, expand=True)
        
        back_icon = tk.PhotoImage(file="./Game/Assets/icons/back.png")
        back_button = tk.Button(self.shop_frame, image=back_icon, command=self.return_to_main_menu, bg = "mediumpurple4", bd = 5, highlightcolor = "black")
        back_button.image = back_icon
        back_button.pack(anchor="nw", padx=10, pady=10)
        
        game_data = GameData()
        game_data.load()
        coin_icon = tk.PhotoImage(file="./Game/Assets/Obstacle/coin.png")
        coin_label = tk.Label(self.shop_frame, text=f"Coins: {game_data.coins}", font=("Helvetica", 16), image=coin_icon, compound="left", bg="purple")
        coin_label.image = coin_icon
        coin_label.pack(anchor="nw", padx=20, pady=20)
        self.coin_label = coin_label

        self.create_shop_buttons()

    def return_to_main_menu(self):
        self.root.title("Main Menu")
        for widget in self.root.winfo_children():
            widget.destroy()

        main_menu = MainMenu(self.root, self.start_game_callback)

    def create_shop_button(self, frame, text, command, image):
        button_width = 400
        button_height = 60

        button = tk.Button(frame, text=text, command=command, width=button_width, height=button_height, font=("Helvetica", 16), image=image, compound="left", bg = "maroon3", bd = 5, highlightcolor = "black")
        button.image = image
        button.pack(pady=20)
        return button

    def create_shop_buttons(self):
        buy_extra_life_icon = tk.PhotoImage(file="./Game/Assets/icons/heart.png")
        add_100_coins_icon = tk.PhotoImage(file="./Game/Assets/Obstacle/coin.png")
        buy_random_body_color_icon = tk.PhotoImage(file="./Game/Assets/icons/random.png")
        buy_random_outline_color_icon = tk.PhotoImage(file="./Game/Assets/icons/random.png")

        extra_life_price = 50
        random_body_color_price = 30
        random_outline_color_price = 40

        buttons_frame = tk.Frame(self.shop_frame, bg="purple")
        buttons_frame.pack()

        self.create_shop_button(buttons_frame, "Add 100 Coins (Cheats)", self.add_100_coins, add_100_coins_icon).pack(side="top", pady=20)
        self.create_shop_button(buttons_frame, f"Buy Random Body Color ({random_body_color_price} Coins)", self.buy_random_body_color, buy_random_body_color_icon).pack(side="top", pady=20)
        self.create_shop_button(buttons_frame, f"Buy Random Outline Color ({random_outline_color_price} Coins)", self.buy_random_outline_color, buy_random_outline_color_icon).pack(side="top", pady=20)

        self.buy_extra_life_button = self.create_shop_button(buttons_frame, f"Buy Extra Life ({extra_life_price} Coins)", self.buy_extra_life, buy_extra_life_icon)
        if game_data.lives >= 3:
            self.buy_extra_life_button.config(state=tk.DISABLED, text="Not Available")
        self.buy_extra_life_button.pack(side="top", pady=20)



    def buy_extra_life(self):
        game_data.load()
        current_coins = game_data.coins
        life_price = 50

        if current_coins >= life_price and game_data.lives < 3:
            current_coins -= life_price
            game_data.lives += 1
            game_data.coins = current_coins
            game_data.save()
            self.coin_label.config(text=f"Coins: {current_coins}")
        elif game_data.lives >= 3:
            self.buy_extra_life_button.config(state=tk.DISABLED, text="Not Available")

    def add_100_coins(self):
        game_data.load()
        current_coins = game_data.coins
        current_coins += 100
        game_data.coins = current_coins
        game_data.save()

        self.coin_label.config(text=f"Coins: {current_coins}")

    def buy_random_body_color(self):
        game_data.load()
        current_coins = game_data.coins
        body_color_price = 30

        if current_coins >= body_color_price:
            current_coins -= body_color_price
            game_data.coins = current_coins
            new_body_color = random.choice(AVAILABLE_COLORS)
            while new_body_color == game_data.player_color:
                new_body_color = random.choice(AVAILABLE_COLORS)
            game_data.player_color = new_body_color
            game_data.save()
            self.coin_label.config(text=f"Coins: {current_coins}")

    def buy_random_outline_color(self):
        game_data.load()
        current_coins = game_data.coins
        outline_color_price = 40

        if current_coins >= outline_color_price:
            current_coins -= outline_color_price
            game_data.coins = current_coins
            new_outline_color = random.choice(AVAILABLE_COLORS)
            while new_outline_color == game_data.outline_color:
                new_outline_color = random.choice(AVAILABLE_COLORS)
            game_data.outline_color = new_outline_color
            game_data.save()
            self.coin_label.config(text=f"Coins: {current_coins}")


