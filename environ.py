import os

from dotenv import load_dotenv


load_dotenv()

DB_PORT = os.environ.get('DB_PORT')
APP_PORT = os.environ.get('APP_PORT')
