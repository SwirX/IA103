# TD 2 (ALI BOUYAKHSASS)

## Exercice 1

### Question 1

moderniser SI d'un hopital et gerer les patients, personnel et les ressources et de modeliser ses donnees

### Question 2

- Chaque membre du personnel est affecte a un seul service
- Chaque patient est hospitalise qu'en un seul service
- Chaque patient recois un niveau de gravite lors de son passage aux urgences
- Un medecin peut etre chef de plusieurs services
- Un patient peut avoir plusieurs sejours au cours du temps
- Un soin ne peut etre associe qu'a un seul sejour
- Plusieurs soins (differents) peuvent etre recu par un patient

### Question 3

- Service Medical
- Personnel
- Patient
- Sejour
- Urgences
- Soins

### Question 4

- Une colonne qui definit le role du personnel (medecin, infirmier)

### Question 5

- Par la date de debut et le numero unique du patient

### Question 6

- Non il est soit administre aux urgences ou hospitalise dans un service

### Question 7

- Soins et Personnel

### Question 8

- Oui car la meme procedure des soins a recevoir est dans les deux.

### Question 9

- Non, car un medecin peut etre attribue a plusieurs services

### Question 10

#### Service Medical

```txt
Table ServMed
id
nom
dirigeur
```

#### Personnel

```txt
Table Personnel
matricule
nom
prenom
tel
emboche
```

#### Patient

```txt
Table Patients
id
nom
prenom
dt_naissance
adresse
```

#### Sejour

```txt
Table Sejour
id
dt_debut
dt_fin
patient
```

#### Urgences

```txt
Table Urgences
id
dt_arrive
dt_prise
gravite
sejour
```

#### Soin

```txt
Table Soin
id
libelle
date
sejour
personnel
```
