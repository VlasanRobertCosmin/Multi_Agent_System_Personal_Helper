import os
from pathlib import Path
from langchain_core.tools import tool

@tool
def search_file(filename: str) -> str:
    """
    Search for a file by name in Documents, Desktop, and Downloads folders on both C: and D: drives.
    Input should be just the filename (e.g. 'ene.txt').
    """
    filename = filename.strip("'\"").lower()

    whitelist_dirs = [
        Path("C:/Users/Robiti/Documents"),
        Path("C:/Users/Robiti/Desktop"),
        Path("C:/Users/Robiti/Downloads"),
        Path("D:/Users/Robiti/Documents"),
        Path("D:/Users/Robiti/Desktop"),
        Path("D:/Users/Robiti/Downloads"),
    ]

    for folder in whitelist_dirs:
        if not folder.exists():
            continue
        for root, dirs, files in os.walk(folder):
            for file in files:
                if file.lower() == filename:
                    return f" Found: {os.path.join(root, file)}"

    return f" File '{filename}' not found in user folders on C: or D:."
