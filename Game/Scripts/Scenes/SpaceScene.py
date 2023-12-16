import tkinter as tk
from Scenes.MainMenu import MainMenu
from GameObjects.GameObject import Player, Obstacle, Coin
from Data.GameData import GameData
from MenuUtils.menuUtils import AppMenu
import random

game_data = GameData()
game_data.load()

def create_label(parent, text, font, image, compound, padx, pady):
        label = tk.Label(parent, text=text, font=font, image=image, compound=compound)
        label.image = image
        label.pack(side="left", padx=padx, pady=pady)
        return label


class FlyingObjectGame:
    def __init__(self, root, start_game_callback):
        self.root = root
        self.start_game_callback = start_game_callback
        self.canvas = tk.Canvas(root, width=900, height=600, bg="lightblue")
        self.canvas.pack()

        self.player = Player(self.canvas, game_data.get_player_color(), game_data.get_outline_color())
        self.player.create_player(160, 120, 200, 180, game_data.get_player_color(), game_data.get_outline_color(), 4)

        root.bind("<Up>", self.player.move_up)  
        root.bind("<Right>", self.player.move_right)
        root.bind("<Left>", self.player.move_left)
        root.bind("<Down>", self.player.move_down)

        root.focus_set()

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(side="top")

        score_icon = tk.PhotoImage(file="./Game/Assets/icons/score.png")
        heart_icon = tk.PhotoImage(file="./Game/Assets/icons/heart.png")
        back_icon = tk.PhotoImage(file="./Game/Assets/icons/back.png")
        coin_icon = tk.PhotoImage(file="./Game/Assets/Obstacle/coin.png")

        self.back_button = tk.Button(self.button_frame, text="Back", command=self.go_back, width=40, height=40, image=back_icon, font=("Helvetica", 12), bg = "mediumpurple4", bd = 5, highlightcolor = "black")
        self.back_button.image = back_icon
        self.back_button.pack(side="left", padx=10, pady=10)

        self.score = 0
        self.score_label = create_label(self.button_frame, f"Score: {self.score}", ("Helvetica", 18), score_icon, "left", 10, 10)
        self.lives_label = create_label(self.button_frame, f"Lives: {game_data.get_lives()}", ("Helvetica", 18), heart_icon, "left", 10, 10)
        self.coins_label = create_label(self.button_frame, f"Coins: {game_data.get_coins()}", ("Helvetica", 18), coin_icon, "left", 10, 10)

        self.obstacles = []
        self.coins = []
        self.game_over = False
        self.spawn_object()

    def go_back(self):
        game_data.save()
        game_data.load()
        main_menu = MainMenu(self.root.winfo_toplevel(), self.start_game_callback)
        self.root.destroy()


    def spawn_object(self):
        if not self.game_over:
            probability = random.randint(1, 4)
            if probability == 1:
                coin = Coin(self.canvas)
                self.coins.append(coin)
            else:
                obstacle = Obstacle(self.canvas)
                self.obstacles.append(obstacle)
                self.player.score += 1
                self.score_label.config(text=f"Score: {self.player.score}")
            self.root.after(1000, self.spawn_object)

    def move_obstacles(self):
        if not self.game_over:
            for obstacle in self.obstacles:
                obstacle.move()
                obstacle_coords = self.canvas.coords(obstacle.obstacle)
                if obstacle_coords[2] < 0:
                    self.canvas.delete(obstacle.obstacle)
                    self.obstacles.remove(obstacle)
            if not self.game_over:
                self.root.after(50, self.move_obstacles)

    def move_obstacles_towards_player(self):
        if not self.game_over:
            player_coords = self.canvas.coords(self.player.player)
            for obstacle in self.obstacles:
                if obstacle.obstacle:
                    obstacle.move()
                    obstacle_coords = self.canvas.coords(obstacle.obstacle)
                    if obstacle_coords and len(obstacle_coords) > 2 and obstacle_coords[2] < 0:
                        self.canvas.delete(obstacle.obstacle)
                        self.obstacles.remove(obstacle)
                        self.score += 1
            for coin in self.coins:
                if coin.coin:
                    coin.move()
            if not self.game_over:
                self.root.after(50, self.move_obstacles_towards_player)

    def update(self):
        if not self.game_over:
            self.player.update()
            self.check_collision()
            self.collect_coins()
            if not self.game_over:
                self.root.after(50, self.update)

    def check_collision(self):
        player_coords = self.canvas.coords(self.player.player)
        player_box = self.canvas.bbox(self.player.player)
        for obstacle in self.obstacles:
            obstacle_coords = self.canvas.coords(obstacle.obstacle)
            obstacle_box = self.canvas.bbox(obstacle.obstacle)
            if player_box and obstacle_box and self.is_collision(player_box, obstacle_box):
                if self.player.lives == 1:
                    self.player.lives -= 1
                    self.lives_label.config(text=f"Lives: {self.player.lives}")
                    self.game_over = True
                    self.end_game()
                else:
                    self.canvas.delete(obstacle.obstacle)
                    self.obstacles.remove(obstacle)
                    self.player.lives -= 1
                    self.lives_label.config(text=f"Lives: {self.player.lives}")

    def collect_coins(self):
        player_coords = self.canvas.coords(self.player.player)
        player_box = self.canvas.bbox(self.player.player)
        collected_coins = []

        for coin in self.coins:
            coin_coords = self.canvas.coords(coin.coin)
            coin_box = self.canvas.bbox(coin.coin)
            if player_box and coin_box and self.is_collision(player_box, coin_box):
                collected_coins.append(coin)

        for coin in collected_coins:
            self.canvas.delete(coin.coin)
            self.coins.remove(coin)
            current_coins = game_data.get_coins()
            game_data.set_coins(current_coins + 1)
            
        self.coins_label.config(text=f"Coins: {game_data.get_coins()}")

    def is_collision(self, box1, box2):
        x1, y1, x2, y2 = box1
        x3, y3, x4, y4 = box2
        return not (x2 < x3 or x4 < x1 or y2 < y3 or y4 < y1)

    def end_game(self):
        global highscore
        self.game_over = True
        if self.player.score > game_data.get_highscore():
            game_data.set_highscore(self.player.score)
        self.canvas.delete("all")
        self.canvas.create_text(450, 250, text="You Lost", font=("Helvetica", 36), fill="red")
        self.canvas.create_text(450, 300, text=f"Highscore: {game_data.get_highscore()}", font=("Helvetica", 24), fill="blue")