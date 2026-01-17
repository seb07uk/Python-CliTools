import os
import re
from pathlib import Path
from datetime import datetime
from cli import command, Color

__author__ = "Sebastian Januchowski"
__category__ = "io"
__group__ = "core"

def highlight_content(content, extension):
    """Simple syntax highlighting for specific file types."""
    if extension == ".json":
        # Highlight JSON keys (text in quotes before a colon)
        return re.sub(r'(".*?")\s*:', f"{Color.CYAN}\\1{Color.RESET}:", content)
    elif extension == ".py":
        # Highlight Python comments
        return re.sub(r'(#.*)', f"{Color.GRAY}\\1{Color.RESET}", content)
    return content

@command(name="print", aliases=["cat", "type"])
def print_file(*args):
    """Reading notes / JSON preview / Displaying source code. Logs to History\\print.log"""
    
    # Help handling
    if not args or "-h" in args or "--help" in args:
        print(f"{Color.CYAN}Usage:{Color.RESET}")
        print(f"  print <file_path>")
        print(f"  cat <file_path>")
        print(f"  type <file_path>")
        print(f"\n{Color.CYAN}Description:{Color.RESET}")
        print("  Displays file content in the console with basic syntax highlighting.")
        print("  Saves a copy to history logs.")
        print(f"  Logs are stored in: %userprofile%\\.polsoft\\psCLI\\History\\print.log")
        print(f"\n{Color.CYAN}Supported file types:{Color.RESET}")
        print("  .txt, .json, .py, .log, .md, .csv, .yaml, .xml")
        print(f"\n{Color.GRAY}author:  Sebastian Januchowski")
        print("email:   polsoft.its@fastservice.com")
        print(f"github:  https://github.com/seb07uk{Color.RESET}")
        return
    
    filepath = args[0]
    path = Path(filepath)
    
    # Log path configuration
    log_dir = Path.home() / ".polsoft" / "psCLI" / "History"
    log_file = log_dir / "print.log"
    
    if not path.exists():
        error_msg = f"[ERROR] File {filepath} does not exist."
        print(f"{Color.RED}{error_msg}{Color.RESET}")
        return

    try:
        content = path.read_text(encoding="utf-8")
        extension = path.suffix.lower()
        
        # Console output with highlighting
        print(f"{Color.GRAY}--- Content: {filepath} ---{Color.RESET}")
        print(highlight_content(content, extension))
        print(f"{Color.GRAY}--- End of file ---{Color.RESET}")

        # Logging to print.log (saving clean text without ANSI codes)
        log_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] Accessed: {filepath}\n")
            f.write(f"{'-'*20}\n{content}\n{'='*40}\n")

    except Exception as e:
        print(f"{Color.RED}Could not read file: {e}{Color.RESET}")