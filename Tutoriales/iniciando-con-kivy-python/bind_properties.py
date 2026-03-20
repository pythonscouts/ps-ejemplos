from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class BindPropertiesApp(App):
    def build(self):
        self.title = "Enlazar propiedades Kivy"
        Window.size = (320, 220)

        root = BoxLayout(orientation="vertical", padding=20, spacing=10)

        entry = TextInput(hint_text="Escribe algo aquí...", multiline=False)
        display = Label(text="")

        def on_text(instance, value):
            display.text = f"Escribiste: '{value}'"

        entry.bind(text=on_text)

        root.add_widget(entry)
        root.add_widget(display)

        return root


BindPropertiesApp().run()
