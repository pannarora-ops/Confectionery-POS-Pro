"""
Confectionery POS Pro
Main Application
"""

from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

# Screens
from app.screens.login import LoginScreen
from app.screens.dashboard import DashboardScreen
from app.screens.products import ProductsScreen


class ConfectioneryPOSApp(MDApp):

    def build(self):

        self.title = "Confectionery POS Pro"

        # Theme
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Blue"

        # Load KV Files
        Builder.load_file("app/kv/login.kv")
        Builder.load_file("app/kv/dashboard.kv")
        Builder.load_file("app/kv/products.kv")

        # Screen Manager
        sm = ScreenManager()

        # Register Screens
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(DashboardScreen(name="dashboard"))
        sm.add_widget(ProductsScreen(name="products"))

        # Start Screen
        sm.current = "dashboard"
        return sm


if __name__ == "__main__":
    ConfectioneryPOSApp().run()