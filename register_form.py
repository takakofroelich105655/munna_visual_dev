import tkinter as tk

class RegisterForm(tk.Frame):
    def __init__(self, master, config):
        super().__init__(master)
        self.config = config
        self.grid(row=0, column=1, sticky="nsew")

        self.create_widgets()

    def create_widgets(self):
        form_config = self.config['forms']['register']
        fields = form_config['fields']

        row = 0
        for field in fields:
            label = tk.Label(self, text=field['label'])
            label.grid(row=row, column=0, padx=10, pady=10, sticky="e")

            entry = tk.Entry(self)
            entry.grid(row=row, column=1, padx=10, pady=10, sticky="w")
            row += 1

        register_button = tk.Button(self, text="Register", command=self.register)
        register_button.grid(row=row, column=1, padx=10, pady=10, sticky="w")

    def register(self):
        pass
