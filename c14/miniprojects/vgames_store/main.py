class JeuVideo:
    total_jeu = 0

    def __init__(self, titre, prix, stc):
        self.__titre = titre
        self.__prix = prix
        self.__stock = stc
        
        self.total_jeu += 1

        @property
        def price(self):
            return self.__prix

        @property
        def stock(self):
            return self.__stock

        @stock.setter
        def stock(self, v):
            self.__stock = abs(v)

        @price.setter
        def price(self, v):
            self.__prix = abs(v)

        

    def vendre(self):
        if self.__stock > 0:
            self.__stock -= 1
            print(f'Sold {self.__titre}\nstock remaning: {self.__stock}')
        else:
            print('Cannot sell: No stock remaining')
    
    def approvisionner(self, qte):
        self.__stock += qte
        print(f'Restocked {qte} items for {self.__titre}')

    def afficher_info(self):
        print(f'Game title: {self.__titre}, Price: {self.__prix}, Stock: {self.__stock}')

    def __str__(self):
        return f'Game title: {self.__titre}, Price: {self.__prix}, Stock: {self.__stock}'


g1 = JeuVideo('game1', 600, 50)
g2 = JeuVideo('game2', 450, 1)
g3 = JeuVideo('game3', 800, 15)


for i in (g1, g2, g3):
    print(i)

g2.vendre()
g2.vendre()

g2.approvisionner(10)
g2.vendre()

