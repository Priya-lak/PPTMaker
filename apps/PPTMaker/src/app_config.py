from os import path

from dotenv import dotenv_values

env_path = ".env"

if not path.exists(env_path):
    raise Exception(".env file not found")

config = dotenv_values(env_path)

FASTAPI_APP_ENVIRONMENT = config.get("FASTAPI_APP_ENVIRONMENT", "development")

FASTAPI_APP_HOST = config.get("FASTAPI_APP_HOST", "0.0.0.0")
FASTAPI_APP_PORT = int(config.get("FASTAPI_APP_PORT", 9999))

FASTAPI_APP_WORKERS = int(config.get("FASTAPI_APP_WORKERS", 2))
FASTAPI_APP_THREADS = int(config.get("FASTAPI_APP_THREADS", 2))

AUTH_KEY = config.get("AUTH_KEY")

AUTH_ALGORITHM = config.get("AUTH_ALGORITHM")

ACCESS_TOKEN_EXPIRE_MINUTES = config.get("ACCESS_TOKEN_EXPIRE_MINUTES", 30)