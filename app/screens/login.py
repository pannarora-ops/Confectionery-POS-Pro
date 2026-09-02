from kivymd.uix.screen import MDScreen


class LoginScreen(MDScreen):

    def login(self):
        username = self.ids.username.text
        password = self.ids.password.text

        if username == "admin" and password == "1234":
            self.manager.current = "dashboard"