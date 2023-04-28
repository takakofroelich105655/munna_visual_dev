import tkinter as tk

class ResponsePanel(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid(row=1, column=0, columnspan=2, sticky="nsew")

        label = tk.Label(self, text="Response:")
        label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.response_text = tk.Text(self, wrap="word")
        self.response_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
