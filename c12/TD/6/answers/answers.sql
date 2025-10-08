-- INSERTIONS

INSERT INTO TABLE etudiant VALUES
('AB234567', 'Alami', 'Ahmad', '1986-01-01', 'Rue du port, 13', 'Tanger', 'Bac'),
('G5346789', 'Toumi', 'Aicha', '2000-12-03', 'N12 immeuble Jaouhara', 'Casablanca', 'Master'),
('C0987265', 'Toumi', 'Sanaa', '1998-04-30', 'Place du peuple n 2', 'Tanger', 'Niveau Bac'),
('D2356903', 'Idrissi Alami', 'Mohammed', '1996-05-05', 'Lotissement najah, 
rue n 12 immeuble 3', 'Rabat', 'Bac+ 4'),
('Y1234987', 'Ouled thami', 'Ali', '1979-12-04', 'La ville haute, rue 
chouhada n 6', 'Tanger', 'Bachelor'),
('J3578902', 'Ben Omar', 'Abd Allah', '1990-06-25', 'Villa Amina 
n12 bir rami', 'Kenitra', 'Phd'),
('F9827363', 'El Khattabi', 'Fatima Zohra', '1997-01-10', 'Immeuble iftikhar, 
n 13 ettakaddoum', 'Rabat', 'Bac + 2');

INSERT INTO formation VALUES 
(11, 'Programming Java', 12, 3600),
(12, 'Web Developpment', 14, 4200),
(13, 'Anglais Technique', 15, 3700),
(14, 'Communication', 10, 2500),
(15, 'Inteligence Artificielle', 20, 6000),
(16, 'Soft Skills', 12, 3000);

INSERT INTO session VALUES 
(1101, 'Session1101', '2022-01-02', '2022-01-14', 11),
(1102, 'Session1102', '2022-02-03', '2022-02-15', 11),
(1201, 'Session1201', '2022-03-04', '2022-03-18', 12),
(1202, 'Session1202', '2022-04-05', '2022-04-19', 12),
(1301, 'Session1301', '2022-01-06', '2022-01-21', 13),
(1302, 'Session1302', '2022-05-07', '2022-05-22', 13),
(1303, 'Session1303', '2022-06-08', '2022-06-23' ,13),
(1401, 'Session1401', '2022-09-01', '2022-09-11', 14),
(1402, 'Session1402', '2022-08-08', '2022-08-18', 14),
(1501, 'Session1501', '2022-11-11', '2022-12-01', 15),
(1502, 'Session1502', '2022-09-12', '2022-10-02', 15),
(1601, 'Session1601', '2022-09-13', '2022-09-25', 16),
(1602, 'Session1602', '2022-10-14', '2022-10-26', 16),
(1104, 'Session1104', '2022-10-15', '2022-10-27', 11),
(1203, 'Session1203', '2022-11-16', '2022-11-30', 12),
(1204, 'Session1204', '2022-12-17', '2022-12-31', 12);

INSERT INTO specialite VALUES 
(101, 'GL', 'Genie logiciel et developpement', 1),
(102, 'Data', 'Data Engineering', 1),
(103, 'Langues', 'Anglais Français', 1),
(104, 'Communication', 'Communication', 1),
(105, 'Securite', 'Resaux et securite', 0);

INSERT INTO catalogue VALUES 
(101, 11),
(101, 12),
(102, 15),
(101, 15),
(103, 13),
(104, 13),
(104, 14),
(104, 16);

INSERT INTO inscription VALUES 
(1101, 'AB234567', 'Distanciel'),
(1101, 'G5346789', 'Distanciel'),
(1101, 'C0987265', 'Distanciel'),
(1101, 'D2356903', 'Distanciel'),
(1101, 'Y1234987', 'Distanciel'),
(1101, 'J3578902', 'Distanciel'),
(1101, 'F9827363', 'Distanciel'),
(1201, 'AB234567', 'Présentiel'),
(1201, 'G5346789', 'Présentiel'),
(1201, 'C0987265', 'Présentiel'),
(1201, 'D2356903', 'Présentiel'),
(1201, 'Y1234987', 'Présentiel'),
(1201, 'J3578902', 'Présentiel'),
(1302, 'AB234567', 'Présentiel'),
(1302, 'G5346789', 'Distanciel'),
(1302, 'C0987265', 'Présentiel'),
(1302, 'D2356903', 'Présentiel'),
(1302, 'Y1234987', 'Présentiel'),
(1401, 'G5346789', 'Distanciel'),
(1401, 'C0987265', 'Distanciel'),
(1401, 'D2356903', 'Distanciel'),
(1401, 'Y1234987', 'Distanciel'),
(1401, 'J3578902', 'Distanciel'),
(1401, 'F9827363', 'Distanciel'),
(1501, 'AB234567', 'Distanciel'),
(1501, 'G5346789', 'Présentiel'),
(1501, 'C0987265', 'Distanciel'),
(1501, 'D2356903', 'Présentiel'),
(1501, 'Y1234987', 'Présentiel'),
(1501, 'J3578902', 'Présentiel'),
(1501, 'F9827363', 'Présentiel');


-- EXERCICE 1 P2

UPDATE etudiant SET niveauScolaire = 'Bac+5' WHERE niveauScolaire = 'Master';
UPDATE etudiant SET niveauScolaire = 'Bac+4' WHERE niveauScolaire = 'Bachelor';
UPDATE etudiant SET niveauScolaire = 'Doctorat' WHERE niveauScolaire = 'Phd';

UPDATE formation SET titreForm = 'développement Java' WHERE codeForm = 11;

ALTER TABLE inscription ADD COLUMN numInscription VARCHAR(50) DEFAULT CONCAT(codeSess, numCINEtu);

UPDATE etudiant SET dateNaissance = '1987-01-02' WHERE numCINEtu = 'AB234567';

UPDATE inscription SET typeCours = 'Présentiel' WHERE numCINEtu = 'G5346789';

-- EXERCICE 1 P3

SELECT * FROM etudiant;
SELECT * FROM formation;
SELECT * FROM inscription;
SELECT * FROM session;
SELECT * FROM catalogue;
SELECT * FROM specialite;

SELECT * FROM etudiant WHERE villeEtu = 'Tanger';

SELECT * FROM formation WHERE prixForm >= 3000;

SELECT titreForm, dureeForm, prixForm, (prixForm / dureeForm) AS prixJournalier FROM formation;

SELECT * FROM session WHERE codeSess = 11;

SELECT numCINEtu FROM inscription WHERE codeSess = 1302;

SELECT * FROM specialite WHERE active = 1;

SELECT COUNT(*) AS total_etudiants FROM etudiant;

SELECT nomEtu, prenomEtu TIMESTAMPDIFF(YEAR, dateNaissance, CURDATE()) as age FROM etudiant;

SELECT titreForm, FROM formation WHERE prixForm = (SELECT MAX(prixForm) FROM formation);

SELECT SUM(prixForm) AS prix_total FROM formation;

SELECT COUNT(DISTINCT numCINEtu) as total_etudiants FROM inscription GROUP BY codeSess;

SELECT DISTINCT numCINEtu FROM inscription;

SELECT numCINEtu, COUNT(*) as nbr_inscrip FROM inscription GROUP BY numCINEtu;

SELECT codeSess, SUM(typeCours="Présentiel") as nbr_presentiel, SUM(typeCours="Distanciel") AS nbr_distanciel FROM inscription GROUP BY codeSess;

SELECT f.titreForm, s.nomSess, s.dateDebut, s.dateFin FROM session s JOIN formation f ON s.codeForm = f.codeForm ORDER BY f.titreForm, s.dateDebut;

SELECT DISTINCT f.titreForm, e.numCINEtu, e.nomEtu, e.prenomEtu FROM session s JOIN formation f ON s.codeForm = f.codeForm JOIN inscription i ON s.codeSess = i.codeSess JOIN etudiant e ON i.numCINEtu = e.numCINEtu ORDER BY f.titreForm;

SELECT SUM(i.typeCours="Distanciel"), SUM(i.typeCours="Présentiel") FROM inscription i JOIN session s ON i.codeSess = s.codeSess JOIN formation f ON s.codeForm = f.codeForm WHERE f.titreForm = "Web Developpment";

SELECT f.codeForm, f.titreForm, SUM(i.typeCours = "Distanciel") AS nbr_distanciel FROM inscription i JOIN session s ON i.codeSess = s.codeSess JOIN formation f ON s.codeForm = f.codeForm HAVING nbr_distanciel >= 3 ORDER BY nbr_distanciel DESC;

SELECT s.nomSpec, f.dureeForm, f.prixForm FROM catalogue c JOIN formation f ON c.codeForm = f.codeForm JOIN specialite s ON c.codeSpec = s.codeSpec WHERE c.active = 1;

-- 21 22 not answered