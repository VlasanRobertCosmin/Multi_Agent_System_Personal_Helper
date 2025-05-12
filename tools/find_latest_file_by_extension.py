import os
from datetime import datetime
from pathlib import Path
from langchain_core.tools import tool

@tool
def find_latest_file_by_extension(extension: str) -> str:
    """
    Find the most recently modified file with a given extension in user directories.
    Input should be a string like '.txt', '.csv', etc.
    """
    extension = extension.strip().strip("'\"").lower()

    if not extension.startswith("."):
        return " Please provide a valid file extension (like .txt, .csv, .docx)."

    whitelist_dirs = [
        Path.home() / "Documents",
        Path.home() / "Desktop",
        Path.home() / "Downloads",
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
                    except Exception:
                        continue
                    if mod_time > latest_time:
                        latest_time = mod_time
                        latest_file = full_path

    if latest_file:
        return f" Latest {extension} file: {latest_file} (modified {datetime.fromtimestamp(latest_time)})"
    return f" No files with extension '{extension}' found."
