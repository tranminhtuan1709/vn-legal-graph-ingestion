from datetime import datetime
from zoneinfo import ZoneInfo


def check_valid_date(date_string: str, format: str) -> bool:
    try:
        datetime.strptime(date_string, format)
        return True
    except Exception:
        return False


def get_current_timestamp() -> str:
    timezone = ZoneInfo("Asia/Ho_Chi_Minh")
    current_timestamp = datetime.now(timezone)

    return current_timestamp.strftime("%Y-%m-%d %H:%M:%S")
