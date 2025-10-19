# Devoir 1 (ALI BOUYAKHSASS)

## SUJET 1

Gestion Des Examens

Ce systeme d;information correspond a la gestion des examens d'automne des etudiants S5 de la FSJES.

Un etudiant est inscrit dans un parcours (Gestion ou Eco-Gestion), l'etudiant est connu par son cne, son nom et son numero d'examen. L'etudiant a le droit de passer un examen dans tous les modules auxquels il est inscrit. Le planning des modules comporte le titre du module, la date, l'heure et la duree. Un etudiant passe ses examens dans un meme lieu (salle ou amphi) connu par son numero et sa capacite totale.

La plus part des professeurs assurent la surveillance dans la meme salle ou amphi durant toute la periode des examens On ignore dans cet exercice le group de l'etudiant et les differents sujets par module.

### MCD

```mermaid
---
id: 8102e99f-3bb0-4625-9ea8-5eee00ba8144
config:
  theme: redux-color
---
erDiagram
    ETUDIANT {
        string cne PK
        string nom
        string numeroExam
    }

    EXAM {
        int numExam PK
        string titreMod
        date dateMod
        time heureMod
        int dureeMod
    }

    LIEU {
        int numeroLieu PK
        int capaciteTotale
        string libelle
    }

    PROF {
        int idProf PK
        string nom
    }

    ETUDIANT ||--o{ PASSER : "1,n"
    EXAM ||--o{ PASSER : "1,n"
    LIEU ||--o{ contient : "1,n"
    contient ||--o{ EXAM : "1,1"
    LIEU ||--o{ affecte : "1,n"
    affecte ||--o{ PROF : "1,1"

    PASSER {
        string cne FK
        int numExam FK
    }
```

### MLD

```mermaid
---
id: 312a1c0e-5c78-486f-ab4d-f67bbeb1fb5a
config:
  theme: redux-color
---
erDiagram
    etudiants {
        string cne PK
        string nom
        string numeroExam
    }

    passer {
        string cne FK
        int numExam FK
    }

    exam {
        int numExam PK
        string titreMod
        date dateMod
        time heureMod
        int dureeMod
        int numeroLieu FK
    }

    lieu {
        int numeroLieu PK
        int capaciteTotale
        string libelle
    }

    profs {
        int idProf PK
        string nom
        int numeroLieu FK
    }

    etudiants ||--o{ passer : "passe"
    exam ||--o{ passer : "associe"
    lieu ||--o{ exam : "contient"
    lieu ||--o{ profs : "affecte"
```

### Code SQL

etudiants( cne(PK), nom, numeroExam (unique) )
passer ( cne(FK), numExam(FK))
exam ( numExam(PK) , titreMod, dateMod, heureMod, dureeMod, numeroLieu(FK))
lieu ( numeroLieu(PK), capaciteTotale, libelle )
profs ( idProf(PK), nom, numeroLieu (FK) )

```SQL
CREATE TABLE etudiants (
    CNE VARCHAR(10) PRIMARY KEY, 
    nom VARCHAR(50),
    numeroExam VARCHAR(16) UNIQUE
);
CREATE TABLE lieu (
    numeroLieu INT PRIMARY KEY,
    capaciteTotale INT,
    libelle VARCHAR(45)
);
CREATE TABLE exam (
    NumExam INT PRIMARY KEY,
    titreModule VARCHAR(45),
    dateModule DATE,
    heureModule TIME,
    dureeModule INT,
    numeroLieu INT,
    CONSTRAINT FK_EXAM_LIEU FOREIGN KEY (numeroLieu) REFERENCES lieu(numeroLieu)
);
CREATE TABLE passer (
    CNE VARCHAR(10),
    NumExam INT,
    PRIMARY KEY (CNE, NumExam),
    CONSTRAINT FK_PASSER_ETUDIANTS FOREIGN KEY (CNE) REFERENCES etudiants(CNE),
    CONSTRAINT FK_PASSER_EXAM FOREIGN KEY (NumExam) REFERENCES exam(NumExam)
);
CREATE TABLE profs (
    idProf INT PRIMARY KEY,
    nom VARCHAR(50),
    numeroLieu INT,
    CONSTRAINT FK_PROFS_LIEU FOREIGN KEY (numeroLieu) REFERENCES lieu(numeroLieu)
);
```

