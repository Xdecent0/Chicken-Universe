import random
from tkinter import PhotoImage
from PIL import Image, ImageTk
from Data.GameData import GameData

game_data = GameData()
game_data.load()
class Player:
    def __init__(self, canvas, color, outline_color):
        self.canvas = canvas
        self.player = None
        self.lives = game_data.lives
        self.score = 0
        self.color = game_data.player_color
        self.outline_color = game_data.outline_color
        self.dy = 0
        self.dx = 0

    def move_up(self, event):
        if self.canvas.coords(self.player)[1] > 0:
            self.dy = -20
        else:
            self.dy = 0
    
    def move_left(self, event):
        if self.canvas.coords(self.player)[0] > 0:
            self.dx = -20
        else:
            self.dx = 0

    def move_right(self, event):
        if self.canvas.coords(self.player)[2] < 900:
            self.dx = 20
        else:
            self.dx = 0

    def move_down(self, event):
        if self.canvas.coords(self.player)[3] < 600:
            self.dy = 20
        else:
            self.dy = 0

    def update(self):
        self.canvas.move(self.player, self.dx, self.dy)
        self.dx = 0
        self.dy = 0

    
    def create_player(self, x1, y1, x2, y2, fill_color, outline_color, outline_width):
        self.player = self.canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color, outline=outline_color, width=outline_width)

class Obstacle:
    def __init__(self, canvas):
        self.canvas = canvas
        self.obstacle = None
        self.speed = 15
        self.height = 15
        self.image = self.load_obstacle_image()
        self.create_obstacle()

    def load_obstacle_image(self):
        image_number = random.randint(1, 5)
        image_path = f"./Game/Assets/Obstacle/{image_number}.png"
        image = Image.open(image_path)
        photo_image = ImageTk.PhotoImage(image)
        return photo_image

    def create_obstacle(self):
        x = 900
        y = random.randint(10, 500 - self.height)
        self.obstacle = self.canvas.create_image(x, y, image=self.image, anchor="nw")

    def move(self):
        self.canvas.move(self.obstacle, -self.speed, 0)

class Coin:
    def __init__(self, canvas):
        self.canvas = canvas
        self.coin = None
        self.speed = 15
        self.image = self.load_coin_image()
        self.create_coin()

    def load_coin_image(self):
        image_path = f"./Game/Assets/Obstacle/coin.png"
        image = Image.open(image_path)
        photo_image = ImageTk.PhotoImage(image)
        return photo_image

    def create_coin(self):
        x = 1000
        y = random.randint(10, 500)
        self.coin = self.canvas.create_image(x, y, image=self.image, anchor="nw")

    def move(self):
        self.canvas.move(self.coin, -self.speed, 0)

