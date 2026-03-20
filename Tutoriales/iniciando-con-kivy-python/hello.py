from kivy.app import App
from kivy.uix.label import Label


class HelloApp(App):
    def build(self):
        return Label(text="Hola, Mundo!")


HelloApp().run()