## Sujet 2

logement(id (PK), quartier(FK), type(FK), surface, loyer, chargesForf)
types( id(PK), libelle)
signataires(id (PK), nom, prenom, dateNaiss, telephone)
occuper(signataire (PK, FK, U), logement (PK, FK) )
quartiers(id (PK), nom, niveau, distance)

## Sujet 3

### MCD

```mermaid
erDiagram
    CLIENT {
        int IdClient PK
        string nom
        string prenom
        string adresse
        string ville
        string codePostal
        string pays
        string tel
        string email
    }

    RESERVATION {
        int NumReservation PK
        date dateDebut
        date dateFin
    }

    FACTURE {
        int IdFacture PK
    }

    LIGNE_FACTURE {
    }

    PRESTATIONS {
        int CodePrest PK
        string designation
        decimal prix
    }

    CONSOMATIONS {
        int NumConsomation PK
        datetime dateConsom
    }

    HOTELS {
        int HotelId PK
        string nom
        string adresse
        string CPH
        string Telephone
    }

    CLASSES_HOTEL {
        int IdClasse PK
        string libelle
    }

    CHAMBRES {
        int NumeroChambre PK
        string telephone
    }

    CATEGORIES_CHAMBRE {
        int IdCategorie PK
        string libelle
        string description
    }

    PRIX_CHAMBRES {
        decimal prix
    }

    %% CARDINALITIES / INTERMEDIATE TABLES
    CLIENT ||--o{ reserve : "1,n"
    reserve ||--o{ RESERVATION : "1,n"
    %% 1 client can make many reservations
    RESERVATION ||--|| CHAMBRES : "1,1" 
    %% 1 reservation occupies exactly 1 room
    RESERVATION ||--o{ FACTURE : "1,1" 
    %% 1 reservation generates 1 facture
    FACTURE ||--o{ LIGNE_FACTURE : "1,n" 
    %% 1 facture contains many lines
    PRESTATIONS ||--o{ LIGNE_FACTURE : "1,n" 
    %% 1 prestation can appear in many lines
    CONSOMATIONS ||--|| PRESTATIONS : "0,n" 
    %% 0 or many consumations per prestation

    HOTELS ||--o{ CHAMBRES : "1,n" 
    %% 1 hotel has many rooms
    CLASSES_HOTEL ||--o{ HOTELS : "1,n" 
    %% 1 class has many hotels
    CHAMBRES ||--o{ PRIX_CHAMBRES : "1,n" 
    %% 1 room can have different prices per category
    CATEGORIES_CHAMBRE ||--o{ PRIX_CHAMBRES : "1,n" 
    %% 1 category can apply to many rooms

```

### MLD

```mermaid
erDiagram
    client {
        int IdClient PK
        string nom
        string prenom
        string adresse
        string ville
        string codePostal
        string pays
        string tel
        string email
    }

    reservation {
        int NumReservation PK
        int IdClient FK
        int NumeroChambre FK
        date dateDebut
        date dateFin
    }

    facture {
        int IdFacture PK
        int NumReservation FK
    }

    ligne_facture {
        int IdFacture FK
        int CodePrest FK
    }

    prestations {
        int CodePrest PK
        string designation
        decimal prix
    }

    consomations {
        int NumConsomation PK
        datetime dateConsom
        int CodePrest FK
    }

    hotels {
        int HotelId PK
        string nom
        string adresse
        string CPH
        string Telephone
        int classeHotel FK
    }

    classes_hotel {
        int IdClasse PK
        string libelle
    }

    chambres {
        int NumeroChambre PK
        string telephone
        int HotelId FK
    }

    categories_chambre {
        int IdCategorie PK
        string libelle
        string description
    }

    prix_chambres {
        int NumeroChambre FK
        int IdCategorie FK
        decimal prix
    }

    client ||--o{ reservation : "fait"
    reservation ||--o{ facture : "genere"
    reservation ||--|| chambres : "occupe"
    prestations ||--o{ ligne_facture : "associe"
    facture ||--o{ ligne_facture : "contient"
    consomations ||--o{ prestations : "concerne"
    hotels ||--o{ chambres : "contient"
    classes_hotel ||--o{ hotels : "classe"
    chambres ||--o{ prix_chambres : "defini"
    categories_chambre ||--o{ prix_chambres : "associe"

```

