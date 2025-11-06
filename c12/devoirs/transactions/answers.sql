-- 1
SELECT * FROM comptes;

-- 2
UPDATE comptes SET solde = solde - 100 WHERE titulaire = 'Alice';
UPDATE comptes SET solde = solde + 100 WHERE titulaire = 'Bob';
-- si la requete echoue le solde sera deduit de chez Alice mais pas ajoute chez bob

-- 3
START TRANSACTION;
UPDATE comptes SET solde = solde - 100 WHERE titulaire = 'Alice';
UPDATE comptes SET solde = solde + 100 WHERE titulaire = 'Bob';
COMMIT;

SELECT * FROM comptes;

-- 4
START TRANSACTION;
UPDATE comptes SET solde = solde - 100 WHERE titulaire = 'Alice';
UPDATE comptes SET solde = solde + 'ErreurTexte' WHERE titulaire =
'Bob';
ROLLBACK;




---------------------------------------
--------------EX d'appl.---------------
---------------------------------------

-- 1
INSERT INTO commandes (client) VALUES ('Nora');

INSERT INTO lignes_commande (commande_id, produit_id, qte) VALUES 
(1, 1, 2), 
(1, 2, 2);


-- 2
-- version 1 (not working, just trying out logic)
START TRANSACTION;
INSERT INTO commandes (client) VALUES ('Nora');
INSERT INTO lignes_commande (commande_id, produit_id, qte) VALUES
(1, 1, 2),
(1, 2, 2);
IF (SELECT stock - 2 FROM produits WHERE id = 1) < 0 OR (SELECT stock - 2 FROM produits WHERE id = 2) < 0 THEN ROLLBACK;
ELSE COMMIT; END;

-- ideas
/*
1. find a way to add mutlitple products like *args in python and iterate
1 -> new procedure to add products to a list
2. add all items to ligne_commande
2.1 -> find a way to insert multiple programatically
2.2 -> insert from select
2.3 -> check if you can join tables in update
2.4 -> join temporary table with a table
3. check stock sub if enough rollback if not
3 -> if statements
3.1 -> condition count how many products are low in stock
3.2 -> if count > 0 then one of the products is low in stock
4. idk if needed: delete the temp table
*/

-- version 2 (prolly works?)
DELIMTER $$
CREATE PROCEDURE add_product(IN product_id INT, IN quantity INT)
BEGIN
    CREATE TEMPORARY TABLE IF NOT EXISTS temp_lignes (
        produit_id INT,
        qte INT
    );

    INSERT INTO temp_lignes VALUES (product_id, quantity);
END$$
DELIMTER ;

DELIMITER $$
CREATE PROCEDURE add_command(IN nomCl VARCHAR(100))
BEGIN
    START TRANSACTION;
    INSERT INTO commandes (client) VALUES (nomCl);
    SET l_id = LAST_INSERT_ID();
    
    IF (SELECT COUNT(*) FROM temp_lignes t
            JOIN produits p ON p.id = t.produit_id
            WHERE p.stock < t.qte) > 0 THEN
        ROLLBACK;
    ELSE
        INSERT INTO ligne_produit (commande_id, produit_id, qte)
        SELECT l_id, produit_id, qte FROM temp_lignes;

        UPDATE produits SET p.stock - t.qte
        FROM produits p JOIN temp_lignes t ON p.id = t.produit_id;

        COMMIT;
END$$
DELIMITER ;


-- version 3 (just some clean up)
DELIMITER $$
CREATE PROCEDURE add_product(IN product_id INT, IN quantity INT)
BEGIN 
    CREATE TEMPORARY TABLE IF NOT EXISTS temp_lignes (
        produit_id INT,
        qte INT
    );
    INSERT INTO temp_lignes VALUES (product_id, quantity);
END$$
DELIMITER ;

DELIMITER $$
CREATE PROCEDURE add_command(IN nomCl VARCHAR(100))
BEGIN
    DECLARE pas_de_stock INT;
    DECLARE l_id INT;
    START TRANSACTION;
    INSERT INTO commandes (client) VALUES (nomCl);
    SET l_id = LAST_INSERT_ID();
    
    SELECT COUNT(*) INTO pas_de_stock
    FROM temp_lignes t
    JOIN produits p ON p.id = t.produit_id
    WHERE p.stock < t.qte;

    IF pas_de_stock > 0 THEN
        ROLLBACK;
    ELSE
        INSERT INTO lignes_produit (commande_id, produit_id, qte)
        SELECT l_id, produit_id, qte FROM temp_lignes;
        
        UPDATE produits p
        JOIN temp_lignes t ON p.id = t.produit_id
        SET p.stock = p.stock - t.qte;

        COMMIT;
        DROP TABLE IF EXISTS temp_lignes;
    END IF;
END$$
DELIMITER ; 
