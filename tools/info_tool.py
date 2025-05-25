from datetime import datetime
from langchain_core.tools import tool

@tool
def get_current_time(dummy_input: str) -> str:
    """
    Get the current local time.
    """
    now = datetime.now()
    return f" Current time: {now.strftime('%H:%M:%S')}"

@tool
def get_current_date(dummy_input: str) -> str:
    """
    Get the current local date.
    """
    today = datetime.now()
    return f" Current date: {today.strftime('%Y-%m-%d')}"
