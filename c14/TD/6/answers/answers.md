# TD6 (ALI BOUYAKHSASS)

## Exercice 1

```txt
ex1
Var
T : TABLEAU[1..5] DE Entier

Debut
    Pour i de 1 a 5 faire
        Ecrire("Entrer la valeur en pos ", i, ": ")
        Lire(T[i])
    FinPour
Fin
```

## Exercice 2

```txt
ex2
Var
T : TABLEAU[1..10] DE Entier
S : Entier

Debut
    S := 0
    Pour i de 1 a 10 faire
        Ecrire("Entrer la valeur en pos ", i, ": ")
        Lire(T[i])
        S := S + T[i]
    FinPour
Fin
```

## Exercice 3

```txt
ex3

Var
T: TABLEAU[1..8] DE Entier
max: Entier

Debut
    max := 1
    Pour i de 0 a 8 faire
        Ecrire("Entrer la valeur en pos ", i, ": ")
        Lire(T[i])
        Si T[max] < T[i]
            max = i
    FinPour
    Ecrire("Valeur max est ", T[max], " dans l'index ", max)
Fin
```

## Exercice 4

```txt
ex4

Var
n : Entier
T : Tableau[1, 1000] De Reel
s : Entier

Debut
    Ecrire("Entrer la taille du tableau")
    Lire(n)
    s := 0
    Pour i de 1 a n faire
        Ecrire("Entrer la valeur en pos ", i, ": ")
        Lire(T[i])
        s := s + T[i]
    FinPour
    Ecrire("La moyenne est: ", s/n)
Fin
```

## Exercice 5

```txt
ex5

Var
M : Tableau[1..3, 1..3] DE Entier

Debut
    Pour i de 1 a 3 faire
        Pour j de 1 a 3 faire
            Ecrire("Entrer la value en pos (", j, ", ", i, "): ")
            Lire(M[i, j])
        FinPour
        Ecrire(M[i, 1], M[i, 2], M[i, 3])
    FinPour
Fin
```

## Exercice 6

```txt
ex6

Var
M : Tableau[1..2, 1..3]
s : Entier

Debut
    Pour i de 1 a 2 faire
        Pour 1 a 3 faire
            Ecrire("Entrer la value en pos (", j, ", ", i, "): ")
            Lire(M[i, j])
            s := s + M[i, j]
        FinPour
    FinPour
Fin
```

## Exercice 7

```txt
ex7

Var
M : Tableau[1..3, 1..4] De Entier
s : Entier

Debut
    Pour i de 1 a 3 faire
        s := 
        Pour j de 1 a 4 faire
            Ecrire("Entrer la value en pos (", j, ", ", i, "): ")
            Lire(M[i, j])
            s := s + M[i, j]
        FinPour
        Ecrire("La somme de la ligne ", i, " est: ", s)
    FinPour
Fin
```

## Exercice 8

```txt
ex8

Var
M : Tableau[1..3, 1..3] DE Entier

Debut
    Pour i de 1 a 3 faire
        Pour j de 1 a 3 faire
            Ecrire("Entrer la value en pos (", j, ", ", i, "): ")
            Lire(M[i, j])
        FinPour
        Ecrire(M[i, i])
    FinPour
Fin
```
