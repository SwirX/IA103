import re

def ex1():
    sample = 'Hello 345 Wo8924rld 064398;fej3409'
    nums = re.findall(r'\d+', sample)
    print(nums)

def ex2():
    sample1 = "Bonjour Lorem Ipsum dolor"
    sample2 = "Lorem Ipsum dolor sit amet"
    if re.match(r'^Bonjour', sample1) == None:
        print('Sample1 ne commence pas par "Bonjour"')
    else:
        print('Sample1 commence par "Bonjour"')
    if re.match(r'^Bonjour', sample2) == None:
        print('Sample2 ne commence pas par "Bonjour"')
    else:
        print('Sample2 commence par "Bonjour"')

def ex3():
    def valide_email(email:str) -> bool:
        return False if re.match(r'\w+@\w\.\w+', email) == None else True
    print(valide_email(input('enter an email > ')))

def ex4():
    sample = 'hello Lorem Ipsum world Dolor test Sit Amet'
    matches = re.findall(r'[A-Z][a-z]+', sample)
    print(matches)

def ex5():
    i = input('Enter une date DD/MM/YYYY > ')
    if re.match(r'\d{2}\/\d{2}\/\d{4}', i) == None:
       print('La date n\'est pas au format')
    else:
        print('La date est au bon format')

if __name__ == '__main__':
    ex = [ex1, ex2, ex3, ex4, ex5]
    for i, v in enumerate(ex):
        print(f'Exercice {i+1}')
        v()
        print('\n')
        input('Enter to continue')
