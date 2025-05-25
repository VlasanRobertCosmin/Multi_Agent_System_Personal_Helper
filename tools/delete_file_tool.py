import os
import shutil
from pathlib import Path
from langchain_core.tools import tool

# We'll use a fixed trash folder
TRASH_FOLDER_C = Path("C:/Users/Robiti/.trash")
TRASH_FOLDER_D = Path("D:/.trash")

TRASH_FOLDER_C.mkdir(parents=True, exist_ok=True)
TRASH_FOLDER_D.mkdir(parents=True, exist_ok=True)

# This keeps track of the last deleted file
last_deleted = {}

@tool
def delete_file(file_path: str) -> str:
    """
    Move a file to a trash folder (soft delete).
    Input: Full file path (e.g., 'C:\\Users\\Robiti\\Documents\\ene.txt')
    """
    global last_deleted

    file_path = file_path.strip().strip('"\'')
    path = Path(file_path)

    if not path.exists():
        return f" File not found: {file_path}"

    if path.is_dir():
        return f" The specified path is a directory, not a file: {file_path}"

    # Confirm target trash folder
    if str(path).lower().startswith("c:"):
        trash_folder = TRASH_FOLDER_C
    elif str(path).lower().startswith("d:"):
        trash_folder = TRASH_FOLDER_D
    else:
        return "⚠️ Unsupported drive for trash."

    try:
        # Move to trash
        trash_path = trash_folder / path.name
        shutil.move(str(path), str(trash_path))

        # Record for undo
        last_deleted['original_path'] = path
        last_deleted['trash_path'] = trash_path

        return f"🗑️ Moved to trash: {trash_path}\n Do you want to undo this deletion? Ask: 'Undo last delete'"
    except Exception as e:
        return f"⚠️ Failed to move file '{file_path}' to trash: {e}"

@tool
def undo_last_delete(dummy_input: str) -> str:
    """
    Undo the last deletion by restoring the file from trash.
    Input can be any string (ignored).
    """
    global last_deleted

    if not last_deleted:
        return " No recently deleted file to undo."

    try:
        shutil.move(str(last_deleted['trash_path']), str(last_deleted['original_path']))
        restored = last_deleted['original_path']
        last_deleted = {}
        return f" Successfully restored: {restored}"
    except Exception as e:
        return f" Failed to restore file: {e}"