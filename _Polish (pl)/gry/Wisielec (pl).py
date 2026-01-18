import random
import os
import getpass  # Do ukrycia wpisywanego hasła

# Ścieżki
BASE_DIR = os.path.expandvars(r'%userprofile%\.polsoft\games')
SCORE_FILE = os.path.join(BASE_DIR, "hiscores.txt")

def inicjalizuj():
    if not os.path.exists(BASE_DIR):
        os.makedirs(BASE_DIR)

def wyczysc_ekran():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_hangman_art(index):
    etapy = [
        """
           +-------+
           |       |
                   |
                   |
                   |
                   |
        ==============
        """,
        """
           +-------+
           |       |
           O       |
                   |
                   |
                   |
        ==============
        """,
        """
           +-------+
           |       |
           O       |
           |       |
                   |
                   |
        ==============
        """,
        """
           +-------+
           |       |
           O       |
          /|       |
                   |
                   |
        ==============
        """,
        """
           +-------+
           |       |
           O       |
          /|\\      |
                   |
                   |
        ==============
        """,
        """
           +-------+
           |       |
           O       |
          /|\\      |
          /        |
                   |
        ==============
        """,
        """
           +-------+
           |       |
           O       |
          /|\\      |
          / \\      |
                   |
        ==============
        """
    ]
    return etapy[index]

def logo():
    return """
    _    _                                         
   | |  | |                                        
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
   |  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                        __/ |                      
                       |___/                       
    """

def zapisz_i_sortuj_wynik(nick, punkty):
    wyniki = []
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "r") as f:
            for linia in f.readlines()[1:]:
                if ":" in linia:
                    try:
                        name_part = linia.split(". ")[1]
                        name = name_part.split(":")[0].strip()
                        score = int(name_part.split(":")[1].replace(" pkt", "").strip())
                        wyniki.append((name, score))
                    except:
                        continue

    wyniki.append((nick, punkty))
    wyniki.sort(key=lambda x: x[1], reverse=True)

    with open(SCORE_FILE, "w") as f:
        f.write("--- TOP 10 REKORDÓW ---\n")
        for i, (n, p) in enumerate(wyniki[:10], 1):
            f.write(f"{i}. {n}: {p} pkt\n")

def pokaz_hiscore():
    wyczysc_ekran()
    print("\033[93m" + "╔════════════════════════════════════╗")
    print("║          TABELA REKORDÓW           ║")
    print("╚════════════════════════════════════╝\033[0m")

    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "r") as f:
            print(f.read())
    else:
        print("Brak zapisanych wyników.")

    input("\nNaciśnij Enter...")

def pomoc():
    wyczysc_ekran()

    print("\033[96m" + "═══════════════════════════════════════════════")
    print("                 P O M O C")
    print("═══════════════════════════════════════════════\033[0m\n")

    # CEL GRY
    print("\033[93m▶ CEL GRY\033[0m")
    print("Twoim zadaniem jest odgadnięcie ukrytego hasła, zanim licznik błędów osiągnie maksymalny poziom.\n")

    # TRYBY GRY
    print("\033[92m▶ TRYBY GRY\033[0m")
    print("\033[92m1. Tryb 1 Gracz (VS CPU)\033[0m")
    print("   • Gra losuje hasło.")
    print("   • Zdobywasz punkty za trafione litery.")
    print("   • Otrzymujesz bonus za niewykorzystane życia.\n")

    print("\033[92m2. Tryb 2 Graczy (VS Player)\033[0m")
    print("   • Gracz 1 wpisuje hasło (ukryte).")
    print("   • Gracz 2 zgaduje litery.\n")

    # PUNKTACJA
    print("\033[95m▶ PUNKTACJA\033[0m")
    print("   • \033[92m+10 pkt\033[0m za każdą trafioną literę.")
    print("   • \033[96mBonus:\033[0m (6 – liczba błędów) × 25 pkt.")
    print("   • Wyniki zapisywane są w tabeli rekordów (TOP 10).\n")

    # ZASADY
    print("\033[94m▶ ZASADY\033[0m")
    print("   • Podajesz pojedynczą literę.")
    print("   • Litery muszą być alfabetu łacińskiego.")
    print("   • Litery już użyte nie mogą być powtórzone.\n")

    # HISCORE
    print("\033[91m▶ TABELA WYNIKÓW\033[0m")
    print("   • Zapisywana w: \033[93m%userprofile%\\.polsoft\\games\\hiscores.txt\033[0m")
    print("   • Automatyczne sortowanie wyników.\n")

    # KONIEC GRY
    print("\033[90m▶ KONIEC GRY\033[0m")
    print("   • Wygrana: odgadnięcie hasła.")
    print("   • Przegrana: 6 błędów.\n")

    # STEROWANIE
    print("\033[96m▶ STEROWANIE\033[0m")
    print("   • W menu wybierasz numer opcji.")
    print("   • W grze wpisujesz litery i zatwierdzasz Enterem.\n")

    # STOPKA
    print("\033[90m" + "─" * 55 + "\033[0m")
    print("\033[97m" + " " * 15 + "Sebastian Januchowski")
    print(" " * 15 + "polsoft.its@fastservice.com")
    print(" " * 15 + "https://github.com/seb07uk")
    print(" " * 15 + "2026© polsoft.ITS London\033[0m")
    print("\033[90m" + "─" * 55 + "\033[0m\n")

    input("Naciśnij Enter...")

