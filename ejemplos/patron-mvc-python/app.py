from model import Model
from view import Window


class Controller:
    def __init__(self, model, view):
        self._model = model
        self._view = view
        self._view.greetings_button["command"] = self._greet

    def run(self):
        self._view.mainloop()

    def _greet(self):
        self._view.show_greeting(greeting=self._model.get_greeting())


if __name__ == "__main__":
    controller = Controller(model=Model(), view=Window())
    controller.run()
