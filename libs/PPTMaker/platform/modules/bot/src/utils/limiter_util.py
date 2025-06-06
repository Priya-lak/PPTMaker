from os import path

from dotenv import dotenv_values
from slowapi import Limiter
from slowapi.util import get_remote_address

env_path = ".env"

if not path.exists(env_path):
    raise Exception(".env file not found")

config = dotenv_values(env_path)

MAX_REQUESTS = config.get("MAX_REQUESTS", 1)
TIME_WINDOW = config.get("TIME_WINDOW", "minute")

RATE_LIMIT = f"{MAX_REQUESTS}/{TIME_WINDOW}"


limiter = Limiter(
    key_func=get_remote_address,
)