## Sujet 4

### MCD

```mermaid
erDiagram
    %% ENTITIES
    AGENCE {
        int IdAgence PK
        string nom
        string rue
        string codePostal
        string ville
        string telephone
        string fax
    }

    VENDEUR {
        int IdVendeur PK
        string nom
        string prenom
        string sexe
        decimal salaireFixe
    }

    CLIENT {
        int IdClient PK
        string nom
        string prenom
        string adresse
    }

    VEHICLE {
        int IdVehicle PK
        string marque
        string modele
        string type
        string immatriculation
        date datePremiereImmat
        int kilometrage
        decimal puissanceFiscale
        string carburation
        string couleur
        decimal prixAchat
    }

    TRANSACTION {
        int IdTransaction PK
        date dateVente
        decimal prixContractualise
        string observations
    }

    PHOTO {
        int IdPhoto PK
        string url
    }

    %% INTERMEDIATE TABLES
    EMBOCHE {
        int IdAgence FK
        int IdVendeur FK
        int objectifVente
    }

    VEHICLE_EXPOSITION {
        int IdAgence FK
        int IdVehicle FK
    }

    %% LINKS / CARDINALITIES
    AGENCE ||--o{ emboche: "1,n"
    emboche ||--|| VENDEUR : "1,1"

    VENDEUR ||--o{ effectue: "1,n"
    effectue ||--|| TRANSACTION : "1,1"

    CLIENT ||--o{ passe: "1,n"
    passe ||--|| TRANSACTION : "1,1"

    VEHICLE ||--o{ concerne: "1,1"
    concerne ||--|| TRANSACTION : "1,1"

    VEHICLE ||--o{ a_photo: "1,n"
    a_photo ||--|| PHOTO : "1,1"

    AGENCE ||--o{ expose: "1,n"
    expose ||--|| VEHICLE : "1,1"
```

### MLD

```mermaid
erDiagram
    AGENCE {
        int IdAgence PK
        string nom
        string rue
        string codePostal
        string ville
        string telephone
        string fax
    }

    VENDEUR {
        int IdVendeur PK
        string nom
        string prenom
        string sexe
        decimal salaireFixe
        int IdAgence FK
    }

    VENDEUR_OBJECTIF {
        int IdVendeur FK
        int mois
        int annee
        int objectif
    }

    CLIENT {
        int IdClient PK
        string nom
        string prenom
        string adresse
    }

    VEHICLE {
        int IdVehicle PK
        string marque
        string modele
        string type
        string immatriculation
        date datePremiereImmat
        int kilometrage
        decimal puissanceFiscale
        string carburation
        string couleur
        decimal prixAchat
    }

    VEHICLE_EXPOSITION {
        int IdVehicle FK
        int IdAgence FK
        string statut
    }

    TRANSACTION {
        int IdTransaction PK
        int IdVendeur FK
        int IdClient FK
        int IdVehicle FK
        date dateVente
        decimal prixContractualise
        string observations
    }

    PHOTO {
        int IdPhoto PK
        int IdVehicle FK
        string url
    }

    %% RELATIONS
    AGENCE ||--o{ VENDEUR : "employe"
    VENDEUR ||--o{ VENDEUR_OBJECTIF : "a pour"
    AGENCE ||--o{ VEHICLE_EXPOSITION : "possede"
    VEHICLE ||--o{ VEHICLE_EXPOSITION : "expose"
    VEHICLE ||--o{ PHOTO : "a"
    VEHICLE ||--o{ TRANSACTION : "vendu"
    CLIENT ||--o{ TRANSACTION : "effectue"
    VENDEUR ||--o{ TRANSACTION : "realise"
```