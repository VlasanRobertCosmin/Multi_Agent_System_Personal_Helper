import os
from datetime import datetime
from pathlib import Path
from langchain_core.tools import tool

@tool
def find_latest_file_by_extension(extension: str) -> str:
    """
    Find the most recently modified file with a given extension in user folders on C: and D: drives.
    Input should be like '.txt'.
    """
    extension = extension.strip("'\"").lower()
    if not extension.startswith("."):
        return " Please provide a valid file extension (e.g., .txt, .csv)."

    whitelist_dirs = [
        Path("C:/Users/Robiti/Documents"),
        Path("C:/Users/Robiti/Desktop"),
        Path("C:/Users/Robiti/Downloads"),
        Path("D:/Users/Robiti/Documents"),
        Path("D:/Users/Robiti/Desktop"),
        Path("D:/Users/Robiti/Downloads"),
    ]

    latest_file = None
    latest_time = 0

    for folder in whitelist_dirs:
        if not folder.exists():
            continue
        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.lower().endswith(extension):
                    full_path = os.path.join(root, file)
                    try:
                        mod_time = os.path.getmtime(full_path)
                    except:
                        continue
                    if mod_time > latest_time:
                        latest_time = mod_time
                        latest_file = full_path

    if latest_file:
        return f"🕓 Latest {extension} file: {latest_file} (modified {datetime.fromtimestamp(latest_time)})"
    return f"❌ No {extension} files found on C: or D:."
