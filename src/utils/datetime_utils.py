from datetime import datetime
from zoneinfo import ZoneInfo


def get_current_timestamp() -> datetime:
    return datetime.now(tz=ZoneInfo("Asia/Ho_Chi_Minh"))
