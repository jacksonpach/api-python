from decouple import config
from unipath import Path

BASE_DIR = Path(__file__).parent

MYSQL_CONNECTOR_ASYNCMY = config('MYSQL_CONNECTOR_ASYNCMY')
MYSQL_CONNECTOR_PYMYSQL = config('MYSQL_CONNECTOR_PYMYSQL')
MYSQL_USER = config('MYSQL_USER')
MYSQL_PASSWORD = config('MYSQL_PASSWORD')
MYSQL_HOST = config('MYSQL_HOST')
MYSQL_PORT = config('MYSQL_PORT')
MYSQL_DB = config('MYSQL_DB')

DB_URL_ASYNCMY = f"{MYSQL_CONNECTOR_ASYNCMY}://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
DB_URL_PYMYSQL = f"{MYSQL_CONNECTOR_PYMYSQL}://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"

DEBUG = True
HOST_DEBUG = '192.168.18.55'
