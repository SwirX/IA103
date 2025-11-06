-- 1 Affcher tous les réalisateurs (tous les champs).
SELECT * 
FROM LPECOM_REALISATEURS;

-- 2 Affcher uniquement les noms et prénoms des réalisateurs.
SELECT nom, prenom 
FROM LPECOM_REALISATEURS;

-- 3 Affcher le nom et la date de réalisation de tous les films.
SELECT nom, date_realisation 
FROM LPECOM_FILMS;

-- 4Afficher les titres des films réalisés par le réalisateur d'identifiant 16.
SELECT nom 
FROM LPECOM_FILMS 
WHERE id_realisateur = 16;

-- 5 Affcher la liste des nationalités présentes dans la table des réalisateurs sans doublon.
SELECT 
DISTINCT nation 
FROM LPECOM_REALISATEURS;

-- 6 Affcher tous les réalisateurs britanniques (nation = 'uk').
SELECT * 
FROM LPECOM_REALISATEURS 
WHERE nation = 'uk';

-- 7 Affcher les films réalisés après l'an 2010.
SELECT * 
FROM LPECOM_FILMS 
WHERE date_realisation > '2010-12-31';

-- 8 Affcher les réalisatrices (femmes, sexe = 1).
SELECT * 
FROM LPECOM_REALISATEURS 
WHERE sexe = 1;

-- 9 Affcher les films dont le titre contient le mot 'Black'.
SELECT * 
FROM LPECOM_FILMS WHERE nom LIKE '%Black%';

-- 10 Affcher les notes supérieures ou égales à 4 dans la table LPECOM_FILMS_NOTES.
SELECT * 
FROM LPECOM_FILMS_NOTES 
WHERE note >= 4;

-- 11 Donner la note moyenne de tous les films confondus.
SELECT AVG(note) AS note_moyenne 
FROM LPECOM_FILMS_NOTES;

-- 12 Donner la moyenne des notes pour le film 'Black Swan'.
SELECT AVG(note) AS note_moyenne_black_swan 
FROM LPECOM_FILMS_NOTES WHERE id_film = (SELECT id FROM LPECOM_FILMS WHERE nom = 'Black Swan');

-- 13 Donner le nombre de films réalisés par chaque réalisateur.
SELECT id_realisateur, COUNT(*) AS nombre_de_films 
FROM LPECOM_FILMS GROUP BY id_realisateur;

-- 14 Donner la note la plus élevée enregistrée dans la base.
SELECT MAX(note) AS note_maximale 
FROM LPECOM_FILMS_NOTES;

-- 15 Donner la date de naissance la plus ancienne parmi les réalisateurs.
SELECT MIN(date_naissance) AS date_naissance_plus_ancienne 
FROM LPECOM_REALISATEURS;

-- 16 Affcher tous les films triés par date de réalisation décroissante.
SELECT * 
FROM LPECOM_FILMS 
ORDER BY date_realisation DESC;

-- 17 Affcher les réalisateurs triés par nom alphabétique.
SELECT * 
FROM LPECOM_REALISATEURS 
ORDER BY nom ASC;

-- 18 Affcher les films avec leur moyenne de notes, triés du meilleur au moins bon.
SELECT f.id, f.nom, AVG(n.note) AS moyenne_notes
FROM LPECOM_FILMS f
JOIN LPECOM_FILMS_NOTES n ON f.id = n.id_film
GROUP BY f.id, f.nom
ORDER BY moyenne_notes DESC;

-- 19 Affcher les films réalisés par le réalisateur le plus âgé.
SELECT f.*
FROM LPECOM_FILMS f
JOIN LPECOM_REALISATEURS r ON f.id_realisateur = r.id
WHERE r.date_naissance = (SELECT MIN(date_naissance) FROM LPECOM_REALISATEURS);

-- 20 Affcher le nom du réalisateur du film le mieux noté.
SELECT r.nom, r.prenom
FROM LPECOM_REALISATEURS r
JOIN LPECOM_FILMS f ON r.id = f.id_realisateur
JOIN LPECOM_FILMS_NOTES n ON f.id = n.id_film
WHERE n.note = (SELECT MAX(note) FROM LPECOM_FILMS_NOTES);

-- 21 Affcher les réalisateurs et le nombre total de notes reçues pour leurs films.
SELECT r.id, r.nom, r.prenom, COUNT(n.note) AS nombre_de_notes
FROM LPECOM_REALISATEURS r
JOIN LPECOM_FILMS f ON r.id = f.id_realisateur
JOIN LPECOM_FILMS_NOTES n ON f.id = n.id_film
GROUP BY r.id, r.nom, r.prenom;

