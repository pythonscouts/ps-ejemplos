from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class ButtonsApp(App):
    def build(self):
        self.title = "Botones Kivy"
        Window.size = (200, 200)
        layout = BoxLayout(orientation="vertical", padding=20, spacing=10)

        for text in ["Ok", "Cancelar", "Aplicar", "Sí", "No", "Cerrar"]:
            button = Button(text=text)
            layout.add_widget(button)

        return layout


ButtonsApp().run()
