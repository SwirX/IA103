# c = 4
# for i in range(1, 11, 2):
#     print(f'{" "*c}{"*"*i}')
#     c -= 1
# c = 1
# for i in range(7, -1, -2):
#     print(f'{" "*c}{"*"*i}')
#     c += 1

for n in range(-4, 5):
    i = 9 - abs(n) * 2
    c = abs(n)
    print(f'{" " * c}{"*" * i}')
