from hotel.chambre import Chambre
from hotel.reservation import Reservation

c1 = Chambre(1, 'test', 1000)
c2 = Chambre(2, 'test2', 1500)
print('Chambres: ')
print(c1)
print(c2)
print()

r = Reservation('Ali', c2, 5)
print()
print('Chambres: ')
print(c1)
print(c2)
