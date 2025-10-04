CREATE DATABASE IF NOT EXISTS centre_formation;
USE centre_formation;
CREATE TABLE IF NOT EXISTS etudiant(
    numCINEtu VARCHAR(10) PRIMARY KEY NOT NULL,
    nomEtu VARCHAR(45) NOT NULL,
    prenomEtu VARCHAR(45) NOT NULL,
    dateNaissance DATE,
    adressEtu VARCHAR(45),
    villeEtu VARCHAR(45),
    niveauEtu VARCHAR(45)
);

CREATE TABLE IF NOT EXISTS session(
    codeSess INT PRIMARY KEY NOT NULL,
    nomSess VARCHAR(45),
    dateDebut DATE,
    dateFin DATE,
    CHECK(dateDebut < dateFin)
);

CREATE TABLE IF NOT EXISTS inscription(
    codeSess INT,
    numCINEtu VARCHAR(10),
    PRIMARY KEY (codeSess, numCINEtu),
    FOREIGN KEY (codeSess) REFERENCES session(codeSess),
    FOREIGN KEY (numCINEtu) REFERENCES etudiant(numCINEtu)
);

CREATE TABLE IF NOT EXISTS formation(
    codeForm INT PRIMARY KEY NOT NULL,
    titreForm VARCHAR(45),
    dureeForm DOUBLE,
    prixForm DOUBLE,
    codeSess INT,
    FOREIGN KEY (codeSess) REFERENCES session(codeSess)
);

CREATE TABLE specialite(
    codeSpec INT PRIMARY KEY NOT NULL,
    nomSpec VARCHAR(45),
    descSpec VARCHAR(45),
    active TINYINT(1) DEFAULT 1
);

CREATE TABLE catalogue(
    codeSpec INT,
    codeForm INT,
    PRIMARY KEY (codeSpec, codeForm),
    FOREIGN KEY (codeSpec) REFERENCES specialite(codeSpec),
    FOREIGN KEY (codeForm) REFERENCES formation(codeForm)
);

