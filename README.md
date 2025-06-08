# Multi-Agent System Personal Helper

This is a personal assistant project built using LangChain and Ollama (running a local LLM like Mistral). It is designed to help you perform common tasks on your personal computer via a conversational interface.

## 🔧 Features

### ✅ Supported Agents (Tools)

* **search\_file**: Search for a file by name within typical user directories (Documents, Desktop, Downloads).
* **open\_path**: Open a file, application, or directory.
* **delete\_file**: Deletes a file, with a confirmation prompt.
* **undo\_last\_delete**: Restore the most recently deleted file from the `.trash` directory.
* **backup\_file**: Copy a file to a `backups` folder.
* **create\_text\_file**: Create a `.txt` file and write custom content into it.
* **get\_current\_time**: Return the current system time.
* **get\_current\_date**: Return the current system date.

## 🚀 Getting Started

### 1. Requirements

* Python 3.10+
* Ollama installed and running with a supported model (e.g., `mistral`)
* LangChain & LangChain Community libraries

### 2. Install Dependencies

```bash
pip install langchain langchain-community langchain-ollama
```

### 3. Run the Project

```bash
python main.py
```

## 📁 Project Structure

```
Multi_Agent_System_Personal_Helper/
├── main.py                    # Entry point
├── tools/
│   ├── file_search_tool.py
│   ├── open_path_tool.py
│   ├── delete_file_tool.py
│   ├── create_text_file_tool.py
│   └── ...
├── backups/                  # Backup storage folder
└── .trash/                   # Trash for recoverable deletes
```

## ⚠️ Notes

* Paths are currently hardcoded for Windows. Adapt `Path(...)` in the tools if needed.
* Make sure Ollama is running in the background.
* Files deleted via the agent are moved to `.trash` for safe recovery.

## 💡 Future Improvements

* Cross-platform compatibility
* GUI front-end

---
