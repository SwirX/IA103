from banque.client import Client
from banque.compte import Compte

c1 = Compte("C123", 5000)
client1 = Client("Hassan", c1)
client1.afficher_infos()
c1.deposer(1000)
c1.retirer(2000)
client1.afficher_infos()