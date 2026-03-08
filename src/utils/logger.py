import logging
import logging.handlers
from logging import LogRecord, Logger, Formatter
import os
from datetime import datetime
from zoneinfo import ZoneInfo

VN_TZ = ZoneInfo("Asia/Ho_Chi_Minh")


class CustomFormatter(Formatter):
    def formatTime(self, record: LogRecord, datefmt: str = "%Y-%m-%d %H:%M:%S"):
        dt = datetime.fromtimestamp(record.created, VN_TZ)
        return dt.strftime(datefmt)

    def format(self, record: LogRecord):
        timestamp = self.formatTime(record)
        file_info = f"{record.filename}:{record.funcName}:{record.lineno}"

        context = ""

        if hasattr(record, "context") and record.context:
            context = f" {record.context}"

        message = record.getMessage()

        log = f"[{timestamp}] [{record.levelname}] [{file_info}] {message}. {context}"

        if record.exc_info:
            exc_text = self.formatException(record.exc_info)
            log = f"{log}\n{exc_text}"

        return log


def get_logger(name: str, log_file: str, max_bytes: int, backup_count: int, level: int) -> Logger:
    logger = logging.getLogger(name)
    logger.setLevel(level)

    if not logger.handlers:
        logger.addHandler(handler)

    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    handler = logging.handlers.RotatingFileHandler(
        log_file,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding="utf-8",
    )

    formatter = CustomFormatter()
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
