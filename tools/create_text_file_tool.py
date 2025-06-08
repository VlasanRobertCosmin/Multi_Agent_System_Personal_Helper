import os
from langchain_core.tools import tool

@tool
def create_text_file(input_str: str) -> str:
 
    try:
        filename, content = input_str.split("|", 1)
        filename = filename.strip()
        content = content.strip()

        documents_dir = os.path.expanduser("~/Documents")
        os.makedirs(documents_dir, exist_ok=True)
        file_path = os.path.join(documents_dir, filename)

        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

        return f" File '{filename}' created successfully at: {file_path}"
    except ValueError:
        return " Invalid input format. Use: filename.txt | content"
    except Exception as e:
        return f" Error creating file: {e}"
