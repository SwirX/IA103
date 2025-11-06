from .compte import Compte

class Client:
    def __init__(self, nom:str, compte:Compte):
        self.nom:str = nom
        self.compte:Compte = compte
    
    def afficher_info(self):
        print(f"Client: {self.nom}, Solde: {self.compte.solde} MAD")