import tkinter as tk
from tkinter import ttk

class ActionWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Action Window")
        self.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):
        # Dropdown menu
        self.perform_mode = tk.StringVar(self)
        self.perform_mode.set("Select Perform Mode")
        options = [
            "Single shoot with a pistol",
            "Shoot using a rifle",
            "Shoot through machine gun",
            "Blast like a bomb"
        ]
        dropdown = ttk.Combobox(self, textvariable=self.perform_mode, values=options)
        dropdown.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Form fields
        form_labels = ["Request URI", "Header", "Payload"]
        self.entries = {}
        for i, label in enumerate(form_labels):
            label_widget = tk.Label(self, text=label)
            label_widget.grid(row=i + 1, column=0, padx=10, pady=10, sticky="e")

            entry = tk.Entry(self)
            entry.grid(row=i + 1, column=1, padx=10, pady=10, sticky="w")

            self.entries[label.lower().replace(" ", "_")] = entry

        # Buttons
        submit_button = tk.Button(self, text="Submit", command=self.submit)
        submit_button.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        stop_button = tk.Button(self, text="Stop", command=self.stop)
        stop_button.grid(row=4, column=1, padx=10, pady=10, sticky="e")

        # Response area
        self.response_text = tk.Text(self, wrap="word")
        self.response_text.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

    def submit(self):
        # Process form data
        form_data = {}
        for field_name, entry in self.entries.items():
            form_data[field_name] = entry.get()

        perform_mode = self.perform_mode.get()
        # Do something with the form data and perform mode
        print(perform_mode, form_data)

    def stop(self):
        # Stop any ongoing actions
        pass
