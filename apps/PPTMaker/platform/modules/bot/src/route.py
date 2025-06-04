import os
import traceback
import urllib

from fastapi import (
    APIRouter,
    BackgroundTasks,
    Depends,
    HTTPException,
    Query,
    Request,
    Response,
)
from fastapi.responses import JSONResponse
from starlette_context import context

from apps.PPTMaker.auth.src.service import verify_access_token
from apps.PPTMaker.platform.modules.bot.src.dto import (
    ContentGenerationRequest,
    DownloadFileRequest,
    PresentationGenerationRequest,
)
from apps.PPTMaker.platform.modules.bot.src.service import (
    create_customized_presentation,
    download_presentation_service,
    generate_presentation_content,
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
    request_data: ContentGenerationRequest,
    # token_data=Depends(verify_access_token),
):
    try:
        # context["username"] = token_data.get("username")
        response = generate_presentation_content(request_data)
        return JSONResponse(
            content={
                "message": "generated presentation content",
                "success": True,
                "content": response,
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
    # token_data=Depends(verify_access_token),
):
    try:
        # context["username"] = token_data.get("username")
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


# Updated backend route for serving PPT file as response body
@chatbot_route.get(
    "/preview/{filepath:path}", dependencies=[Depends(verify_access_token)]
)
async def preview_presentation(filepath: str):
    try:
        # Verify token if needed
        # verify_token(token)  # Implement your token verification logic

        # Decode the filepath
        decoded_filepath = urllib.parse.unquote(filepath)

        # Ensure the file exists
        if not os.path.exists(decoded_filepath):
            raise HTTPException(status_code=404, detail="File not found")

        # Read the file content
        with open(decoded_filepath, "rb") as file:
            file_content = file.read()

        # Return the file content with appropriate headers for embedding
        return Response(
            content=file_content,
            media_type="application/vnd.openxmlformats-officedocument.presentationml.presentation",
            headers={
                "Content-Disposition": "inline",  # Changed from 'attachment' to 'inline'
                "Content-Length": str(len(file_content)),
                "Accept-Ranges": "bytes",
                "Cache-Control": "no-cache, no-store, must-revalidate",
                "Pragma": "no-cache",
                "Expires": "0",
            },
        )
    except Exception as e:
        logger.error(
            f"An error occurred while serving file for preview: {traceback.format_exc()}"
        )
        raise HTTPException(status_code=500, detail=str(e))


@chatbot_route.post("/download")
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
