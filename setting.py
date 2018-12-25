import os
from os.path import join, dirname
from dotenv import Dotenv

dotenv_path = join(dirname(__file__), '.env')
dotenv = Dotenv(dotenv_path)
os.environ.update(dotenv)

URL = os.environ.get("URL")
AUTH = os.environ.get("AUTH")