-- 22 Affcher les réalisateurs ayant réalisé au moins un film avec une moyenne supérieure a 4
SELECT DISTINCT r.id, r.nom, r.prenom
FROM LPECOM_REALISATEURS r
JOIN LPECOM_FILMS f ON r.id = f.id_realisateur
JOIN LPECOM_FILMS_NOTES n ON f.id = n.id_film
GROUP BY r.id, r.nom, r.prenom
HAVING AVG(n.note) > 4;

-- 23 Affcher la moyenne des notes pour chaque réalisateur classée par ordre décroissant.
SELECT r.id, r.nom, r.prenom, AVG(n.note) AS moyenne_notes
FROM LPECOM_REALISATEURS r
JOIN LPECOM_FILMS f ON r.id = f.id_realisateur
JOIN LPECOM_FILMS_NOTES n ON f.id = n.id_film
GROUP BY r.id, r.nom, r.prenom
ORDER BY moyenne_notes DESC;

-- 24 Affcher les réalisateurs n'ayant aucun film noté
SELECT r.id, r.nom, r.prenom
FROM LPECOM_REALISATEURS r
WHERE r.id NOT IN (SELECT DISTINCT f.id_realisateur
                   FROM LPECOM_FILMS f
                   JOIN LPECOM_FILMS_NOTES n ON f.id = n.id_film);

-- 25 Affcher pour chaque film, le nombre de notes reçues et la moyenne correspondante.
SELECT f.id, f.nom, COUNT(n.note) AS nombre_de_notes, AVG(n.note) AS moyenne_notes
FROM LPECOM_FILMS f
JOIN LPECOM_FILMS_NOTES n ON f.id = n.id_film
GROUP BY f.id, f.nom;

-- 26 Affcher le réalisateur dont le film a reçu la plus grande variation de notes (écart entre MAX et MIN).
SELECT r.id, r.nom, r.prenom, (MAX(n.note) - MIN(n.note)) AS variation_notes
FROM LPECOM_REALISATEURS r
JOIN LPECOM_FILMS f ON r.id = f.id_realisateur
JOIN LPECOM_FILMS_NOTES n ON f.id = n.id_film
GROUP BY r.id, r.nom, r.prenom
ORDER BY variation_notes DESC
LIMIT 1;

-- 27 Affcher les réalisateurs ayant plusieurs films dont la moyenne dépasse 3.5.
SELECT r.id, r.nom, r.prenom, COUNT(f.id) AS nombre_de_films
FROM LPECOM_REALISATEURS r
JOIN LPECOM_FILMS f ON r.id = f.id_realisateur
JOIN LPECOM_FILMS_NOTES n ON f.id = n.id_film
GROUP BY r.id, r.nom, r.prenom
HAVING AVG(n.note) > 3.5 AND COUNT(f.id) > 1;

-- 28 Affcher les films réalisés par des réalisateurs américains (us) avant 2015.
SELECT f.id, f.nom, f.date_realisation
FROM LPECOM_FILMS f
JOIN LPECOM_REALISATEURS r ON f.id_realisateur = r.id
WHERE r.nation = 'us' AND f.date_realisation < '2015-01-01';

-- 29 Affcher les réalisateurs et leurs films, même si certains films ne sont pas notés (utiliser LEFT JOIN).
SELECT r.id, r.nom, r.prenom
       f.id AS idFilm, f.nom AS Film, n.note
FROM LPECOM_REALISATEURS r
LEFT JOIN LPECOM_FILMS f ON r.id = f.id_realisateur
LEFT JOIN LPECOM_FILMS_NOTES n ON f.id = n.id_film;

-- 30 Créer un utilisateur nommé etudiant1 avec le mot de passe sql2025
CREATE USER etudiant1@localhost IDENTIFIED BY 'sql2025';

-- 31 Donner à etudiant1 le privilège de sélectionner toutes les données de la table LPECOM_FILMS.
GRANT SELECT ON LPECOM_FILMS.* TO etudiant1@localhost;

-- 32 Créer un utilisateur gestionnaire ayant tous les privilèges sur la base LPECOM
CREATE USER gestionnaire@localhost IDENTIFIED BY 'gst2025';
GRANT ALL PRIVILEGES ON LPECOM.* TO gestionnaire@localhost;

-- 33 Retirer à etudiant1 le droit de mise à jour (UPDATE) sur la table LPECOM_FILMS_NOTES
REVOKE UPDATE ON LPECOM_FILMS_NOTES FROM etudiant1@localhost;

-- 34 Supprimer complètement l'utilisateur gestionnaire de la base.
DROP USER gestionnaire@localhost;