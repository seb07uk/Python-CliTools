# 🚀 polsoft.ITS CLI Ecosystem (2026 Edition)

A professional collection of system tools, functional modules, and arcade games implemented in **Python**. This ecosystem is designed for the Windows terminal environment, emphasizing ANSI aesthetics, performance, and persistent data management.

### 👨‍💻 Author Information
* **Author:** Sebastian Januchowski
* **Brand:** polsoft.ITS London
* **GitHub:** [seb07uk](https://github.com/seb07uk)
* **Email:** polsoft.its@fastservice.com

---

## 🧩 Section: System Modules (CLI Plugins)
The following files are modular plugins optimized for integration with a central dispatcher (`cli.py`). They utilize a shared `@command` decorator and a unified color palette.

* **Calculator Pro (module):** A scientific calculator plugin with history logging saved to `%userprofile%\.polsoft\psCli\Calculator\`.
* **psBrowser CLI (module):** A text-based web browser featuring cookie support, page snapshots, and JSON history.
* **Games Menu:** A dynamic entertainment hub that scans the games directory and launches titles in new console windows.
* **print (module):** An advanced file reader with syntax highlighting (Python, JSON, MD) and 20-line pagination.
* **file list generator:** A tool for scanning directory structures, synchronized with global `terminal.json` settings.
* **echo (module):** A diagnostic utility for displaying colored ANSI system messages.

---

## 🛠️ Section: Standalone Utilities

### 📂 CMD File Manager v1.5.0
A lightweight file manager with a confirmation system. It allows for copying, moving, and deleting assets, plus quick access to system report folders.

### 🎨 Paint Cli v1.0
A unique ASCII graphic editor for the terminal. It supports the ANSI color palette, various brush types, and the ability to export designs to `.txt` files.

### 📝 Simple Notepad v1.5
A notepad featuring `W/S` key navigation and an Auto-save system. Ideal for quick notes without leaving the terminal environment.

### 🖼️ ICON TOOL - Icon Manager
A resource management tool: extract icons from `.exe`/`.dll` files, convert images to `.ico` format, and build local icon libraries.

---

## 🎮 Section: Entertainment (Games)

| Title | Description | Features |
| :--- | :--- | :--- |
| **Snake CLI** | Classic retro snake | 3 difficulty levels, skin system, TOP 5 ranking. |
| **Hangman** | Logic word game | VS CPU and Multiplayer modes (with hidden input). |
| **Tic-Tac-Toe** | Noughts and Crosses | `winsound` effects and match history logging. |
| **Rock-Paper-Scissors** | Game engine | Persistent win/loss stats, EN/PL language support. |

---

## ⚙️ Data Architecture & Paths
The system uses a consistent folder hierarchy within the user profile for easy backups and configuration management:

* **Main Data Root:** `%USERPROFILE%\.polsoft\`
* **Global Settings:** `...\psCli\settings\terminal.json`
* **History & Logs:** `...\psCli\History\`
* **Game Assets:** `...\psCli\Games\`

---

### 💻 Technical Requirements
1.  **Interpreter:** Python 3.x
2.  **System:** Windows (utilizes `msvcrt`, `winsound`, and `ctypes` for ANSI support).
3.  **Terminal:** **Windows Terminal** or PowerShell (recommended for full color support).
4.  **Dependencies:** `Pillow` (required only for the *Icon Tool* module).

---
*2026© polsoft.ITS London | Created by Sebastian Januchowski*