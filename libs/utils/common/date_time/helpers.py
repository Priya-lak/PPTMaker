from datetime import datetime, timezone
from json import dumps

from libs.utils.common.custom_logger.str_helpers import color_string


def get_current_utc_timestamp() -> datetime:
    return datetime.now(timezone.utc)


def convert_ms_to_readable_format(execution_time_ms: float) -> str:
    milliseconds = execution_time_ms % 1000
    seconds = int((execution_time_ms // 1000) % 60)
    minutes = int((execution_time_ms // (1000 * 60)) % 60)
    hours = int((execution_time_ms // (1000 * 60 * 60)) % 24)

    time_str = ""
    if hours > 0:
        time_str += f"{hours}h "
    if minutes > 0:
        time_str += f"{minutes}m "
    if seconds > 0:
        time_str += f"{seconds}s "
    if milliseconds > 0 or time_str == "":
        time_str += f"{milliseconds:.0f}ms"

    return time_str.strip()


def get_execution_time_in_seconds(start_time: datetime) -> float:
    if start_time.tzinfo is timezone.utc:
        return round((get_current_utc_timestamp() - start_time).total_seconds(), 2)
    else:
        return round((datetime.now() - start_time).total_seconds(), 2)


def get_execution_time_in_readable_format(start_time: datetime) -> str:
    if start_time.tzinfo is timezone.utc:
        return color_string(
            convert_ms_to_readable_format(
                (get_current_utc_timestamp() - start_time).total_seconds() * 1000
            )
        )
    else:
        return color_string(
            convert_ms_to_readable_format(
                (datetime.now() - start_time).total_seconds() * 1000
            )
        )


def get_formatted_current_utc_datetime():
    now = datetime.now(timezone.utc)

    # Create a dictionary with different date formats
    return dumps(
        {
            "iso_format": now.isoformat(),
            "date": now.strftime("%Y-%m-%d"),
            "time": now.strftime("%H:%M:%S"),
            "year": now.year,
            "month": now.month,
            "day": now.day,
            "weekday": now.strftime("%A"),
            "timestamp": int(now.timestamp()),
        }
    )


def convert_utc_to_unix_format(timestamp):
    dt = datetime.fromisoformat(timestamp)
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    unix_timestamp = dt.timestamp()
    return unix_timestamp
