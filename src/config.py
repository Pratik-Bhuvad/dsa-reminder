import os
from dotenv import load_dotenv

load_dotenv()

GMAIL_APP_PASSWORD = os.getenv("APP_PASSWORD")
GMAIL_SENDER_EMAIL = os.getenv("SENDER_EMAIL")
GMAIL_RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")

INPUT_FILE_PATH = os.getenv("INPUT_FILE_PATH")
OUTPUT_FILE_PATH = os.getenv("OUTPUT_FILE_PATH")

LOG_FILE_PATH = os.getenv

DB_FILE = os.getenv("DB_FILE_PATH", "data/dsa_reminder.db")