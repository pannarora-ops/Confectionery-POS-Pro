from kivy.lang import Builder
from kivy.uix.screenmanager import Screen

from app.services.auth_service import AuthService

Builder.load_file("app/kv/login.kv")


class LoginScreen(Screen):

    def login(self):
        username = self.ids.username.text.strip()
        password = self.ids.password.text.strip()

        if not username or not password:
            print("Username or Password missing")
            return

        user = AuthService.login(username, password)

        if user:
            print("Login Success")
            self.manager.current = "dashboard"
        else:
            print("Invalid Username or Password")