def silnik_gry(slowo, tryb_2_graczy=False):
    odgadniete = []
    bledy = 0
    max_bledow = 6
    punkty_za_litery = 0

    while bledy < max_bledow:
        wyczysc_ekran()
        print("\033[96m" + logo() + "\033[0m")

        if tryb_2_graczy:
            print("         [ TRYB 2 GRACZY ]")

        print(get_hangman_art(bledy))

        stan = "".join([f" {l} " if l in odgadniete else " _ " for l in slowo])
        print(f"\n   HASŁO: {stan}")
        print(f"\n   BŁĘDY: {bledy}/{max_bledow}  |  PUNKTY: {punkty_za_litery}")
        print(f"   UŻYTE: {', '.join(odgadniete)}")
        print("   " + "─" * 40)

        if "_" not in stan:
            total = punkty_za_litery + (max_bledow - bledy) * 25
            print(f"\n\033[92m   ZWYCIĘSTWO! FINALNY WYNIK: {total}\033[0m")
            nick = input("   Podaj nick zwycięzcy: ")
            zapisz_i_sortuj_wynik(nick, total)
            return

        strzal = input("\n   Podaj literę > ").upper()
        if len(strzal) != 1 or not strzal.isalpha() or strzal in odgadniete:
            continue

        odgadniete.append(strzal)

        if strzal in slowo:
            punkty_za_litery += slowo.count(strzal) * 10
        else:
            bledy += 1

    wyczysc_ekran()
    print(get_hangman_art(6))
    print(f"\033[91m   KONIEC GRY. HASŁO: {slowo}\033[0m")
    nick = input("   Podaj nick (mimo przegranej): ")
    zapisz_i_sortuj_wynik(nick, punkty_za_litery)

def menu():
    inicjalizuj()
    while True:
        wyczysc_ekran()
        print("\033[95m" + logo() + "\033[0m")
        print("       [1] NOWA GRA (VS CPU)")
        print("       [2] 2 GRACZY (VS PLAYER)")
        print("       [3] HI-SCORE")
        print("       [4] POMOC")
        print("       [5] WYJŚCIE")
        print("\n" + "       " + "═" * 25)

        wybor = input("\n       WYBIERZ: ")

        if wybor == "1":
            slowa = ["PYTHON", "TERMINAL", "SKRYPT", "KODOWANIE", "INTERFEJS", "SYSTEM"]
            silnik_gry(random.choice(slowa))

        elif wybor == "2":
            wyczysc_ekran()
            print("\033[93m" + "=== TRYB 2 GRACZY ===\033[0m")
            print("Graczu 1, wpisz hasło do odgadnięcia (tekst będzie ukryty):")
            haslo = getpass.getpass("Hasło: ").upper()

            if haslo.isalpha() and len(haslo) > 0:
                silnik_gry(haslo, tryb_2_graczy=True)
            else:
                print("Błędne hasło! Musi zawierać tylko litery.")
                input("Naciśnij Enter...")

        elif wybor == "3":
            pokaz_hiscore()

        elif wybor == "4":
            pomoc()

        elif wybor == "5":
            break

if __name__ == "__main__":
    menu()