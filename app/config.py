import os
from dotenv import load_dotenv

load_dotenv()

APP_HOST = os.getenv("APP_HOST", "127.0.0.1")
APP_PORT = int(os.getenv("APP_PORT", "8000"))
DEBUG = os.getenv("DEBUG", "True").lower() == "true"
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./ads.db")
