CREATE DATABASE IF NOT EXISTS tramwayRabat;
USE tramwayRabat;

CREATE TABLE IF NOT EXISTS arrondissement (
    numArrondissement INT PRIMARY KEY,
    nomArrond VARCHAR(45) NOT NULL,
    superficie DOUBLE NOT NULL,
    nbrHabitants INT NOT NULL
);

CREATE TABLE IF NOT EXISTS station (
    numStation INT PRIMARY KEY,
    nomStation VARCHAR(45) NOT NULL,
    numArrondissement INT,
    FOREIGN KEY (numArrondissement) REFERENCES arrondissement(numArrondissement)
);

CREATE TABLE IF NOT EXISTS ligne (
    numLigne INT PRIMARY KEY,
    nbrStations INT NOT NULL,
    nbrPassagers2020 INT NOT NULL,
    DATEMService DATE NOT NULL
    stationDepart INT,
    stationArrivee INT,
    FOREIGN KEY (stationDepart) REFERENCES station(numStation),
    FOREIGN KEY (stationArrivee) REFERENCES station(numStation)
);

CREATE TABLE IF NOT EXISTS travaux (
    numArrondissement INT,
    numLigne INT,
    dateDebut DATE NOT NULL,
    duree DOUBLE NOT NULL,
    PRIMARY KEY (dateDebut),
    FOREIGN KEY (numArrondissement) REFERENCES arrondissement(numArrondissement),
    FOREIGN KEY (numLigne) REFERENCES ligne(numLigne)
);
