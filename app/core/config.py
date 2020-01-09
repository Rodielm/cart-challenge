import os
from pathlib import Path  # python3 only
from dotenv import load_dotenv

APP_ROOT = os.path.join(os.path.dirname(__file__), '../..')   # refers to application_top
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)
PROJECT_NAME = os.getenv("PROJECT_NAME")
ENVIRONMENT = os.getenv("ENVIRONMENT")
DB_NAME = os.getenv('DB_NAME')
