class MathUtils:

    @staticmethod
    def carre(n):
        return n*n

    @staticmethod
    def cube(n):
        return n*n*n

#print(MathUtils.carre(2))
#print(MathUtils.cube(2))

class Employe:
    count = 0
    def __init__(self):
        Employe.count += 1

    @classmethod
    def nbr_empl(cls):
        return cls.count


e = Employe()
e2 = Employe()
e3 = Employe()
print(Employe.count)
