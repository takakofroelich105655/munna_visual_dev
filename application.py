import tkinter as tk
from action_window import ActionWindow

class Application(tk.Tk):
    def __init__(self, config=None):
        super().__init__()
        self.app_config = config  # Change the name here
        self.title("My Python Application")
        self.geometry("800x600")
        self.configure(bg=self.app_config['parts']['header']['background_color'])  # Update the reference

        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)
        self.create_menu()

    def create_menu(self):
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)

        tools_menu = tk.Menu(self.menu_bar, tearoff=0)
        tools_menu.add_command(label="Open Action Window", command=self.open_action_window)

        self.menu_bar.add_cascade(label="File", menu=file_menu)
        self.menu_bar.add_cascade(label="Tools", menu=tools_menu)

    def new_file(self):
        pass

    def open_file(self):
        pass

    def save_file(self):
        pass

    def open_action_window(self):
        action_window = ActionWindow(self)
