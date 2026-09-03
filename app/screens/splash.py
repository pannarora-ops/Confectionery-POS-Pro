from kivy.clock import Clock
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_file("app/kv/splash.kv")


class SplashScreen(Screen):

    def on_enter(self, *args):
        Clock.schedule_once(self.goto_login, 2)

    def goto_login(self, dt):
        self.manager.current = "login"