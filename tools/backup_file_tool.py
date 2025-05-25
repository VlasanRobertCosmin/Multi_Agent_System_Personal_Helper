import shutil
from pathlib import Path
from langchain_core.tools import tool

@tool
def backup_file(file_path: str) -> str:
    """
    Back up a file by copying it into the 'backups' folder on the same drive.
    Example: 'C:\\Users\\Robiti\\Documents\\file.txt' will go to 'C:\\Users\\Robiti\\backups\\file.txt'
    """
    try:
        file_path = Path(file_path.strip().strip('"\''))
        if not file_path.exists():
            return f" Source file not found: {file_path}"

        # Decide backup folder based on drive
        if str(file_path).lower().startswith("c:"):
            backup_folder = Path("C:/Users/Robiti/backups")
        elif str(file_path).lower().startswith("d:"):
            backup_folder = Path("D:/backups")
        else:
            return " Unsupported drive. Only C: and D: are supported."

        # Create backup folder if it doesn't exist
        backup_folder.mkdir(parents=True, exist_ok=True)

        # Destination path
        dest_path = backup_folder / file_path.name

        # Copy file
        shutil.copy2(str(file_path), str(dest_path))
        return f" Backup created: {dest_path}"

    except Exception as e:
        return f" Failed to create backup: {e}"
