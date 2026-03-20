from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.label import Label


class CheckBoxApp(App):
    def build(self):
        self.title = "Botones de opción Kivy"
        Window.size = (250, 150)
        Window.clearcolor = (1, 1, 1, 1)

        options = [
            "Recibir notificaciones",
            "Aceptar términos y condiciones",
            "Suscribirse al boletín",
        ]

        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        for option in options:
            row = BoxLayout(orientation="horizontal", spacing=8)
            row.add_widget(CheckBox(size_hint_x=None, width=30))

            label = Label(
                text=option,
                color=(0, 0, 0, 1),
                size_hint_x=None,
            )
            label.texture_update()
            label.width = label.texture_size[0]

            row.add_widget(label)
            layout.add_widget(row)

        return layout


CheckBoxApp().run()
