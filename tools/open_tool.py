import os
import subprocess
from langchain_core.tools import tool
from pathlib import Path

@tool
def open_path(target: str) -> str:
    """
    Open a known app or a file/folder path from C:/ or D:/.
    Input examples:
    - 'notepad'
    - 'chrome'
    - 'steam'
  
    """

    target = target.strip().strip('"\'').lower()

    # Known app names with multiple possible install locations (C and D)
    known_apps = {
        "notepad": ["notepad.exe"],
        "chrome": [
            "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
            "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
            "D:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
        ],
        "steam": [
            "C:\\Program Files (x86)\\Steam\\Steam.exe",
            "C:\\Program Files\\Steam\\Steam.exe",
            "D:\\Steam\\Steam.exe",
            "D:\\Games\\Steam\\Steam.exe"
        ],
        "vscode": [
            "C:\\Users\\%USERNAME%\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
            "D:\\Apps\\VSCode\\Code.exe"
        ],
        "calculator": ["calc.exe"],
        "explorer": ["explorer.exe"]
    }

    try:
        # 1. If it's a known app name
        if target in known_apps:
            for path in known_apps[target]:
                expanded = os.path.expandvars(path)
                if os.path.exists(expanded) or expanded.endswith(".exe"):
                    subprocess.Popen(expanded)
                    return f"✅ Launched {target}"
            return f"❌ Could not find installation for '{target}'."

        # 2. If it's a path (file/folder)
        path = Path(target)
        if path.exists():
            os.startfile(str(path))
            return f"✅ Opened {path}"
        return f"❌ Path not found: {path}"

    except Exception as e:
        return f"⚠️ Failed to open '{target}': {e}"
