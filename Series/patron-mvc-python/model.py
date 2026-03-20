from random import choice


class Model:
    def __init__(self):
        self.greetings = (
            "Hola, Python!",
            "Hola, Mundo!",
            "Hola, Python Scouts!",
        )

    def get_greeting(self):
        return choice(self.greetings)
