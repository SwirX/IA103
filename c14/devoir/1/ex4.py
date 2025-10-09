# c = 4
# for i in range(1, 11, 2):
#     print(f'{" "*c}{"*"*i}')
#     c -= 1

# un example ou on 'compute' les espaces 'in runtime'
for i in range(1, 11, 2):
    print(f'{" " * ((9 - i) // 2)}{"*" * i}')