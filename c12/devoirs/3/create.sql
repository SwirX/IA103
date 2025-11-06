CREATE TABLE IF NOT EXISTS LPECOM_REALISATEURS (
    id INT PRIMARY KEY,
    nom VARCHAR(50),
    prenom VARCHAR(50),
    sexe INT,
    nation VARCHAR(2),
    date_naissance DATE
);

CREATE TABLE IF NOT EXISTS LPECOM_FILMS(
    id INT PRIMARY KEY,
    nom VARCHAR(50),
    id_realisateur INT,
    date_realisation DATE,
    FOREIGN KEY (id_realisateur) REFERENCES LPECOM_REALISATEURS(id)
);

CREATE TABLE IF NOT EXISTS LPECOM_FILMS_NOTES(
    id INT,
    id_film INT,
    note FLOAT,
    PRIMARY KEY (id, id_film),
    FOREIGN KEY (id_film) REFERENCES LPECOM_FILMS(id)
);
