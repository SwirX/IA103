class Chambre:
    def __init__(self, numero:int, _type:str, prix_nuit:float, disponible:bool=True):
        self.numero = numero
        self.type = _type
        self.prix_nuit = prix_nuit
        self.disponible = disponible

    def afficher_details(self):
        print(f'{'Disponible' if self.disponible else 'Non Disponible'}\nChambre: {self.numero}, de type: {self.type}\n{self.prix_nuit}DH/nuit')

    def __str__(self):
        return f'{"-"*15}\nStatus: {'Disponible' if self.disponible else 'Non Disponible'}\nChambre: {self.numero}, de type: {self.type}\n{self.prix_nuit}DH/nuit\n{"-"*15}'
