from datetime import datetime, timedelta, timezone
from typing import Annotated

import jwt
from cachetools import TTLCache, cached
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from passlib.hash import pbkdf2_sha256

from apps.PPTMaker.src.app_config import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    AUTH_ALGORITHM,
    AUTH_KEY,
)

# from libs.PPTMaker.platform.modules.bot.src.repository import users_repository
from libs.utils.common.custom_logger import CustomLogger

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

log = CustomLogger("ChatbotAuthService")

logger, listener = log.get_logger()
listener.start()

cache = TTLCache(maxsize=100, ttl=int(ACCESS_TOKEN_EXPIRE_MINUTES) * 60 * 60)


def create_access_token(user_id: str = "default", expires_delta: int = None) -> str:
    logger.debug(f"Creating access token for user: {user_id}...")
    if expires_delta is not None:
        expires_delta = datetime.now(timezone.utc) + timedelta(minutes=expires_delta)
    else:
        expires_delta = datetime.now(timezone.utc) + timedelta(
            minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES)
        )

    to_encode = {"exp": expires_delta, "username": user_id}
    encoded_jwt = jwt.encode(to_encode, AUTH_KEY, AUTH_ALGORITHM)
    logger.debug(
        f"Access token created with expiry: {expires_delta.strftime('%Y-%m-%d %H:%M:%S')}."
    )
    return encoded_jwt


# Function to verify the access token extracted from the request
@cached(cache)
def verify_access_token(token: Annotated[str, Depends(oauth2_scheme)]):
    logger.debug("Verifying access token...")
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, AUTH_KEY, algorithms=[AUTH_ALGORITHM])
        username = payload.get("username")
        if username is None:
            logger.warning("Token validation failed: username not found in token.")
            raise credentials_exception
        token_data = {"username": username}
        logger.debug(f"Token validated successfully for user: {username}.")

    except jwt.InvalidTokenError:
        logger.error("Invalid token error during token verification.")
        raise credentials_exception
    # if user is None:
    #     raise credentials_exception
    return token_data


@cached(cache)
def authenticate_user(username, password):
    logger.debug(f"Authenticating user password for user {username}...")
    # user = users_repository.find_one({"username": username})
    user = "user"
    if not user:
        logger.warning(f"Authentication failed: User {username} not found!!")
        return False

    is_verified = pbkdf2_sha256.verify(password, user.get("password"))
    if is_verified:
        logger.debug(f"User {username} authenticated successfully.")
    else:
        logger.warning(f"Authentication failed: Invalid password for user {username}.")

    return is_verified
