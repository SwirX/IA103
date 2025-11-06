class Compte:
    def __init__(self, numero:int, solde:int=0):
        self.numero = numero
        self.solde = solde
    
    def deposer(self, montant:int):
        if montant > 0:
            self.solde += montant
    def retirer(self, montant:int):
        if 0 < montant <= self.solde:
            self.solde -= montant
    
    def afficher_solde(self):
        print(f"Compte {self.numero} - Solde: {self.solde} MAD")