import sys
from pathlib import Path

BASE_DIR = str(Path(__file__).resolve().parent.parent.parent.parent)
sys.path.append(BASE_DIR)

from apps.PPTMaker.src import start_server
from apps.PPTMaker.src.app_config import (
    FASTAPI_APP_ENVIRONMENT,
    FASTAPI_APP_HOST,
    FASTAPI_APP_PORT,
    FASTAPI_APP_THREADS,
    FASTAPI_APP_WORKERS,
)

if __name__ == "__main__":
    start_server(
        host=FASTAPI_APP_HOST,
        port=FASTAPI_APP_PORT,
        workers=FASTAPI_APP_WORKERS,
        threads=FASTAPI_APP_THREADS,
        environment=FASTAPI_APP_ENVIRONMENT,
    )
