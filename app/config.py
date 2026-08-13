import os
from dotenv import load_dotenv

load_dotenv()

APP_ENV = os.getenv("APP_ENV", "development")

APP_HOST = os.getenv("APP_HOST", "0.0.0.0")
APP_PORT = int(os.getenv("APP_PORT", 8000))

DEBUG = APP_ENV == "development"

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./ads.db")

APP_VERSION = os.getenv("APP_VERSION", "development")