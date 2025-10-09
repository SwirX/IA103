# for i in range(2, 7):
#     s = ""
#     for j in range(1, i):
#         s = f"{s}{j}"
#     print(s)

for i in range(2, 7):
    print(''.join(str(j) for j in range(1, i)))