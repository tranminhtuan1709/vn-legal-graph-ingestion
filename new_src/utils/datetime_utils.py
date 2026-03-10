from datetime import datetime
from dateutil import parser
from zoneinfo import ZoneInfo


def format_date(input: str, format: str) -> str:
    return parser.parse(input).strftime(format)


def get_current_timestamp() -> str:
    timezone = ZoneInfo("Asia/Ho_Chi_Minh")
    current_timestamp = datetime.now(timezone)

    return current_timestamp.strftime("%Y-%m-%d %H:%M:%S")
