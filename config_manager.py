import requests
import os
from dotenv import load_dotenv


PATH = os.getenv("BACKUP_PATH")
API_BASE_URL = os.getenv("API_BASE_URL")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")