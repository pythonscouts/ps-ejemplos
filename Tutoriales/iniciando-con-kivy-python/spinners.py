from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner


class SpinnerApp(App):
    def build(self):
        self.title = "Lista desplegable Kivy"
        Window.size = (250, 350)

        root = BoxLayout(orientation="vertical", padding=20, spacing=10)

        options = ("Kivy", "PyQt6", "PySide6", "Tkinter")
        base_text = "Framework GUI favorito"

        spinner = Spinner(
            text=base_text,
            values=options,
            size_hint_y=None,
            height=100,
        )
        root.add_widget(spinner)

        return root


SpinnerApp().run()
