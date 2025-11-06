f1 = 'bonjour.txt'
f2 = 'nombres.txt'

def ex1():
    with open(f1, 'w+') as f:
        f.write('Bonjour\nJe decouvre la gestion des fichiers en python')

def ex2():
    with open(f1) as f:
        print(f.readlines())

def ex3():
    with open(f1, 'a') as f:
        f.write('\nC\'est facile d\'ecrire dans un fichier')

def ex4():
    with open(f2, 'w+') as f:
        f.write('\n'.join([str(i) for i in range(1, 11)]))

def ex5():
    with open(f2) as f:
        print(sum([int(i) for i in f.readlines()]))

if __name__ == '__main__':
    ex = [ex1, ex2, ex3, ex4, ex5]
    for i, v in enumerate(ex):
        print(f'Exercice {i+1}')
        v()
        print('\n')
        input()
