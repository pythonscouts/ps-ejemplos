from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class GridLayoutApp(App):
    def build(self):
        self.title = "Disposición en cuadrícula Kivy"
        Window.size = (300, 300)

        root = GridLayout(cols=2, padding=20, spacing=10)

        for index in range(6):
            root.add_widget(Button(text=f"index={index}"))

        return root


GridLayoutApp().run()
