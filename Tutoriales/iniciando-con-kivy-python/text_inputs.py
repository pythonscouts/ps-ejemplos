from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput


class TextInputApp(App):
    def build(self):
        self.title = "Campos de texto Kivy"
        Window.size = (250, 180)
        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)
        for text in ["Nombre", "Usuario", "Contraseña"]:
            entry = TextInput(
                hint_text=text,
                multiline=False,
            )
            layout.add_widget(entry)
        return layout


TextInputApp().run()
