from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

from apps.PPTMaker.auth.src.service import (
    authenticate_user,
    create_access_token,
)
from apps.PPTMaker.platform.modules.core.src.dto import Token
from libs.utils.common.custom_logger import CustomLogger

log = CustomLogger("ChatbotCoreRoute")

logger, listener = log.get_logger()
listener.start()

core_route = APIRouter(tags=["Core Routes"])


@core_route.get("/")
def root():
    logger.info("Financial Chatbot app root endpoint accessed")
    return JSONResponse(
        status_code=200,
        content={"success": True, "message": "Server is up and running 🚀🚀🚀"},
    )


@core_route.post("/token", include_in_schema=False)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    logger.debug(f"Token request received for user: {form_data.username}")
    try:
        user = authenticate_user(form_data.username, form_data.password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )

        access_token = create_access_token(user_id=form_data.username)
        return Token(access_token=access_token, token_type="bearer")
    except Exception as e:
        logger.error(f"Unexpected error during token generation: {str(e)}")
        raise
