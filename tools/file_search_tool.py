import os
from pathlib import Path
from langchain_core.tools import tool

@tool
def search_file(filename: str) -> str:
   
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
                # Skip folders we don't have access to
                continue
            except Exception as e:
                print(f"⚠️ Error scanning {root}: {e}")
                continue

    if found_paths:
        return f" Found: {found_paths[0]}"  # Return first match
    else:
        return f"File '{filename}' not found in search directories."
