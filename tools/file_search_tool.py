import os
from pathlib import Path
from langchain_core.tools import tool

@tool
def search_file(filename: str) -> str:
    """
    Search for a file by name in user directories.
    Accepts plain input like 'ene.txt', even if passed with quotes.
    """
    filename = filename.strip("'\"")  # 👈 Strip extra quotes

    whitelist_dirs = [
        Path.home() / "Documents",
        Path.home() / "Desktop",
        Path.home() / "Downloads",
    ]

    for folder in whitelist_dirs:
        if not folder.exists():
            continue
        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.lower() == filename.lower():
                    return f" Found: {os.path.join(root, file)}"
    
    return f" File '{filename}' not found in Documents, Desktop, or Downloads."
