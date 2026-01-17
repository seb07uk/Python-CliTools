import os
import re
from pathlib import Path
from datetime import datetime
from cli import command, Color

__author__ = "Sebastian Januchowski"
__category__ = "io"
__group__ = "core"

def highlight_content(content, extension):
    """Proste kolorowanie składni dla wybranych typów plików."""
    if extension == ".json":
        # Kolorowanie kluczy w JSON (tekst w cudzysłowie przed dwukropkiem)
        return re.sub(r'(".*?")\s*:', f"{Color.CYAN}\\1{Color.RESET}:", content)
    elif extension == ".py":
        # Kolorowanie komentarzy w Pythonie
        return re.sub(r'(#.*)', f"{Color.GRAY}\\1{Color.RESET}", content)
    return content

@command(name="print", aliases=["cat", "type"])
def print_file(*args):
    """Odczyt notatek / podgląd JSON / wyświetlanie kodu źródłowego. Loguje do History\\print.log"""
    
    # Obsługa pomocy
    if not args or "-h" in args or "--help" in args:
        print(f"{Color.CYAN}Użycie:{Color.RESET}")
        print(f"  print <ścieżka_do_pliku>")
        print(f"  cat <ścieżka_do_pliku>")
        print(f"  type <ścieżka_do_pliku>")
        print(f"\n{Color.CYAN}Opis:{Color.RESET}")
        print("  Wyświetla zawartość pliku w konsoli z podstawowym kolorowaniem składni.")
        print("  Zapisuje kopię w logach historii.")
        print(f"  Logi są przechowywane w: %userprofile%\\.polsoft\\psCLI\\History\\print.log")
        print(f"\n{Color.CYAN}Obsługiwane typy plików:{Color.RESET}")
        print("  .txt, .json, .py, .log, .md, .csv, .yaml, .xml")
        print(f"\n{Color.GRAY}author:  Sebastian Januchowski")
        print("email:   polsoft.its@fastservice.com")
        print(f"github:  https://github.com/seb07uk{Color.RESET}")
        return
    
    filepath = args[0]
    path = Path(filepath)
    
    # Konfiguracja ścieżki logowania
    log_dir = Path.home() / ".polsoft" / "psCLI" / "History"
    log_file = log_dir / "print.log"
    
    if not path.exists():
        error_msg = f"[ERROR] Plik {filepath} nie istnieje."
        print(f"{Color.RED}{error_msg}{Color.RESET}")
        return

    try:
        content = path.read_text(encoding="utf-8")
        extension = path.suffix.lower()
        
        # Wyjście w konsoli z kolorowaniem
        print(f"{Color.GRAY}--- Zawartość: {filepath} ---{Color.RESET}")
        print(highlight_content(content, extension))
        print(f"{Color.GRAY}--- Koniec pliku ---{Color.RESET}")

        # Zapis do print.log
        log_dir.mkdir(parents=True, exist_ok=True)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] Dostęp: {filepath}\n")
            f.write(f"{'-'*20}\n{content}\n{'='*40}\n")

    except Exception as e:
        print(f"{Color.RED}Nie można odczytać pliku: {e}{Color.RESET}")