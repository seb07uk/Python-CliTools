"""
Snake Game - Classic Console Snake
===================================
A simple console-based Snake game implementation.

Author: Sebastian Januchowski
Email: polsoft.its@fastservice.com
GitHub: https://github.com/seb07uk
Company: polsoft.ITS™ London
Copyright: 2026© Sebastian Januchowski. All rights reserved.
"""

import os
import sys
import time
import random
try:
    import msvcrt  # Windows only
    WINDOWS = True
except ImportError:
    import tty
    import termios
    WINDOWS = False

# ANSI Colors
G = "\033[92m"
R = "\033[91m"
Y = "\033[93m"
B = "\033[94m"
C = "\033[36m"
RESET = "\033[0m"
BOLD = "\033[1m"

class SnakeGame:
    def __init__(self):
        self.width = 40
        self.height = 20
        self.snake = [(self.height // 2, self.width // 2)]
        self.direction = 'RIGHT'
        self.food = self.spawn_food()
        self.score = 0
        self.running = True
        self.game_over = False
    
    def spawn_food(self):
        while True:
            food = (random.randint(1, self.height - 2), random.randint(1, self.width - 2))
            if food not in self.snake:
                return food
    
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def draw(self):
        self.clear_screen()
        
        # Header
        print(f"{G}{BOLD}╔═══════════════════════════════════════════════════════════╗{RESET}")
        print(f"{G}{BOLD}║                  SNAKE GAME - Console Edition             ║{RESET}")
        print(f"{G}{BOLD}╠═══════════════════════════════════════════════════════════╣{RESET}")
        print(f"{G}{BOLD}║  Score: {self.score:<5}  |  Controls: WASD or Arrow Keys            ║{RESET}")
        print(f"{G}{BOLD}╚═══════════════════════════════════════════════════════════╝{RESET}\n")
        
        # Game board
        for row in range(self.height):
            for col in range(self.width):
                if row == 0 or row == self.height - 1 or col == 0 or col == self.width - 1:
                    print(f"{B}#{RESET}", end='')
                elif (row, col) == self.snake[0]:
                    print(f"{G}O{RESET}", end='')
                elif (row, col) in self.snake:
                    print(f"{G}o{RESET}", end='')
                elif (row, col) == self.food:
                    print(f"{R}*{RESET}", end='')
                else:
                    print(' ', end='')
            print()
        
        print(f"\n{Y}Press 'Q' to quit{RESET}")
    
    def get_key(self):
        if WINDOWS:
            if msvcrt.kbhit():
                key = msvcrt.getch().decode('utf-8').upper()
                return key
        else:
            # Non-blocking input for Unix
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                import select
                if select.select([sys.stdin], [], [], 0)[0]:
                    key = sys.stdin.read(1).upper()
                    return key
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return None
    
    def update(self):
        head_row, head_col = self.snake[0]
        
        # Move based on direction
        if self.direction == 'UP':
            new_head = (head_row - 1, head_col)
        elif self.direction == 'DOWN':
            new_head = (head_row + 1, head_col)
        elif self.direction == 'LEFT':
            new_head = (head_row, head_col - 1)
        elif self.direction == 'RIGHT':
            new_head = (head_row, head_col + 1)
        
        # Check wall collision
        if (new_head[0] <= 0 or new_head[0] >= self.height - 1 or
            new_head[1] <= 0 or new_head[1] >= self.width - 1):
            self.game_over = True
            return
        
        # Check self collision
        if new_head in self.snake:
            self.game_over = True
            return
        
        # Move snake
        self.snake.insert(0, new_head)
        
        # Check food
        if new_head == self.food:
            self.score += 10
            self.food = self.spawn_food()
        else:
            self.snake.pop()
    
    def run(self):
        self.clear_screen()
        print(f"{G}{BOLD}SNAKE GAME{RESET}")
        print(f"{Y}Author: Sebastian Januchowski{RESET}")
        print(f"{C}polsoft.ITS™ London{RESET}\n")
        print("Controls:")
        print("  W or ↑ - Move Up")
        print("  S or ↓ - Move Down")
        print("  A or ← - Move Left")
        print("  D or → - Move Right")
        print("  Q - Quit\n")
        input("Press Enter to start...")
        
        while self.running and not self.game_over:
            self.draw()
            
            # Get input
            key = self.get_key()
            if key:
                if key == 'Q':
                    self.running = False
                elif key in ['W', '\x1b[A'] and self.direction != 'DOWN':
                    self.direction = 'UP'
                elif key in ['S', '\x1b[B'] and self.direction != 'UP':
                    self.direction = 'DOWN'
                elif key in ['A', '\x1b[D'] and self.direction != 'RIGHT':
                    self.direction = 'LEFT'
                elif key in ['D', '\x1b[C'] and self.direction != 'LEFT':
                    self.direction = 'RIGHT'
            
            self.update()
            time.sleep(0.15)
        
        # Game over screen
        self.clear_screen()
        print(f"\n{R}{BOLD}╔═══════════════════════════════════════════════════════════╗{RESET}")
        print(f"{R}{BOLD}║                      GAME OVER!                           ║{RESET}")
        print(f"{R}{BOLD}╠═══════════════════════════════════════════════════════════╣{RESET}")
        print(f"{R}{BOLD}║  Final Score: {self.score:<5}                                       ║{RESET}")
        print(f"{R}{BOLD}╚═══════════════════════════════════════════════════════════╝{RESET}\n")
        print(f"{Y}Thank you for playing!{RESET}")
        print(f"{C}© 2026 Sebastian Januchowski - polsoft.ITS™ London{RESET}\n")
        input("Press Enter to exit...")

if __name__ == "__main__":
    try:
        game = SnakeGame()
        game.run()
    except KeyboardInterrupt:
        print(f"\n{Y}Game interrupted{RESET}")
    except Exception as e:
        print(f"{R}Error: {e}{RESET}")
