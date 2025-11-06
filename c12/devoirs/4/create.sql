CREATE TABLE IF NOT EXISTS styliste (
    NumStyliste INT PRIMARY KEY,
    NomStyliste VARCHAR(50),
    AdrStyliste VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS caftan (
    NumStyliste INT PRIMARY KEY,
    designationCaftan VARCHAR(50),
    NumStyliste INT
);

CREATE TABLE IF NOT EXISTS membreJury (
    numMembreJury INT PRIMARY KEY,
    nom VARCHAR(50),
    fonction VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS NotesJury (
    NumCaftan INT,
    NumMembre INT,
    note FLOAT
);
