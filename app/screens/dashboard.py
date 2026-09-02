from kivymd.uix.screen import MDScreen


class DashboardScreen(MDScreen):

    def open_products(self):
        self.manager.current = "products"