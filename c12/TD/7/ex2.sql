CREATE TABLE IF NOT EXISTS styliste (
    numStyliste INT PRIMARY KEY,
    NomStyliste VARCHAR(50),
    AdrStyliste VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS caftan (
    numCaftan INT PRIMARY KEY,
    DesignationCaftan VARCHAR(50),
    NumStyliste INT,
    FOREIGN KEY (NumStyliste) REFERENCES styliste(NumStyliste)
);

CREATE TABLE IF NOT EXISTS MembreJury (
    numMembreJury INT PRIMARY KEY,
    nom VARCHAR(50),
    fonction VARCHAR(50)
);
