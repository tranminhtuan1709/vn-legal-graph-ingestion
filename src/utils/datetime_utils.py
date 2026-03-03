from datetime import datetime


def check_valid_date(date_string: str, format: str) -> bool:
    """
    Check if a string is in specific date format.

    Args:
        date_string (str): A string to check.
        format (str): Format to check.

    Returns:
        bool: True if `date_string` is in `format` format, else False.
    """
    
    try:
        datetime.strptime(date_string, format)
        return True
    except Exception:
        return False
