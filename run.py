"""
Confectionery-POS-Pro

Application Entry Point
"""

from app.database import Database
from kivy.config import Config

Config.set("graphics", "width", "1200")
Config.set("graphics", "height", "800")
Config.set("graphics", "resizable", "1")

def initialize():
    """Initialize application resources."""
    db = Database()
    db.create_tables()
    db.close()


def main():
    initialize()

    # आगे Kivy App यहीं से चलेगा
    from app.main import ConfectioneryPOSApp

    ConfectioneryPOSApp().run()


if __name__ == "__main__":
    main()