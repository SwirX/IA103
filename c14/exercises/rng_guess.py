from random import randint

running = True
while running:
    guess = input("Guess a number > ")
    if guess == "q":
        running = False
    else:
        try:
            rng = randint(1, 10)
            if int(guess) == rng:
                print('spot on!')
            else:
                print(f'Wrong it was {rng}! Better luck next time!')
        except Exception:
            print('Enter a number or (q)uit')

print('Goodbye!')
