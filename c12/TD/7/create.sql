CREATE TABLE client (
    numCl INT PRIMARY KEY,
    nomCl VARCHAR(50),
    prCl VARCHAR(50),
    telephone VARCHAR(10)
);

CREATE TABLE commande (
    numBon INT PRIMARY KEY,
    dateCmd DATE,
    numCl INT,
    FOREIGN KEY (numCl) REFERENCES client(numCl)
);

CREATE TABLE produit (
    reference INT PRIMARY KEY,
    intitule VARCHAR(50),
    pu INT,
    quantiteStock INT
);

CREATE TABLE ligneCommande (
    numBon INT,
    reference INT,
    quantiteCommandee INT,
    PRIMARY KEY (numBon, reference),
    FOREIGN KEY (numBon) REFERENCES commande(numBon),
    FOREIGN KEY (reference) REFERENCES produit(reference)
);


-- 1
DELIMITER $$
CREATE PROCEDURE sp_ValeursProduits() BEGIN SELECT reference, intitule, (quantiteStock * pu) AS valeurStock FROM produit; END$$
DELIMITER ;

-- 2
DELIMITER $$ 
CREATE PROCEDURE sp_listeProduitsCommandes(IN nCom INT) BEGIN SELECT * FROM ligneCommande WHERE numBon = nCom; END$$
DELIMITER ;

-- 3
DELIMITER $$
CREATE PROCEDURE sp_nbCommandes(OUT nbCom INT) BEGIN SELECT COUNT(*) INTO nbCom FROM commande; END$$
DELIMITER ;

-- 4
DELIMITER $$
CREATE PROCEDURE gainActualise(IN gMen INT, INOUT chAff FLOAT) BEGIN SELECT COALESCE(chAff, 0) + gMen INTO chAff; END$$
DELIMITER ;

-- 5
DROP PROCEDURE gainActualise;

-- 6
-- delete and redo

-- 7
DELIMITER $$
CREATE PROCEDURE Disponibilite(IN ref INT, OUT dispo VARCHAR(30)) BEGIN SELECT CASE WHEN quantiteStock > 10 THEN 'Produit Disponible' ELSE 'Besoin en reapprovisionnement' END INTO dispo FROM produit WHERE reference = ref; END $$
DELIMITER ;

-- proc cannot be used in requests, func always returns ONE value and used for calculating
-- fn cannot run queries
