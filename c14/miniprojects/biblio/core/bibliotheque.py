from .livre import Livre

class Bibliotheque:
    def __init__(self):
        self.livres:list[Livre] = []

    def ajouter_livre(self, *livres:tuple[Livre]):
        for livre in livres:
            self.livres.append(livre)

    def suprimer_livre(self, livre:Livre):
        self.livres.remove(livre)

    def afficher_livres(self):
        for l in self.livres: print(l)


