from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.slider import Slider


class SliderApp(App):
    def build(self):
        self.title = "Selector deslizante Kivy"
        Window.size = (300, 150)

        root = BoxLayout(orientation="vertical", padding=20, spacing=10)

        label = Label(text="Valor: 0")
        slider = Slider(min=0, max=100, value=0)

        def on_value(instance, value):
            label.text = f"Valor: {int(value)}"

        slider.bind(value=on_value)

        root.add_widget(label)
        root.add_widget(slider)
        return root


SliderApp().run()
