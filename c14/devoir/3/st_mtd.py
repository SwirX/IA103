def ex1():
    class MathUtils:

        @staticmethod
        def carre(n):
            return n*n

        @staticmethod
        def cube(n):
            return n*n*n

    print(MathUtils.carre(2))
    print(MathUtils.cube(2))

def ex2():
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


def ex3():
    class Temperature:

        @staticmethod
        def celsius_vers_fahrenheit(celsius):
            return (celsius * 9/5) + 32

        @staticmethod
        def fahrenheit_vers_celsius(fahrenheit):
            return (fahrenheit - 32) * 5/9
        
    print(Temperature.celsius_vers_fahrenheit(0))
    print(Temperature.fahrenheit_vers_celsius(32))
