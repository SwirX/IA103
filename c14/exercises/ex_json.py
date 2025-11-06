import json

def ex1():
    p = {"nom": "Ordinateur", "prix": 7500, "stock": 12}
    with open('produit.json', 'w+') as f:
        json.dump(p, f)

def ex2():
    with open('produit.json') as f:
        p:dict = json.load(f)
        print(f'Produit: {p["nom"]}')
        print(f'Prix: {p["prix"]} DH')
        print(f'Stock Disponible: {p["stock"]}')

def ex3():
    e = [
            {
                'name': 'Ali',
                'grades': [18,19, 17, 19, 19]
            },
            {
                'name': 'Taha',
                'grades': [20, 17, 17, 18, 19]
            },
            {
                'name': 'Wadie',
                'grades': [17, 18, 17, 19, 18]
            }
        ]
    with open('etudiants.json', 'w+') as f:
        json.dump(e, f)

    with open('etudiants.json') as f:
        e = json.load(f)
        for etu in e:
            g = etu['grades']
            n = etu['name']
            avg = sum(g)/len(g)
            print(f'{n}\nMoyenne: {avg}\n{"-"*10}')

if __name__ == '__main__':
    ex = [ex1, ex2, ex3]
    for i, v in enumerate(ex):
        print(f'Exercice {i+1}')
        v()
        print('\n')
        input('Enter to continue\n')
