class Livre:
    def __init__(self, titre, auteur, prix):
        self.titre = titre
        self.auteur = auteur
        self.__prix = prix
    
    @property
    def prix(self):
        return self.__prix
    
    @prix.setter
    def prix(self, v):
        self.__prix = abs(v)

    def __str__(self):
        return f'Titre: {self.titre}, Auteur: {self.auteur}, Prix: {self.__prix}'
    
    def __dict__(self):
        return {
            "titre": self.titre,
            "auteur": self.auteur,
            "prix": self.__prix,
        }
