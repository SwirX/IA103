# TD 4 (ALI BOUYAKHSASS)

## Exercice 1

```txt
ITER10

Var
i : Entier

Debut
    Pour i de 0 a 10 faire
        Ecrire(i)
    FinPour
Fin
```

## Exercice 2

```txt
TBL_MULT

Var
n, i : Entier

Debut
    Ecrire("Entrer un nombre: ")
    Lire(n)
    Pour i de 1 a 10 faire
        Ecrire(n, "*", i, "=", n*i)
    FinPour
Fin
```

## Exercice 3

```txt
SOMME_N

Var
n, i, s : Entier

Debut
    Ecrire("Entrer un nombre: ")
    Lire(n)
    Pour i de 1 a n faire
        s := s + i
    FinPour
    Ecrire("Somme: ", s)
Fin
```

<br>

## Exercice 4

(Explication ambigue)

```txt
SOMME

Var
n, s : Entier

Debut
    s := 0 // initialisation
    Tant que n != 0 faire
        Ecrire("Entrer un nombre (0 pour arreter): ")
        Lire(n)
        s := s + n
    FinTantque
    Ecrire(s)
Fin
```

<br>

## Exercice 5

```txt
MDP

Const
c = "1234" : Chaine de char

Var
e : Chaine de char

Debut
    Tant que e != c faire
        Ecrire("Enter le mot de passe")
        Lire(e)
    FinTantque
Fin
```

<br><br><br><br><br><br>

## Exercice 6

```txt
NUMCOUNT

Var
e, c : Entier

Debut
    Tant que e >= 0 faire
        Ecrire("Entrer un nombre (<0 pour l'arreter): ")
        Lire(e)
        c := c + 1
    FinTantque
    Ecrire(c, " valeurs positives on ete entrees")
Fin
```

<br>

## Exercice 7

```txt
TRIES_COUNTER

Const
s = 25 : Entier

Var
e, c : Entier

Debut
    c := -1
    Repeter
        c := c + 1
        Ecrire("Enter le nombre secret: ")
        Lire(e)
    Jusqu'a e == s
    Ecrire(c, " Essais effectues")
Fin
```

<br><br><br><br><br><br><br><br><br><br><br>

## Exercice 8

```txt
INTERVALE

Var
e : Entier

Debut
    Repeter
        Ecrire("Entrer un nombre (1-10): ")
        Lire(e)
    Jusqu'a e <= 10 et e > 0
    Ecrire("Merci, votre nombre est valide")
Fin
```
