def ex2():
    l = []
    for i in range(100):
        l.append(i*2)
    print(l)
    print(f'moyenne: {sum(l)/len(l)}')
    print(f'min: {l[0]}')
    l.reverse()
    print(l)

def ex3():
    n = {
            "Ali": 20,
            "Othmane": 17,
            "Nahid": 19,
            "Rania": 18,
            "Douae": 19,
        }
    print('-'*10)
    for i, v in n.items():
        print(f'{i}: {v}')
    print('-'*10)

    m = sum([i for i in n.values()])/len(n.values())
    print(f'Moyenne: {m}')
    b = ('', 0)
    for i, v in n.items():
        if b[1] < v:
            b = (i, v)
    print(b)
    n['Rayane'] = 15 
    print('-'*10)
    for i, v in n.items():
        print(f'{i}: {v}')
    print('-'*10)


if __name__ == '__main__':
    ex = [ex2, ex3]
    for i, fn in enumerate(ex):
        print(f'Exercise {i+1}')
        fn()
        print('\n')
