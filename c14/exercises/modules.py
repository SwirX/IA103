from math import sqrt, ceil, floor, sin, radians
from datetime import datetime
from random import randint
import os 

def ex1():
    print(sqrt(81), ceil(5.7), floor(5.7), sin(radians(90)))
    return

def ex2():
    print(datetime.now())
    return

def ex3():
    tries = 0
    while True:
        if randint(1, 100) == 50:
            print(f'got the number in {tries} tries')
            break
        tries += 1

def ex4():
    d = datetime.now()
    print(f'Aujourd\'hui nous sommes le {d.day}/{d.month}/{d.year}')
    return

def ex5():
    os.system('python rng_guessV2.py')

if __name__ == '__main__':
    ex = [ex1, ex2, ex3, ex4, ex5]
    for i, v in enumerate(ex):
        print('-'*30)
        print(f'Exercice {i+1}')
        v()
        print('\n')
        print('-'*30)
        input('Press Enter to continue')
