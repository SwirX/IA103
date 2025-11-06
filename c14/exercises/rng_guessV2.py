import os
from random import randint

tries = 0
running = True
rng_range = 100

def print_help():
    print("""
          Enter a number to start the game.
          commands:
          q/quit to quit
          h/help to show help
          """)

def clr_scr():
    os.system('cls') if os.name == 'nt' else os.system('clear')

rng = randint(1, rng_range)
clr_scr()
while running:
    guess = input('Guess a number > ')
    if guess in ['q', 'quit']:
        print('Goodbye!')
        running = False
    elif guess in ['h', 'help']:
        clr_scr()
        print_help()
    else:
        try:
            guess = int(guess)
            modifier = 'a bit'
            if abs(guess - rng) >= 10:
                modifier = 'a lot'
            if guess == rng:
                if tries == 0:
                    print('Spot on!')
                else:
                    print(f'You got it in {tries} tries')
                rng = randint(1, rng_range)
                if input('Enter to continue and q to quit\n') in ['q', 'quit']:
                    running = False
                modifier = 'a bit'
                if abs(guess - rng) >= 10:
                    modifier = 'a lot'
                    clr_scr()
                    tries = 0
                    print('Goodbye')
                else:
                    clr_scr()
            elif guess > rng:
                print(f'You over-shot {modifier} try again!')
            else:
                print(f'Try going {modifier} higher')
            tries += 1
        except Exception:
            print('Enter a number or use h for help')
