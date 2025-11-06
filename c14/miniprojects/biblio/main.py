from core.livre import Livre
from core.bibliotheque import Bibliotheque


b = Bibliotheque()

l1 = Livre('livre1', 'auteur1', 500)
l2 = Livre('livre2', 'auteur2', 250)
l3 = Livre('livre3', 'auteur1', 500)

print(l2.__dict__())
l2.prix = -500
print(l2.__dict__())

print()
b.ajouter_livre(l1, l2, l3)

b.afficher_livres()

b.suprimer_livre(l3)
