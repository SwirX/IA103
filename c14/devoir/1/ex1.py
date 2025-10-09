# running = True

# while running:
#     n1, n2 = int(input("Entrer 1er nombre: ")), int(input("Entrer 2eme nombre: "))
#     op = input("Entrer une operation: ").lower()

#     if op in ['+', 'addition']:
#         print(n1+n2)
#     elif op in ['-', 'soustraction']:
#         print(n1-n2)
#     elif op in ['*', 'x', 'multiplication']:
#         print(n1*n2)
#     elif op in ['/', 'division']:
#         if n2 == 0:
#             print('On peut pas diviser par 0')
#         else:
#             print(n1/n2)
#     elif op in ['**', '^', 'exponentiel']:
#         print(n1**n2)
    
#     if input("continue? (y/N)").lower() in ['y', 'yes']:
#         print(f"\n{'#'*10}\n")
#         continue
#     else:
#         running = False

# print("Au revoir")


# example sans les elif statements car j'aime pas en avoir beaucoup

# ops = {
#     '+': lambda a, b: a + b,
#     'addition': lambda a, b: a + b,
#     '-': lambda a, b: a - b,
#     'soustraction': lambda a, b: a - b,
#     '*': lambda a, b: a * b,
#     'x': lambda a, b: a * b,
#     'multiplication': lambda a, b: a * b,
#     '/': lambda a, b: a / b if b != 0 else "On peut pas diviser par 0",
#     'division': lambda a, b: a / b if b != 0 else "On peut pas diviser par 0",
#     '**': lambda a, b: a ** b,
#     '^': lambda a, b: a ** b,
#     'exponentiel': lambda a, b: a ** b
# }

# while True:
#     n1, n2 = int(input("Entrer 1er nombre: ")), int(input("Entrer 2eme nombre: "))
#     op = input("Entrer une operation: ").lower()

#     print(ops[op](n1, n2) if op in ops else "Opération inconnue")
    
#     if input("continue? (y/N): ").lower() not in ['y', 'yes']:
#         break
#     print("\n" + "#"*10 + "\n")

# print("Au revoir")


# un autre example sans les eval redondantes car je prefere un code optimize
ops = {
    '+': 'add', 'addition': 'add',
    '-': 'sub', 'soustraction': 'sub',
    '*': 'mul', 'x': 'mul', 'multiplication': 'mul',
    '/': 'div', 'division': 'div',
    '**': 'pow', '^': 'pow', 'exponentiel': 'pow'
}

def calc(a, b, op):
    match op:
        case 'add': return a + b
        case 'sub': return a - b
        case 'mul': return a * b
        case 'div': return a / b if b != 0 else "On peut pas diviser par 0"
        case 'pow': return a ** b

while True:
    # n1 n2
    n1, n2 = map(int, input("Entrer 1er et 2eme nombre: ").split())
    op = input("Entrer une operation: ").lower()

    if op in ops:
        print(calc(n1, n2, ops[op]))
    else:
        print("Opération inconnue")

    if input("continue? (y/N): ").lower() not in ('y', 'yes'):
        break
    print("\n" + "#"*10 + "\n")

print("Au revoir")
