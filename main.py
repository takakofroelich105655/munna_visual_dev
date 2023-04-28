import tkinter as tk
import json
from application import Application
from login_form import LoginForm
from register_form import RegisterForm
from response_panel import ResponsePanel
from action_window import ActionWindow

def load_config():
    with open('config.json') as config_file:
        return json.load(config_file)

app_config = load_config()

app = Application(config=app_config)

# Create UI components
login_form = LoginForm(app, app_config)
register_form = RegisterForm(app, app_config)
response_panel = ResponsePanel(app)

# Perform some Python code
# Here you can add your Python code that needs to be executed

app.mainloop()
