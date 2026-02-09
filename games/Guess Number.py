"""
Number Guessing Game
====================
Guess the secret number between 1 and 100!

Author: Sebastian Januchowski
Email: polsoft.its@fastservice.com
GitHub: https://github.com/seb07uk
Company: polsoft.ITS™ London
Copyright: 2026© Sebastian Januchowski. All rights reserved.
"""

import os
import random

# ANSI Colors
G = "\033[92m"
R = "\033[91m"
Y = "\033[93m"
B = "\033[94m"
C = "\033[36m"
RESET = "\033[0m"
BOLD = "\033[1m"
GRAY = "\033[90m"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def play_game():
    clear_screen()
    
    print(f"{B}{BOLD}╔═══════════════════════════════════════════════════════════╗{RESET}")
    print(f"{B}{BOLD}║              NUMBER GUESSING GAME                         ║{RESET}")
    print(f"{B}{BOLD}╠═══════════════════════════════════════════════════════════╣{RESET}")
    print(f"{B}{BOLD}║  {Y}Guess the secret number between 1 and 100!{RESET}               {B}{BOLD}║{RESET}")
    print(f"{B}{BOLD}╠═══════════════════════════════════════════════════════════╣{RESET}")
    print(f"{B}{BOLD}║  Author: {C}Sebastian Januchowski{RESET}                            {B}{BOLD}║{RESET}")
    print(f"{B}{BOLD}║  {GRAY}2026© polsoft.ITS™ London{RESET}                                {B}{BOLD}║{RESET}")
    print(f"{B}{BOLD}╚═══════════════════════════════════════════════════════════╝{RESET}\n")
    
    # Game settings
    min_num = 1
    max_num = 100
    secret_number = random.randint(min_num, max_num)
    attempts = 0
    max_attempts = 10
    
    print(f"{C}[i] You have {max_attempts} attempts to guess the number{RESET}")
    print(f"{C}[i] The number is between {min_num} and {max_num}{RESET}\n")
    
    while attempts < max_attempts:
        try:
            guess = int(input(f"{Y}Attempt {attempts + 1}/{max_attempts} - Enter your guess: {RESET}"))
            attempts += 1
            
            if guess < min_num or guess > max_num:
                print(f"{R}[!] Please enter a number between {min_num} and {max_num}{RESET}\n")
                attempts -= 1
                continue
            
            if guess == secret_number:
                print(f"\n{G}{BOLD}╔═══════════════════════════════════════════════════════════╗{RESET}")
                print(f"{G}{BOLD}║                  CONGRATULATIONS!                         ║{RESET}")
                print(f"{G}{BOLD}╠═══════════════════════════════════════════════════════════╣{RESET}")
                print(f"{G}{BOLD}║  You guessed the number {secret_number} in {attempts} attempts!{RESET}          {G}{BOLD}║{RESET}")
                print(f"{G}{BOLD}╚═══════════════════════════════════════════════════════════╝{RESET}\n")
                break
            elif guess < secret_number:
                print(f"{Y}[→] Too low! Try a higher number{RESET}\n")
            else:
                print(f"{Y}[←] Too high! Try a lower number{RESET}\n")
            
            # Show remaining attempts
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"{C}[i] {remaining} attempts remaining{RESET}\n")
        
        except ValueError:
            print(f"{R}[!] Please enter a valid number{RESET}\n")
            attempts -= 1
    
    else:
        print(f"\n{R}{BOLD}╔═══════════════════════════════════════════════════════════╗{RESET}")
        print(f"{R}{BOLD}║                    GAME OVER!                             ║{RESET}")
        print(f"{R}{BOLD}╠═══════════════════════════════════════════════════════════╣{RESET}")
        print(f"{R}{BOLD}║  The secret number was: {secret_number}{RESET}                          {R}{BOLD}║{RESET}")
        print(f"{R}{BOLD}╚═══════════════════════════════════════════════════════════╝{RESET}\n")

def main():
    while True:
        play_game()
        
        play_again = input(f"{G}Play again? (y/n): {RESET}").lower().strip()
        if play_again != 'y':
            break
        clear_screen()
    
    print(f"\n{G}Thank you for playing!{RESET}")
    print(f"{GRAY}© 2026 Sebastian Januchowski - polsoft.ITS™ London{RESET}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Y}Game interrupted{RESET}")
    except Exception as e:
        print(f"{R}Error: {e}{RESET}")
