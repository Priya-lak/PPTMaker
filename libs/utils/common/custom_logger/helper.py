from datetime import datetime
from os import getcwd, path

from starlette.requests import Request
from starlette.responses import Response
from starlette.routing import Match

from libs.utils.common.custom_logger.constants import Colors
from libs.utils.common.custom_logger.enums import LogType
from libs.utils.common.custom_logger.str_helpers import color_string
from libs.utils.common.date_time import convert_ms_to_readable_format, get_execution_time_in_seconds


def extra_details_for_req(
    inspect,
    cls_name,
    request: Request = None,
    request_body=None,
    response: Response = None,
    response_body=None,
    start_time: datetime = None,
):
    frame = inspect.currentframe().f_back
    frame_info = inspect.getframeinfo(frame)

    extra = {
        "fileName": frame_info.filename.split("/")[-1],
        "filePath": path.relpath(frame_info.filename, getcwd()),
        "line": frame_info.lineno,
        "column": frame_info.positions.col_offset,
        "functionName": frame_info.function,
        "className": cls_name,
        "qualname": f"{cls_name}.{frame_info.function}",
    }
    if request:
        routes = request.app.router.routes
        path_params = dict()
        query_params = dict()
        for route in routes:
            match, scope = route.matches(request)
            if match == Match.FULL:
                path_params = scope.get("path_params")
                query_params = scope.get("query_params")

        args = request_body.copy()
        if "assistant_name" in args:
            args.pop("assistant_name")
        if "user_id" in args:
            args.pop("user_id")

        req_data = {
            "logType": LogType.REQUEST_INIT.value,
            "extraDetails": f"'{request.method} {request.url.path}', {args}",
            "request": {
                "method": request.method,
                "path": request.url.path,
                "headers": dict(request.headers),
                "body": dict(request_body),
                "params": path_params,
                "query": query_params,
                "calleeDetails": {
                    "host": request.client.host,
                    "port": request.client.port,
                },
            },
        }
        extra.update(req_data)

    if response:
        execution_time_ms = get_execution_time_in_seconds(start_time) * 1000
        execution_time = color_string(
            f"({convert_ms_to_readable_format(execution_time_ms)})",
            Colors.BOLD_GOLD,
        )
        res_data = {
            "logType": LogType.REQUEST_END.value,
            "extraDetails": f"{response.status_code} {execution_time}",
            "response": {
                "statusCode": response.status_code,
                "headers": dict(response.headers),
                "body": response_body,
                "executionTimeMs": execution_time_ms,
                "executionTime": execution_time,
            },
        }
        extra.update(res_data)

    return extra
