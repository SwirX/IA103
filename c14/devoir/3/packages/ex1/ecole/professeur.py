class Professeur:
    def __init__(self, nom, matiere):
        self.nom = nom
        self.matiere = matiere

    def afficher_infos(self):
        print(f'Prof: {self.nom}, Matiere: {self.matiere}')
