from pathlib import Path

# -----------------------------
# Project Paths
# -----------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

APP_DIR = BASE_DIR / "app"
DATABASE_DIR = BASE_DIR / "database"

ASSETS_DIR = APP_DIR / "assets"

IMAGES_DIR = ASSETS_DIR / "images"
ICONS_DIR = ASSETS_DIR / "icons"
FONTS_DIR = ASSETS_DIR / "fonts"

DATABASE_FILE = DATABASE_DIR / "confectionery.db"

# -----------------------------
# Application
# -----------------------------

APP_NAME = "Confectionery POS Pro"
APP_VERSION = "2.0.0"

WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700

THEME_STYLE = "Light"
PRIMARY_PALETTE = "Blue"

# -----------------------------
# Default Admin
# -----------------------------

DEFAULT_USERNAME = "admin"
DEFAULT_PASSWORD = "admin123"