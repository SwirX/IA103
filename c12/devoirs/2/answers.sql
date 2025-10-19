-- 1  Recuperer toutes les colonnes de la table Sales
SELECT * FROM Sales;
-- 2 Recuperer product name et unit price de la table Products
SELECT product_name, unit_price FROM Products;
-- 3 Recuperer sale id et sale date de la table Sales.
SELECT sale_id, sale_date FROM Sales;
-- 4 Filtrer la table Sales pour afficher uniquement les ventes dont total price est 
-- superieur a 100$
SELECT * FROM Sales WHERE total_price > 100;
-- 5 Filtrer la table Products pour afficher uniquement les produits appartenant 
-- a la categorie Electronics.
SELECT * FROM Products WHERE category = "Electronics";
-- 6  Recuperer sale id et total price des ventes effectuees le 3 janvier 2024.
SELECT sale_id, total_price FROM Sales WHERE sale_date = '2024-01-03';
-- 7 Recuperer product id et product name des produits dont le unit price est 
--superieur a 100 $.
SELECT product_id, product_name FROM Products WHERE unit_price > 100;
-- 8 Calculer le chiffre d’affaires total genere par toutes les ventes.
SELECT SUM(total_price) AS chiffre_affaire FROM Sales;
-- 9 Calculer le prix unitaire moyen des produits
SELECT AVG(unit_price) AS prix_moyen_produits FROM Products;
-- 10 Calculer la quantite totale vendue dans la table Sales
SELECT SUM(quantity_sold) AS quantite_totale FROM Sales;
-- 11 Compter le nombre de ventes par jour
SELECT COUNT(*)/DATEDIFF(MAX(sale_date), MIN(sale_date)) AS ventes_p_jour FROM Sales;
-- 12 Recuperer le product name et le unit price du produit ayant le prix unitaire 
-- le plus eleve.
SELECT product_name, MAX(unit_price) FROM Products;
-- 13 Recuperer les ventes dont la quantite vendue (quantity sold) est superieure a 4
SELECT * FROM Sales WHERE quantity_sold > 4;
-- 14 Recuperer product name et unit price des produits, tries par prix decroissant
SELECT product_name, unit_price FROM Products ORDER BY unit_price;
-- 15 Calculer le total des ventes en arrondissant les valeurs `a deux decimales.
SELECT ROUND(SUM(total_price), 2) AS ventes_totales FROM Sales;
-- 16 Calculer le prix moyen des ventes dans la table Sales
SELECT SUM(total_price) AS prix_moyen FROM Sales;
-- 17 Recuperer sale id et sale date de la table Sales, en formatant la date 
-- au format AAAA-MM-JJ
SELECT sale_id, sale_date FROM Sales;
-- 18 Calculer le chiffre d’affaires total genere par les produits appartenant 
-- `a la categorie Electronics
SELECT SUM(total_price) AS prix_total FROM Sales WHERE product_id in (SELECT product_id FROM Products WHERE category = "Electronics");
-- 19 Recuperer product name et unit price des produits dont le prix est 
-- compris entre 20$ et 600$
SELECT product_name, unit_price FROM Products WHERE unit_price > 20 AND unit_price < 600;
-- 20 Recuperer product name et category de la table Products, tries par 
--categorie en ordre croissant
SELECT product_name, category FROM Products ORDER BY category;

---------------------------------------------------------------------
---------------------------------------------------------------------
---------------------------------------------------------------------

-- 1 Calculer la quantit´e totale vendue de produits appartenant `a la 
-- cat´egorie Electronics
SELECT SUM(total_price) FROM Sales WHERE product_id in (SELECT product_id FROM Products WHERE category = "Electronics");
-- 2 R´ecup´erer le nom du produit et le prix total, en calculant ce dernier 
-- comme le produit de quantity sold par unit price
SELECT product_name, quantity_sold * unit_price as prix_total FROM Products JOIN Sales ON Sales.product_id = Products.product_id;
-- 3 Identifier le produit le plus fr´equemment vendu dans la table Sales.
SELECT product_name, MAX(quantity_sold) FROM Sales JOIN Products ON Products.product_id = Sales.product_id;
-- 4 Trouver les produits qui n’ont pas ´et´e vendus dans la table Products
SELECT product_name FROM Products WHERE product_id NOT IN (SELECT product_id FROM Sales);
-- 5 Calculer le chiffre d’affaires total g´en´er´e par les ventes pour 
-- chaque cat´egorie de produits. 
SELECT category, SUM(total_price) FROM Sales JOIN Products ON Products.product_id = Sales.product_id GROUP BY category;
-- 6 Trouver la cat´egorie de produits ayant le prix unitaire moyen le plus ´elev´e.
SELECT category, MAX(avg_price) FROM (SELECT category, AVG(unit_price) AS avg_price FROM Sales s JOIN Products p ON s.product_id = p.product_id GROUP BY category) as max_moyenne;
-- 7 Identifier les produits dont le total des ventes d´epasse 30 $.
SELECT product_name FROM Products WHERE product_id in (SELECT product_id FROM Sales WHERE total_price > 30);
-- 8 Compter le nombre de ventes effectu´ees chaque mois
SELECT COUNT(*)/TIMESTAMPDIFF(month, MAX(sale_date), MIN(sale_date)) AS monthly_sales FROM Sales;
-- 9 R´ecup´erer les d´etails des ventes pour les produits dont le nom contient le mot “Smart”.
SELECT * FROM Sales WHERE product_id IN (SELECT product_id FROM Products WHERE product_name LIKE '%Smart%');
-- 10 D´eterminer la quantit´e moyenne vendue pour les produits dont le prix 
-- unitaire est sup´erieur `a 100 $.
SELECT AVG(s.quantity_sold) AS sold_avg FROM Sales s JOIN Products p ON p.product_id = s.product_id WHERE p.unit_price > 100;
-- 11 R´ecup´erer le nom du produit et le chiffre d’affaires total pour chaque produit.
SELECT product_name, SUM(total_price) AS  FROM Sales s JOIN Products p ON p.product_id = s.product_id GROUP BY product_name;
-- 12 Lister toutes les ventes avec les noms de produits correspondants.
SELECT p.product_name, s.quantity_sold, s.total_price FROM Sales s JOIN Products p ON p.product_id = s.product_id;
-- 13
SELECT category, (total_price/(SELECT SUM(total_price) FROM Sales)*100) as percentage FROM Sales s JOIN Products p ON s.product_id = p.product_id GROUP BY category ORDER BY percentage DESC LIMIT 3;
-- 14 
SELECT 

