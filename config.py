import os

from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

ENGINE = os.getenv("ENGINE")
ECHO = bool(os.getenv("ECHO"))
