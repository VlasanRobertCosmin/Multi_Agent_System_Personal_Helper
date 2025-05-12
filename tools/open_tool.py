import os
import subprocess
from langchain_core.tools import tool
from pathlib import Path

@tool
def open_path(target: str) -> str:
    """
    Open an application, folder, or file based on a path or known app name.
    Examples:
      - 'notepad'
      - 'chrome'
      - 'C:\\Users\\Robiti\\Documents\\ene.txt'
      - 'C:\\Users\\Robiti\\Downloads'
    """
    target = target.strip().strip('"\'')  

    # Known app shortcuts (add your own if needed)
    known_apps = {
        "notepad": "notepad.exe",
        "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    }

    try:
        # 1. Known app
        if target.lower() in known_apps:
            subprocess.Popen(known_apps[target.lower()])
            return f"✅ Opened {target}"

        # 2. File or folder path
        path = Path(target)
        if path.exists():
            os.startfile(str(path))
            return f" Opened {path}"
        else:
            return f" Path not found: {path}"

    except Exception as e:
        return f" Failed to open '{target}': {e}"
