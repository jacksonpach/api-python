from decouple import config
from unipath import Path

BASE_DIR = Path(__file__).parent

POSTGRES_USER = config('POSTGRES_USER')
POSTGRES_PASSWORD = config('POSTGRES_PASSWORD')
POSTGRES_HOST = config('POSTGRES_HOST')
POSTGRES_DB = config('POSTGRES_DB')
POSTGRES_PORT = config('POSTGRES_PORT')
POSTGRES_DRIVER = "postgresql+asyncpg"
POSTGRES_URL = f"{POSTGRES_DRIVER}://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

DEBUG = True
HOST_DEBUG = '192.168.18.55'
