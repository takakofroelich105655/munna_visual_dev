import tkinter as tk

class LoginForm(tk.Frame):
    def __init__(self, master, config):
        super().__init__(master)
        self.config = config
        self.grid(row=0, column=0, sticky="nsew")

        self.create_widgets()

    def create_widgets(self):
        form_config = self.config['forms']['login']
        fields = form_config['fields']

        row = 0
        for field in fields:
            label = tk.Label(self, text=field['label'])
            label.grid(row=row, column=0, padx=10, pady=10, sticky="e")

            entry = tk.Entry(self)
            entry.grid(row=row, column=1, padx=10, pady=10, sticky="w")
            row += 1

        login_button = tk.Button(self, text="Login", command=self.login)
        login_button.grid(row=row, column=1, padx=10, pady=10, sticky="w")

    def login(self):
        pass
