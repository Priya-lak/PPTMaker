import traceback

from fastapi import APIRouter, BackgroundTasks, Depends, Request
from fastapi.responses import JSONResponse
from starlette_context import context

from apps.PPTMaker.auth.src.service import verify_access_token
from apps.PPTMaker.platform.modules.bot.src.dto import (
    DownloadFileRequest,
    PresentationGenerationRequest,
)
from apps.PPTMaker.platform.modules.bot.src.service import (
    create_customized_presentation,
    download_presentation_service,
)
from libs.PPTMaker.platform.modules.bot.src.utils.limiter_util import (
    RATE_LIMIT,
    limiter,
)
from libs.utils.common.custom_logger import CustomLogger

log = CustomLogger("PPTMakerCoreRoute")

logger, listener = log.get_logger()
listener.start()

chatbot_route = APIRouter(prefix="/chatbot", tags=["PPT maker chatbot"])


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
            "message": "PPTMaker health check path...",
            "success": True,
        },
    )


@chatbot_route.post("/generate-content", dependencies=[Depends(verify_access_token)])
@limiter.limit(RATE_LIMIT)
async def generate_presentation(
    request: Request,
    request_data: PresentationGenerationRequest,
    token_data=Depends(verify_access_token),
):
    try:
        context["username"] = token_data.get("username")
        output_file = create_customized_presentation(request_data)
        return JSONResponse(
            content={
                "message": "presentation successfully created",
                "success": True,
                "output_file": output_file,
            },
            status_code=200,
        )
    except Exception as error:
        logger.error(
            f"An error occurred while creating presentation: {traceback.format_exc()}"
        )
        return JSONResponse(
            content={"success": False, "error": str(error)}, status_code=500
        )


@chatbot_route.post("/create-ppt", dependencies=[Depends(verify_access_token)])
@limiter.limit(RATE_LIMIT)
async def generate_presentation(
    request: Request,
    request_data: PresentationGenerationRequest,
    token_data=Depends(verify_access_token),
):
    try:
        context["username"] = token_data.get("username")
        output_file = create_customized_presentation(request_data)
        return JSONResponse(
            content={
                "message": "presentation successfully created",
                "success": True,
                "output_file": output_file,
            },
            status_code=200,
        )
    except Exception as error:
        logger.error(
            f"An error occurred while creating presentation: {traceback.format_exc()}"
        )
        return JSONResponse(
            content={"success": False, "error": str(error)}, status_code=500
        )


@chatbot_route.post("/download", dependencies=[Depends(verify_access_token)])
async def download_presentation(request_data: DownloadFileRequest):
    try:
        return download_presentation_service(request_data)
    except Exception as e:
        logger.error(
            f"An error occurred while downloading file: {traceback.format_exc()}"
        )
        return JSONResponse(
            content={"success": False, "error": str(e)}, status_code=500
        )
