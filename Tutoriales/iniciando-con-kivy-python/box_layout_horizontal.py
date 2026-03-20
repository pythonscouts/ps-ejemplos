from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button


class BoxLayoutApp(App):
    def build(self):
        self.title = "Disposición horizontal Kivy"
        Window.size = (300, 100)

        root = BoxLayout(orientation="horizontal", padding=20, spacing=10)
        root.add_widget(Button(text="Izquierda"))
        root.add_widget(Button(text="Centro"))
        root.add_widget(Button(text="Derecha"))

        return root


BoxLayoutApp().run()
