def ex1():
    def carre(x):
        return x*x

    # ex usage
    print(f"5^2 = {carre(5)}")
    return

def ex2():
    def maximum(a, b):
        return max(a, b) # if a>b -> a else -> b

    # ex usage
    print(f"max entre 1 et 2: {maximum(1, 2)}")
    return

def ex3():
    def est_pair(n):
        return n % 2 == 0

    # ex usage:
    print(f"0 pair? {est_pair(0)}")
    print(f"1 pair? {est_pair(1)}")
    return

def ex4():
    def conversion(celsius):
        return celsius * 9/5 + 32

    # ex usage
    print(f"0C -> {conversion(0)}F")
    return

def ex5():
    def sub(x, y):
        return x - y
    
    def quotient(x, y):
        return x / y
    try:
        a, b = [int(i) for i in input("Entrer deux nombres separes par (,): ").split(",")]
        sum_ab = sum([a, b])
        sub_ab = sub(a, b)
        div_ab = quotient(a, b)
        print(f"Somme: {sum_ab}")
        print(f"Difference: {sub_ab}")
        print(f"Quotient: {div_ab}")
        return
    except Exception:
        print("input should be as <num1>,<num2>")


def ex6():
    cube = lambda a: a**3
    somme = lambda a, b: a+b
    v_abs = lambda a: abs(a)
    
    print(f"2^3 = {cube(2)}")
    print(f"0+1 = {somme(0, 1)}")
    print(f"abs(-1) = {v_abs(-1)}")

def ex7():
    etudiants = [("Ali", 14), ("Ayoub", 18), ("Omar", 10), ("Taha", 16)]
    sorted_list = sorted(etudiants, key=lambda x: x[1], reverse=True)
    
    # usage
    print(sorted_list)
    return

if __name__ == "__main__":
    print("\nEX1\n")
    ex1()
    input("Press enter to continue")
    print("\nEX2\n")
    ex2()
    input("Press enter to continue")
    print("\nEX3\n")
    ex3()
    input("Press enter to continue")
    print("\nEX4\n")
    ex4()
    input("Press enter to continue")
    print("\nEX5\n")
    ex5()
    input("Press enter to continue")
    print("\nEX6\n")
    ex6()
    input("Press enter to continue")
    print("\nEX7\n")
    ex7()
    print("Au revoir!")
