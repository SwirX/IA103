from .chambre import Chambre

class Reservation:
    def __init__(self, nom_client:str, chambre:Chambre, nb_nuits:int):
        self.client = nom_client
        self.chambre = chambre
        self.nuits = nb_nuits

        self.chambre.disponible = False

        print(f'{nom_client} a reserve chambre {chambre.numero} pour {nb_nuits} nuits pour un total de {self.calculer_total()}')
        

    def calculer_total(self):
        return self.chambre.prix_nuit * self.nuits
