class Eleve:
    def __init__(self, nom, niveau):
        self.nom = nom
        self.niveau = niveau

    def afficher_infos(self):
        print(f'Nom: {self.nom}, Niveau: {self.niveau}')


