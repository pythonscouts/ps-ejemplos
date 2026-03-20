from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class BoxLayoutApp(App):
    def build(self):
        self.title = "Disposición vertical Kivy"
        Window.size = (300, 300)

        root = BoxLayout(orientation="vertical", padding=20, spacing=10)
        root.add_widget(Button(text="Arriba"))
        root.add_widget(Button(text="Centro"))
        root.add_widget(Button(text="Abajo"))

        return root


BoxLayoutApp().run()
