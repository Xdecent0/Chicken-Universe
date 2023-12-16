import tkinter as tk
from tkinter import Menu, simpledialog
from Data.GameData import GameData

game_data = GameData()
game_data.load()

class AppMenu:
    def __init__(self, root, start_game_callback):
        self.root = root
        self.start_game_callback = start_game_callback
        self.create_menu()

    def create_menu(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)

        # File Menu
        file_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)

        file_menu.add_command(label="Save Data", command=self.save_data)

        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.destroy)

        # Player Menu
        player_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Player", menu=player_menu)

        self.update_player_menu(player_menu)

        # Info Menu
        info_menu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Info", menu=info_menu)

        info_menu.add_command(label="Get Information", command=self.show_info)

    def save_data(self):
        game_data.save()

    def update_player_menu(self, player_menu):
        player_menu.delete(0, tk.END)  # Удаляем все элементы из меню

        player_menu.add_command(label=f"Player Name: {game_data.name}", state=tk.DISABLED)

        player_menu.add_separator()

        player_menu.add_command(label="Change Name", command=self.change_name_dialog)

    def change_name_dialog(self):
        new_name = simpledialog.askstring("Change Name", "Enter new player name:")
        if new_name:
            game_data.name = new_name
            self.create_menu()
            game_data.save()

    def show_info(self):
        info_text = "Info:\n\n" \
                    "Dodge obstacles, collect coins, and beat your record.\n\n" \
                    "Controls:\n" \
                    "Up arrow - move up\n" \
                    "Down arrow - move down\n" \
                    "Left arrow - move left\n" \
                    "Right arrow - move right"

        tk.messagebox.showinfo("Info", info_text)