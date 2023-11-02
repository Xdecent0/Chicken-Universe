import tkinter as tk
from Scenes.MainMenu import MainMenu
from GameObjects.GameObject import Player, Obstacle, Coin
from Data.GameData import GameData

game_data = GameData()
game_data.load()

class FlyingObjectGame:
    def __init__(self, root, start_game_callback):
        self.root = root
        self.start_game_callback = start_game_callback
        self.canvas = tk.Canvas(root, width=1000, height=800, bg="lightblue")
        self.canvas.pack()

        self.player = Player(self.canvas, game_data.player_color, game_data.outline_color)
        self.player.create_player(160, 120, 200, 180, game_data.player_color, game_data.outline_color, 4)

        root.bind("<Up>", self.player.move_up)
        root.bind("<Down>", self.player.move_down)

        root.focus_set()

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(side="top")

        score_icon = tk.PhotoImage(file="./Assets/icons/score.png")
        heart_icon = tk.PhotoImage(file="./Assets/icons/heart.png")
        back_icon = tk.PhotoImage(file="./Assets/icons/back.png")
        coin_icon = tk.PhotoImage(file="./Assets/Obstacle/coin.png")

        self.back_button = tk.Button(self.button_frame, text="Back", command=self.go_back, width=40, height=40, image = back_icon, font=("Helvetica", 12))
        self.back_button.image = back_icon
        self.back_button.pack(side="left", padx=10, pady=10)

        self.score = 0
        self.score_label = tk.Label(self.button_frame, text=f"Score: {self.score}", font=("Helvetica", 18), image=score_icon, compound="left")
        self.score_label.image = score_icon
        self.score_label.pack(side="left", padx=10, pady=10)

        self.lives_label = tk.Label(self.button_frame, text="Lives: 2", font=("Helvetica", 18), image=heart_icon, compound="left")
        self.lives_label.image = heart_icon
        self.lives_label.pack(side="left", padx=10, pady=10)

        self.coins_label = tk.Label(self.button_frame, text=f"Coins: {game_data.coins}", font=("Helvetica", 18), image=coin_icon, compound="left")
        self.coins_label.image = coin_icon
        self.coins_label.pack(side="left", padx=10, pady=10)


        self.obstacles = []
        self.coins = []
        self.game_over = False
        self.spawn_obstacle()
        self.spawn_coin()

    def go_back(self):
        game_data.save()
        game_data.load()
        self.root.destroy()
        main_menu = MainMenu(root, start_game)

    def spawn_obstacle(self):
        if not self.game_over:
            obstacle = Obstacle(self.canvas)
            self.obstacles.append(obstacle)
            self.player.score += 1
            self.score_label.config(text=f"Score: {self.player.score}")
        self.root.after(1000, self.spawn_obstacle)
    
    def spawn_coin(self):
        if not self.game_over:
            coin = Coin(self.canvas)
            self.coins.append(coin)
            self.root.after(3300, self.spawn_coin)


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
            game_data.coins += 1
        self.coins_label.config(text=f"Coins: {game_data.coins}")


    def is_collision(self, box1, box2):
        x1, y1, x2, y2 = box1
        x3, y3, x4, y4 = box2
        return not (x2 < x3 or x4 < x1 or y2 < y3 or y4 < y1)

    def end_game(self):
        global highscore 
        self.game_over = True
        if self.player.score > game_data.highscore: 
            game_data.highscore = self.player.score  
        self.canvas.delete("all")
        self.canvas.create_text(500, 400, text="You Lost", font=("Helvetica", 36), fill="red")
        self.canvas.create_text(500, 450, text=f"Highscore: {game_data.highscore}", font=("Helvetica", 24), fill="blue")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1000x800")
    
    def start_game():
        game_frame = tk.Frame(root, width=1000, height=800)
        game_frame.place(relx=0.5, rely=0.5, anchor="center")
        game = FlyingObjectGame(game_frame, start_game)
        game.move_obstacles_towards_player()
        game.update()
    
    main_menu = MainMenu(root, start_game)
    root.mainloop()
