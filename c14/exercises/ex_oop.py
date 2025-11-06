def ex1():

    class livre:
        def __init__(self, titre:str, auteur:str, pages:int):
            self.titre:str = titre
            self.auteur:str = auteur
            self.pages:str = pages

        def __str__(self):
            return f'Titre: {self.titre}\nAuteur: {self.auteur}\nPages {self.pages}'


    l1 = livre('livre 1', 'auteur1', 500)
    l2 = livre('livre 2', 'auteur2', 250)

    print(l1)
    print(l2)
    return

def ex2():
    class CompteBancaire:
        def __init__(self, titulaire:str, solde:int =0):
            self.titulaire:str = titulaire
            self.solde:str = solde

        def deposer(self, montant:int) -> None:
            self.solde += montant
            return

        def retirer(self, montant:int) -> None:
            if montant <= self.solde:
                self.solde -= montant
            else:
                print('solde insufisant')
            return

        def afficher(self) -> None:
            print(f'Solde: {self.solde}')
            return

    cmpt = CompteBancaire('Ali')
    cmpt.deposer(500)
    cmpt.retirer(200)
    cmpt.afficher()

def ex3():
    class Animal:
        def __init__(self, name):
            self.name = name
            
            print(f'l\'animal {self.name} est ne')

        def __del__(self):
            print(f'l\'animal {self.name} est mort')

    chat = Animal('chat')
    chien = Animal('chien')
    lapin = Animal('lapin')
    del chat
    del chien

def ex4():
    class Voiture:
        roues = 4
        def __init__(self, marque:str, couleur:str):
            self.marque:str = marque
            self.couleur:str = couleur

        def __str__(self):
            return f'Roues: {self.roues}, marque {self.marque}, couleur: {self.couleur}'

    v1 = Voiture('voiture1', 'Red')
    v2 = Voiture('voiture2', 'Blue')
    v1.roues = 3
    Voiture.roues = 11
    print(v1)
    print(v2)
    v2.couleur = 'Magenta'
    print(v2)

def ex5():
    class Etudiant:
        def __init__(self, nom:str, age:int, notes:list[float] = []):
            self.nom:str = nom
            self.age:int = age
            self.notes:list[float] = notes

            print(f'etudiant {nom} a ete cree')

        def ajouter_note(self, note:float) -> None:
            self.notes.append(note)
            return

        def moyenne(self) -> float:
            return round(sum(self.notes)/len(self.notes) * 100) / 100

        def afficher_info(self) -> None:
            print(f'Nom: {self.nom}\nAge: {self.age}\nMoyenne: {self.moyenne()}\n')
            return

        def __del__(self):
            print(f'etudiant {self.nom} a ete suprime')

    e1 = Etudiant('etu1', 18)
    e2 = Etudiant('etu2', 18, [18, 19, 18])
    e1.ajouter_note(20)
    e1.ajouter_note(19)
    e1.ajouter_note(18)
    e1.afficher_info()
    e2.afficher_info()
    del e2

if __name__ == '__main__':
    ex = [ex1, ex2, ex3, ex4, ex5]
    for i, fn in enumerate(ex):
        print(f'Execice {i+1}')
        fn()
        print('\n\n')
