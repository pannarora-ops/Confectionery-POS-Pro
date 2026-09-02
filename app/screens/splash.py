from kivy.clock import Clock
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel


class SplashScreen(MDScreen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.add_widget(
            MDLabel(
                text="Confectionery POS Pro\nVersion 0.1",
                halign="center",
            )
        )

    def on_enter(self):
        Clock.schedule_once(self.goto_login, 2)

    def goto_login(self, dt):
        self.manager.current = "login"