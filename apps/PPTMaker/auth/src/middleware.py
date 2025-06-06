import inspect
import traceback
from datetime import datetime, timezone
from json import JSONDecodeError

from starlette.concurrency import iterate_in_threadpool
from starlette.middleware import Middleware
from starlette.middleware.base import (
    BaseHTTPMiddleware,
    RequestResponseEndpoint,
)
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette_context import context, plugins
from starlette_context.middleware import RawContextMiddleware

from libs.utils.common.custom_logger import CustomLogger
from libs.utils.common.custom_logger.helper import extra_details_for_req

log = CustomLogger("ChatbotAppMiddleware")

logger, listener = log.get_logger()
listener.start()


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint):
        included_paths = ["chatbot"]

        if not any(substring in request.url.path for substring in included_paths):
            return await call_next(request)

        start_time = datetime.now(timezone.utc)

        try:
            request_body = await request.json()
        except JSONDecodeError:
            request_body = dict()

        context["userId"] = request_body.get("user_id")
        context["account_id"] = request_body.get("account_id")

        extra = extra_details_for_req(
            inspect, __class__.__name__, request, request_body
        )
        logger.info(f"🚀 Request initiated... | {extra['extraDetails']}", extra=extra)

        try:
            response = await call_next(request)
            response_body = [chunk async for chunk in response.body_iterator]
            response.body_iterator = iterate_in_threadpool(iter(response_body))
            content_type = response.headers.get("content-type", "")
            is_text_response = any(
                content_type.startswith(t)
                for t in ["text/", "application/json", "application/xml"]
            )
            if is_text_response and response_body:
                try:
                    decoded_body = response_body[0].decode()
                    logger.debug(f"Response body: {decoded_body}")
                except UnicodeDecodeError:
                    logger.warning("Response body could not be decoded as UTF-8.")

            extra = extra_details_for_req(
                inspect,
                __class__.__name__,
                response=response,
                response_body=response_body,
                start_time=start_time,
            )

            logger.info(
                f"✅ Request completed successfully | {extra['extraDetails']}",
                extra=extra,
            )
        except Exception as error:
            response = JSONResponse(
                status_code=500, content={"success": False, "error": str(error)}
            )

            extra = extra_details_for_req(
                inspect,
                __class__.__name__,
                response=response,
                start_time=start_time,
            )
            logger.info(
                f"❌ Request failed... | {extra['extraDetails']}{traceback.format_exc()}",
                extra=extra,
            )

        return response


middlewares = [
    Middleware(
        RawContextMiddleware,
        plugins=[plugins.RequestIdPlugin(force_new_uuid=True)],
    ),
    Middleware(LoggingMiddleware),
    Middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
        allow_headers=["*"],  # Allow all headers
    ),
]
