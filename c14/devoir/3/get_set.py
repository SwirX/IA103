def ex1():
    class Employe:
        def __init__(self, nom:str, salaire:int):
            self.__nom = nom
            self.__salaire = salaire
            
        @property
        def nom(self):
            return self.__nom
        
        @nom.setter
        def nom(self, nouveau_nom:str):
            self.__nom = nouveau_nom
        
        def afficher_info(self):
            print(f"Nom: {self.__nom}, Salaire: {self.__salaire}")
    
    
    emp = Employe("Alii", 50000)
    emp.afficher_info()
    emp.nom = "Ali"
    emp.afficher_info()
    emp2 = Employe("Othmane", 60000)
    emp2.afficher_info()
    emp2.__nom = "Othman"
    emp2.afficher_info()
    print("Nom via getter:", emp2.nom)

def ex2():
    class Voiture:
        def __init__(self):
            self.__vitesse = 0
        
        def afficher_vitesse(self):
            print(f"Vitesse: {self.__vitesse} km/h")
        
        def accelerer(self, increment:int):
            self.__vitesse = min(200, self.__vitesse + abs(increment))
        
        def decelerer(self, decrement:int):
            self.__vitesse = max(0, self.__vitesse - abs(decrement))
    
    voiture = Voiture()
    voiture.afficher_vitesse()
    voiture.accelerer(30)
    voiture.afficher_vitesse()
    voiture.decelerer(100)
    voiture.afficher_vitesse()
    voiture.accelerer(300)
    voiture.afficher_vitesse()

def ex3():
    class CompteBancaire:
        def __init__(self, solde:int=0):
            self.__solde = solde
        
        @property
        def solde(self):
            return self.__solde
        
        @solde.setter
        def solde(self, nouveau_solde):
            if nouveau_solde >= 0:
                self.__solde = nouveau_solde
        
        def deposer(self, montant):
            if montant > 0:
                self.__solde += montant
        
        def retirer(self, montant):
            if 0 < montant <= self.__solde:
                self.__solde -= montant
                
    compte = CompteBancaire()
    compte.solde = 1000
    print(compte.solde)
    compte.deposer(500)
    print(compte.solde)
    compte.retirer(1250)
    print(compte.solde)
    compte.retirer(1000)
    print(compte.solde)

if __name__ == "__main__":
    ex = [ex1, ex2, ex3]
    for i, fn in enumerate(ex):
        print(f"--- Exercice {i+1} ---")
        fn()
        print()
