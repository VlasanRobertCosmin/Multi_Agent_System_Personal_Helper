import os
from pathlib import Path


filename_to_find = "ene.txt"
search_folders = [
    Path.home() / "Documents",
    Path.home() / "Desktop",
    Path.home() / "Downloads",
    Path("C:/Projects"),
    Path("C:/Work"),
    Path("D:/Work"),
]

print(f"\n🔍 Searching for '{filename_to_find}' in known user folders...\n")

found_any = False

for folder in search_folders:
    print(f"📂 Scanning folder: {folder}")
    if not folder.exists():
        print("⚠️  Folder does not exist.")
        continue
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.lower() == filename_to_find.lower():
                print(f" Found: {os.path.join(root, file)}")
                found_any = True

if not found_any:
    print(f"\n File '{filename_to_find}' was NOT found in the above folders.")
