# config_manager.py
import os
from dotenv import load_dotenv


# Carrega as env

load_dotenv()

# Colocando na variável, não precisa ficar repetindo os.getenv

PATH = os.getenv("BACKUP_PATH")
API_BASE_URL = os.getenv("API_BASE_URL")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
