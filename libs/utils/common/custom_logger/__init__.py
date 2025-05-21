import logging
import logging.config
import queue
from logging.handlers import QueueListener

from libs.utils.common.custom_logger.constants import Colors
from libs.utils.common.custom_logger.enums import LogType
from libs.utils.common.custom_logger.handlers import (
    RequestDetailsFilter,
    console_handler,
    dynamic_file_handler,
)


class CustomLogger:
    def __init__(
        self,
        logger_name: str,
        queue_logger: bool = True,
        is_request: bool = True,
    ):
        self.logger_name = logger_name
        self.queue_logger = queue_logger
        self.is_request = is_request
        if queue_logger:
            self.root_logger, self.root_listener = self.get_logger()
        else:
            self.root_logger = self.get_logger()

    def get_logger(
        self,
        enable_console_handler: bool = True,
        enable_files_handler: bool = True,
    ):
        logger = logging.getLogger(self.logger_name)

        logger.setLevel(logging.DEBUG)
        request_id_filter = RequestDetailsFilter(is_request=self.is_request)
        logger.addFilter(request_id_filter)
        logger.propagate = False

        # Remove all handlers associated with the logger
        if logger.hasHandlers():
            logger.handlers.clear()

        _handlers = []
        _handlers.append(console_handler) if enable_console_handler else None
        _handlers.append(dynamic_file_handler) if enable_files_handler else None

        if self.queue_logger:
            log_queue = queue.Queue()
            queue_handler = logging.handlers.QueueHandler(log_queue)
            logger.addHandler(queue_handler)

            listener = QueueListener(log_queue, *_handlers, respect_handler_level=True)
            return logger, listener

        for _handler in _handlers:
            logger.addHandler(_handler)

        return logger


if __name__ == "__main__":
    log = CustomLogger("test", queue_logger=False, is_request=False)
    test_logger = log.get_logger()
    test_logger.info("Test")
