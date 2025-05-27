import os
from pathlib import Path
from langchain_core.tools import tool

@tool
def search_file(filename: str) -> str:
    """
    Search for a file by name (case-insensitive) in the following folders:
    - C:/Users/Robiti/Documents
    - C:/Users/Robiti/Desktop
    - C:/Users/Robiti/Downloads
    - D:/Users/Robiti/Documents
    - D:/Users/Robiti/Desktop
    - D:/Users/Robiti/Downloads

    Input:
        filename (str): The name of the file to search for (e.g., 'ene.txt').

    Output:
        str: The full path of the first matching file found, or a not-found message.
    """
    filename = filename.strip().strip('"\'').lower()
    search_dirs = [
        Path("C:/Users/Robiti/Documents"),
        Path("C:/Users/Robiti/Desktop"),
        Path("C:/Users/Robiti/Downloads"),
        Path("D:/Users/Robiti/Documents"),
        Path("D:/Users/Robiti/Desktop"),
        Path("D:/Users/Robiti/Downloads"),
    ]

    found_paths = []

    for folder in search_dirs:
        if not folder.exists():
            continue
        for root, dirs, files in os.walk(folder):
            try:
                for file in files:
                    if file.lower() == filename:
                        full_path = os.path.join(root, file)
                        found_paths.append(full_path)
            except PermissionError:
                continue
            except Exception as e:
                print(f" Error scanning {root}: {e}")
                continue

    if found_paths:
        return f" Found: {found_paths[0]}"  # Return first match
    else:
        return f" File '{filename}' not found in search directories."
