# 🚀 polsoft.ITS CLI Ecosystem (2026 Edition)

Zbiór profesjonalnych narzędzi systemowych, modułów funkcjonalnych oraz gier arkadowych zaimplementowanych w języku **Python**. Całość została zaprojektowana z myślą o pracy w środowisku terminala Windows, z naciskiem na estetykę ANSI, wydajność oraz trwały zapis danych.

### 👨‍💻 Informacje o Autorze
* **Autor:** Sebastian Januchowski
* **Brand:** polsoft.ITS London
* **GitHub:** [seb07uk](https://github.com/seb07uk)
* **Email:** polsoft.its@fastservice.com

---

## 🧩 Sekcja: Moduły Systemowe (CLI Plugins)
Poniższe pliki to moduły wtyczkowe zoptymalizowane pod kątem współpracy z centralnym systemem sterowania (`cli.py`). Wykorzystują wspólny dekorator `@command` oraz spójną paletę kolorów.

* **Calculator Pro (module):** Wersja wtyczkowa z historią operacji w `%userprofile%\.polsoft\psCli\Calculator\`.
* **psBrowser CLI (module):** Przeglądarka tekstowa z obsługą ciasteczek, snapshotów stron i historii w JSON.
* **Games Menu:** Centralny hub rozrywki, który dynamicznie skanuje folder gier i uruchamia je w nowych oknach.
* **print (module):** Zaawansowany czytnik plików z podświetlaniem składni (Python, JSON, MD) i stronicowaniem.
* **file list generator:** Narzędzie do skanowania struktur katalogów z synchronizacją ustawień globalnych.
* **echo (module):** Prosty moduł diagnostyczny do wyświetlania kolorowych komunikatów systemowych.

---

## 🛠️ Sekcja: Narzędzia (Standalone Utilities)

### 📂 CMD File Manager v1.5.0
Lekki menedżer plików z systemem potwierdzeń. Pozwala na kopiowanie, przenoszenie, usuwanie zasobów oraz szybki dostęp do folderów systemowych.

### 🎨 Paint Cli v1.0
Edytor grafiki ASCII działający w trybie tekstowym. Obsługuje paletę kolorów ANSI, różne pędzle oraz eksport projektów do plików `.txt`.

### 📝 Simple Notepad v1.5
Notatnik z nawigacją klawiszową (W/S) i systemem Auto-save. Idealny do szybkich notatek bez opuszczania terminala.

### 🖼️ ICON TOOL - Icon Manager
Narzędzie do zarządzania zasobami graficznymi: wyodrębnianie ikon z `.exe`/`.dll`, konwersja obrazów na format `.ico` oraz budowanie bibliotek ikon.

---

## 🎮 Sekcja: Gry (Entertainment)

| Tytuł | Opis | Cechy |
| :--- | :--- | :--- |
| **Snake CLI** | Klasyczny wąż retro | 3 poziomy trudności, system skórek, ranking TOP 5. |
| **Hangman** | Gra w wisielca | Tryb VS CPU oraz Multiplayer (ukryte wpisywanie hasła). |
| **Tic-Tac-Toe** | Kółko i Krzyżyk | Efekty dźwiękowe `winsound`, logowanie historii meczów. |
| **Rock-Paper-Scissors** | Kamień-Papier-Nożyce | System statystyk, obsługa języków PL/EN. |

---

## ⚙️ Architektura Danych i Ścieżki
System korzysta ze spójnej hierarchii folderów w katalogu użytkownika, co ułatwia backup i zarządzanie ustawieniami:

* **Główny folder danych:** `%USERPROFILE%\.polsoft\`
* **Ustawienia globalne:** `...\psCli\settings\terminal.json`
* **Historia i Logi:** `...\psCli\History\`
* **Zasoby gier:** `...\psCli\Games\`

---

### 💻 Wymagania Techniczne
1.  **Interpreter:** Python 3.x
2.  **System:** Windows (wykorzystanie bibliotek `msvcrt`, `winsound` oraz `ctypes` dla kolorów ANSI).
3.  **Terminal:** Zalecany **Windows Terminal** lub PowerShell (wspierający sekwencje kolorów).
4.  **Zależności:** `Pillow` (wymagane tylko dla modułu *Icon Tool*).

---
*2026© polsoft.ITS London | Created by Sebastian Januchowski*