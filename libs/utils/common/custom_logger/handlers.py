import logging
import os
import sys
from datetime import datetime, timezone
from logging.handlers import RotatingFileHandler

from starlette_context import context

from libs.utils.common.custom_logger.constants import COLORS_DICT
from libs.utils.common.custom_logger.enums import LogType
from libs.utils.common.file_helpers import BASE_DIR


class RequestDetailsFilter(logging.Filter):
    def __init__(self, is_request: bool = True, *args, **kwargs):
        self.is_request = is_request
        super().__init__(*args, **kwargs)

    def filter(self, record):
        record.requestId = "rid-None"
        record.userId = "uid-None"
        record.relative_path = os.path.relpath(record.pathname, start=os.getcwd())
        if self.is_request:
            record.requestId = f"rid-{context.get('X-Request-ID', 'None')}"
            record.userId = f"uid-{context.get('username', 'NEW_USER')}"

        return True


# Custom formatter to add colors
class ColoredFormatter(logging.Formatter):
    def format(self, record):
        record = self.__format_record(record)

        colors = {
            "logLevel": COLORS_DICT.get(record.logLevel, COLORS_DICT["RESET"]),
            "logType": COLORS_DICT.get(record.logType, COLORS_DICT["RESET"]),
            "auditAt": COLORS_DICT.get("AUDIT_AT", COLORS_DICT["RESET"]),
            "requestId": COLORS_DICT.get("REQUEST_ID"),
            "userId": COLORS_DICT.get("USER_ID"),
            "qualname": COLORS_DICT.get("QUAL_NAME"),
        }
        colored_attrs = {
            attr: f"{colors[attr]}{getattr(record, attr)}{COLORS_DICT['RESET']}"
            for attr in colors
            if hasattr(record, attr)
        }

        formatted_record = super().format(record)

        for attr, colored_value in colored_attrs.items():
            if getattr(record, attr, None):
                formatted_record = formatted_record.replace(
                    str(getattr(record, attr)), colored_value
                )

        return formatted_record

    @staticmethod
    def __format_record(record):
        record_dict = record.__dict__

        record.auditAt = str(
            datetime.fromtimestamp(record_dict.get("created"), timezone.utc)
        )
        record.logLevel = record_dict.get("levelname")
        record.logType = record_dict.get("logType", LogType.DEFAULT.value)
        record.extraDetails = record_dict.get("extraDetails", "")
        function_name = record_dict.get("functionName", None)
        if function_name is None:
            function_name = record_dict.get("funcName", "N/A")

        class_name = record_dict.get("className", None)
        if class_name is None:
            class_name = record_dict.get("name")

        record.qualname = f"{class_name}.{function_name}"

        return record


class DynamicFileHandler(RotatingFileHandler):
    def __init__(self, *args, **kwargs):
        self.base_directory = os.path.join(BASE_DIR, "logs")
        os.makedirs(self.base_directory, exist_ok=True)
        # Initialize with a default file
        super().__init__(
            os.path.join(self.base_directory, "history.log"), *args, **kwargs
        )


# Create formatter
console_format = ColoredFormatter(
    fmt=" ".join(
        [
            "%(auditAt)s |",
            "%(logLevel)s |",
            "%(userId)s |",
            "%(requestId)s |",
            "%(logType)s |",
            "%(relative_path)s:%(lineno)d|",
            "%(message)s",
        ]
    )
)
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(console_format)

dynamic_file_handler = DynamicFileHandler(
    maxBytes=1 * 1024 * 50, backupCount=10, encoding="utf-8"
)
