from enum import Enum


class LogColors:
    INFO = "\033[92m"  # Green
    DEBUG = "\033[94m"  # Blue
    WARNING = "\033[93m"  # Yellow
    ERROR = "\033[91m"  # Red
    RESET = "\033[0m"  # Reset to default


class Colors(Enum):
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    ORANGE = "\033[38;2;255;165;0m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    # Bright Colors
    BRIGHT_BLACK = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"

    RESET = "\033[0m"

    # Bold Colors
    BOLD_RED = "\033[1;31m"
    BOLD_GREEN = "\033[1;32m"
    BOLD_YELLOW = "\033[1;33m"
    BOLD_BLUE = "\033[1;34m"
    BOLD_MAGENTA = "\033[1;35m"
    BOLD_CYAN = "\033[1;38;2;0;255;255m"
    BOLD_WHITE = "\033[1;37m"

    # Additional Colors
    DEEP_PINK = "\033[1;38;2;255;20;147m"
    GOLD = "\033[38;2;255;215;0m"
    BOLD_GOLD = "\033[1;38;2;255;215;0m"
    TURQUOISE = "\033[38;2;64;224;208m"

    CORAL = "\033[1;38;2;255;127;80m"
    NEON_GREEN = "\033[38;2;57;255;20m"
    ROSE_PINK = "\033[38;2;255;182;193m"
    BRIGHT_ORANGE = "\033[38;2;255;165;0m"
    UNDERLINE_BOLD_RED = "\033[4;1;31m"
    DEFAULT_WHITE = "\033[0;0;37m"


COLORS_DICT = {
    # Log Levels
    "DEBUG": Colors.BRIGHT_BLUE.value,
    "INFO": Colors.NEON_GREEN.value,
    "WARNING": Colors.BOLD_YELLOW.value,
    "ERROR": Colors.BOLD_RED.value,
    "CRITICAL": Colors.UNDERLINE_BOLD_RED.value,
    # Log Events
    "STARTUP": Colors.NEON_GREEN.value,
    "REQUEST_INIT": Colors.BOLD_CYAN.value,
    "FUNCTION_INVOKE": Colors.BOLD_MAGENTA.value,
    "FUNCTION_RETURN": Colors.BOLD_GREEN.value,
    "REQUEST_END": Colors.BOLD_CYAN.value,
    "DEFAULT": Colors.BRIGHT_WHITE.value,
    # Metadata
    "QUAL_NAME": Colors.BRIGHT_WHITE.value,
    "AUDIT_AT": Colors.BRIGHT_MAGENTA.value,
    "USER_ID": Colors.BRIGHT_YELLOW.value,
    "REQUEST_ID": Colors.BRIGHT_BLUE.value,
    "ASSISTANT_NAME": Colors.CORAL.value,
    "RESET": Colors.DEFAULT_WHITE.value,
}
