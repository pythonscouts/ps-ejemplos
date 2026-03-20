from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class ButtonsCallbacksApp(App):
    def build(self):
        self.title = "Enlazar eventos Kivy"
        Window.size = (220, 220)

        root = BoxLayout(orientation="vertical", padding=20, spacing=10)

        self.label = Label(
            text="Presionaste: ...",
        )
        root.add_widget(self.label)

        def on_press(instance):  # Callback
            self.label.text = f"Presionaste: {instance.text}"

        for text in ["Ok", "Cancelar", "Aplicar"]:
            button = Button(text=text)
            button.bind(on_press=on_press)  # Enlace
            root.add_widget(button)

        return root


ButtonsCallbacksApp().run()
