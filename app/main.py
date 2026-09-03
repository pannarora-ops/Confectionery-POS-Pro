from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivymd.app import MDApp

from app.config import (
    APP_NAME,
    APP_VERSION,
    PRIMARY_PALETTE,
    THEME_STYLE,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
)

from app.database import Database

from app.screens.splash import SplashScreen
from app.screens.login import LoginScreen
from app.screens.dashboard import DashboardScreen


class POSApp(MDApp):

    def build(self):

        self.title = f"{APP_NAME} v{APP_VERSION}"

        self.theme_cls.primary_palette = PRIMARY_PALETTE
        self.theme_cls.theme_style = THEME_STYLE

        Window.size = (WINDOW_WIDTH, WINDOW_HEIGHT)
        Window.minimum_width = 1000
        Window.minimum_height = 650

        db = Database()
        db.create_tables()
        db.close()

        sm = ScreenManager()

        sm.add_widget(SplashScreen(name="splash"))
        sm.add_widget(LoginScreen(name="login"))
        sm.add_widget(DashboardScreen(name="dashboard"))

        sm.current = "splash"

        return sm