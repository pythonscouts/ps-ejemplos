import tkinter as tk


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("MVC Demo")
        self.geometry("160x70")
        self.greetings_label = tk.Label(text="Hola!")
        self.greetings_label.pack()
        self.greetings_button = tk.Button(text="Saludar")
        self.greetings_button.pack()

    def show_greeting(self, greeting):
        self.greetings_label["text"] = greeting
