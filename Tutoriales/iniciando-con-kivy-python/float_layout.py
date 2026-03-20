from kivy.app import App
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout


class FloatLayoutApp(App):
    def build(self):
        self.title = "Disposición flotante Kivy"
        Window.size = (600, 300)

        root = FloatLayout()

        button1 = Button(
            text="Centrado",
            size_hint=(0.5, 0.2),
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )

        button2 = Button(
            text="Esquina inferior derecha",
            size_hint=(0.3, 0.1),
            pos_hint={"right": 1, "y": 0},
        )
        root.add_widget(button1)
        root.add_widget(button2)
        return root


FloatLayoutApp().run()
