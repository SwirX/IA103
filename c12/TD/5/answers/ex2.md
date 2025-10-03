# EXERCICE 2

```sql
CREATE DATABASE centre_formation;
USE centre_formation;

CREATE TABLE IF NOT EXISTS etudiant (
    numCINEtu VARCHAR(10) PRIMARY KEY NOT NULL,
    nomEtu VARCHAR(45) NOT NULL,
    prenomEtu VARCHAR(45) NOT NULL,
    dateNaissance DATE NOT NULL,
    adresseEtu VARCHAR(100) NOT NULL,
    villeEtu VARCHAR(45) NOT NULL,
    niveauScolaire VARCHAR(45) NOT NULL,
);

CREATE TABLE IF NOT EXISTS session (
    codeSess INT PRIMARY KEY NOT NULL,
    nomSess VARCHAR(45) NOT NULL,
    dateDebut DATE NOT NULL,
    dateFin DATE NOT NULL,
    CHECK (dateFin > dateDebut)
);

CREATE TABLE IF NOT EXISTS formation (
    codeForm INT PRIMARY KEY NOT NULL,
    titreForm VARCHAR(45) NOT NULL,
    dureeForm DOUBLE NOT NULL,
    prixForm DOUBLE NOT NULL
    codeSess INT,
    FOREIGN KEY (codeSess) REFERENCES session(codeSess)
);

CREATE TABLE IF NOT EXISTS inscription (
    numCINEtu VARCHAR(10),
    codeSess INT,
    typeCours VARCHAR(45) NOT NULL,
    PRIMARY KEY (numCINEtu, codeForm),
    FOREIGN KEY (numCINEtu) REFERENCES etudiant(numCINEtu),
    FOREIGN KEY (codeSess) REFERENCES session(codeSess)
);

CREATE TABLE IF NOT EXISTS specialite (
    codeSpec INT PRIMARY KEY NOT NULL,
    nomSpec VARCHAR(45) NOT NULL,
    descSpec VARCHAR(45) NOT NULL,
    active ENUM(1, 0) NOT NULL DEFAULT 1,
)

CREATE TABLE IF NOT EXISTS catalogue (
    codeSpec INT,
    codeForm INT,
    PRIMARY KEY (codeSpec, codeForm),
    FOREIGN KEY (codeSpec) REFERENCES specialite(codeSpec),
    FOREIGN KEY (codeForm) REFERENCES formation(codeForm),
);
```
