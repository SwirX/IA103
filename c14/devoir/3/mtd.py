class Produit:
    def __init__(self, nom:str, prix:float):
        self.nom = nom
        self.prix = prix
    
    def __str__(self):
        return f"Produit: {self.nom}, Prix: {self.prix} MAD"
        

def ex1():
    produit = Produit("Ordinateur", 9999.99)
    print(produit)
    produit2 = Produit("Smartphone", 4999.49)
    print(produit2)
    
def ex2():
    class Voiture:
        def __init__(self, marque:str, modele:str, annee:int, couleur:str):
            self.marque = marque
            self.modele = modele
            self.annee = annee
            self.couleur = couleur
        
        def __dict__(self):
            return {
                "marque": self.marque,
                "modele": self.modele,
                "annee": self.annee,
                "couleur": self.couleur
            }
        
    voiture = Voiture("Toyota", "Corolla", 2020, "Rouge")
    print(voiture.__dict__())
    voiture.couleur = "Bleu"
    print(voiture.__dict__())
    
def ex3():
    produit = Produit("Tablette", 2999.99)
    print('dunder mtds: ', [i for i in dir(produit) if i.startswith('__') and i.endswith('__')])
    # __init__ pour l'initialisation
    # __str__ pour la représentation en chaîne de caractères
    # __dict__ pour obtenir les attributs de l'objet sous forme de dictionnaire
    

if __name__ == "__main__":
    ex = [ex1, ex2, ex3]
    for i, fn in enumerate(ex):
        print(f"--- Exercice {i+1} ---")
        fn()
        print()