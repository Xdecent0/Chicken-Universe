import tkinter as tk

class MainMenu:
    def __init__(self, root, start_game_callback):
        self.root = root
        self.root.title("Main Menu")
        self.root.attributes("-fullscreen", True) 

        self.start_game_callback = start_game_callback

        self.main_frame = tk.Frame(root, bg="purple")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        button_width = 200
        button_height = 80
        button_font = ("Helvetica", 16)

        left_frame = tk.Frame(self.main_frame, bg="purple")
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        highscore_label = tk.Label(left_frame, text="Highscore: 1000", font=("Helvetica", 24), bg="purple", fg="white")
        highscore_label.pack(pady=(root.winfo_screenheight() - 4 * button_height) // 2, fill=tk.BOTH)

        coins_label = tk.Label(left_frame, text="Coins: $1000", font=("Helvetica", 24), bg="purple", fg="white")
        coins_label.pack(fill=tk.BOTH)

        right_frame = tk.Frame(self.main_frame, bg="purple")
        right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Создаем и отрисовываем четыре кнопки
        self.create_button(right_frame, "Start Game", self.start_game, button_width, button_height, button_font)
        self.create_button(right_frame, "Shop", self.open_settings, button_width, button_height, button_font)
        self.create_button(right_frame, "Reset Progress", self.reset_player, button_width, button_height, button_font)
        self.create_button(right_frame, "Exit", root.quit, button_width, button_height, button_font)

    def create_button(self, parent, text, command, width, height, font):
        button = tk.Button(parent, text=text, command=command, width=width, height=height, font=font)
        button.pack(pady=20, fill=tk.BOTH, expand=True)

    def start_game(self):
        self.main_frame.destroy()
        self.start_game_callback()

    def reset_player(self):
        # Действие, которое происходит при нажатии на кнопку сброса
        pass

    def open_settings(self):
        # Действие, которое происходит при нажатии на кнопку настроек
        pass


