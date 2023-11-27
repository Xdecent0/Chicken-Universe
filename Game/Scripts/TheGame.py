import tkinter as tk
from Scenes.MainMenu import MainMenu
from Scenes.SpaceScene import FlyingObjectGame

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1024x720")

    def start_game():
        game_frame = tk.Frame(root, width=1024, height=720)
        game_frame.place(relx=0.5, rely=0.5, anchor="center")
        game = FlyingObjectGame(game_frame, start_game)
        game.move_obstacles_towards_player()
        game.update()

    main_menu = MainMenu(root, start_game)
    root.mainloop()
