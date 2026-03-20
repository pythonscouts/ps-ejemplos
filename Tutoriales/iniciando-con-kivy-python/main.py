from kivy.app import App
from kivy.core.window import Window
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout


class CounterApp(App):
    def build(self):
        self.title = "KV language Kivy"
        Window.size = (300, 200)

        return RootWidget()


class RootWidget(BoxLayout):
    count = NumericProperty(0)

    def increment(self):
        self.count += 1


CounterApp().run()
