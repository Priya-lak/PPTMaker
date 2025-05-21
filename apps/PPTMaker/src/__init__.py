import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from slowapi import _rate_limit_exceeded_handler
from slowapi.errors import RateLimitExceeded

from apps.PPTMaker.auth.src import middlewares
from apps.PPTMaker.platform.modules.bot.src import chatbot_route
from apps.PPTMaker.platform.modules.core.src import core_route
from libs.PPTMaker.platform.modules.bot.src.lifespan import lifespan
from libs.PPTMaker.platform.modules.bot.src.utils.limiter_util import (
    limiter,
)
from libs.utils.common.custom_logger import CustomLogger, LogType
from libs.utils.common.custom_logger.constants import Colors
from libs.utils.common.custom_logger.helper import color_string

load_dotenv()

log = CustomLogger("Chatbot App", queue_logger=False, is_request=False)
logger = log.get_logger()

chatbot_app = FastAPI(
    title="PPT Maker AI",
    version="0.1.1",
    docs_url="/docs",
    redoc_url="/redoc",
    middleware=middlewares,
    lifespan=lifespan,
)


chatbot_app.state.limiter = limiter
chatbot_app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


chatbot_app.include_router(core_route)
chatbot_app.include_router(chatbot_route)


def start_server(
    host: str,
    port: int,
    reload: bool = True,
    workers: int = 8,
    threads: int = 10,
    environment: str = "development",
):
    if environment == "development":
        logger.info(
            color_string(
                f"Starting server on http://{host}:{port} with "
                f"{workers} workers, environment: {environment}, reload: {reload}.",
                Colors.BOLD_RED,
            ),
            extra={"logType": LogType.STARTUP.value},
        )
        uvicorn.run(
            "apps.PPTMaker.src:chatbot_app",
            host=host,
            port=port,
            reload=reload,
            log_level="error",
            workers=workers,
        )
    elif environment == "production":
        logger.info(
            color_string(
                f"Deploying server on http://{host}:{port} with "
                f"{workers} workers, {threads} threads",
                Colors.BOLD_RED,
            ),
            extra={"logType": LogType.STARTUP.value},
        )
        os.system(
            f"gunicorn "
            f"-w {workers} "
            f"--threads {threads} "
            f"-k uvicorn.workers.UvicornWorker "
            f"-b {host}:{port} apps.PPTMaker.src:chatbot_app"
        )
    else:
        raise ValueError(f"Invalid environment: {environment}, check env file!")
