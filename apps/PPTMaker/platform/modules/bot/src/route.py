from fastapi import APIRouter, BackgroundTasks, Depends, Request
from fastapi.responses import JSONResponse
from starlette_context import context

from apps.PPTMaker.auth.src.service import verify_access_token
from libs.PPTMaker.platform.modules.bot.src.utils.limiter_util import (
    RATE_LIMIT,
    limiter,
)
from libs.utils.common.custom_logger import CustomLogger

log = CustomLogger("FinancialChatbotRoute")

logger, listener = log.get_logger()
listener.start()

chatbot_route = APIRouter(prefix="/chatbot", tags=["Financial query chatbot"])


@chatbot_route.get("/")
async def index():
    logger.debug("Chatbot Route index path...")
    return JSONResponse(
        status_code=200,
        content={
            "message": "Chatbot Route index path...",
            "success": True,
        },
    )


@chatbot_route.get("/health-check")
async def health_check():
    logger.debug("Chatbot Route health check path...")
    return JSONResponse(
        status_code=200,
        content={
            "message": "Financial query chatbot health check path...",
            "success": True,
        },
    )


@chatbot_route.post("/chat", dependencies=[Depends(verify_access_token)])
@limiter.limit(RATE_LIMIT)
async def answer_financial_query(
    request: Request,
    request_data: dict,
    background_tasks: BackgroundTasks,
    token_data=Depends(verify_access_token),
):
    try:
        context["username"] = token_data.get("username")
        return JSONResponse(
            content={"message": "chat route accessed!!"},
            status_code=200,
        )
    except Exception as error:
        return JSONResponse(
            content={"success": False, "error": str(error)}, status_code=500
        )
