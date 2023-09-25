import configparser
import os
import pathlib

import dotenv

ROOT_FOLDER = pathlib.Path(__file__).parent.parent
dotenv.load_dotenv()
config = configparser.ConfigParser()
config.add_section('general')
config['general'] = os.environ
environ = config['general']

# fastapi
DEBUG = environ.getboolean('DEBUG')
HOST = environ.get('HOST')
PORT = environ.getint('PORT')

# mongodb
MONGO_INITDB_ROOT_USERNAME: str = environ['MONGO_INITDB_ROOT_USERNAME']
MONGO_INITDB_ROOT_PASSWORD: str = environ['MONGO_INITDB_ROOT_PASSWORD']
MONGO_HOST: str = environ['MONGO_HOST']
MONGO_PORT: int = environ.getint('MONGO_PORT')
MONGO_URL: str = f'mongodb://{MONGO_INITDB_ROOT_USERNAME}:{MONGO_INITDB_ROOT_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}'
