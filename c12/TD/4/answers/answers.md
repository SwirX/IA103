# Exercice 4

## Sturcture

### BDD a partir du CDC (~~pos~~)

Acteur(nomActeur (PK), prnmActeur (PK), dtNaissActeur, poidsActeur, tailleActeur)

Film(Titre (PK), Annee (PK), realisaeur, scenariste)

Producteur(NomProd (PK), adresse)

Investir(NomProd (PK, FK), Titre (PK, FK), Annee (PK, FK) )

### BDD instinctive

Acteur( ActeurId (PK), nomActeur, prnmActeur, dtNaissActeur, poidsActeur, tailleActeur )

Film( FilmId (PK), Annee, RealId (FK), ScenId (FK) )

Realisateur(RealId (PK), nom)

Scenariste( ScenId, (PK), nom)

Jouer( ActeurId (PK, FK), FilmId (PK, FK))

HistoriqueCachet( Acteur (PK, FK), FilmID (PK, FK), date (PK), pourcentage, cachetFixe)

LiensFilm( FilmId (PK, FK), RemakeId (PK, FK), typeLien)

Producteur( ProdId (PK), nomProd, adresseProd )

Investir( ProdId (PK, FK), FilmId (PK, FK), montant)

(Pas de table plusieur a plusieurs pour "Realisateur" et "Scenariste" car le CDC n'a mentione existance d'un seul)

ce design de BDD est 5FN:

- attributs atomiques (1FN)
- pas de dépendances partielles (2FN)
- pas de dépendances transitives (3FN)
- pas de dépendances multivaluées (4FN)
- toutes tes relations N-N sont déjà en tables séparées (5FN)

### Diagrame MLD

```mermaid
erDiagram
 Acteur {
 int ActeurId PK
 string nomActeur
 string prnmActeur
 date dtNaissActeur
 float poidsActeur
 float tailleActeur
 }
 Film {
 int FilmId PK
 int Annee
 int RealId FK
 int ScenId FK
 }
 Realisateur {
 int RealId PK
 string nom
 }
 Scenariste {
 int ScenId PK
 string nom
 }
 Producteur {
 int ProdId PK
 string nomProd
 string adresseProd
 }
 Jouer {
 int ActeurId PK, FK
 int FilmId PK, FK
 }
 HistoriqueProfit {
 int ActeurId PK, FK
 int FilmId PK, FK
 date date PK
 float pourcentage
 float cachetFixe
 }
 LiensFilm {
 int FilmId PK, FK
 int RemakeId PK, FK
 string typeLien
 }
 Investir {
 int ProdId PK, FK
 int FilmId PK, FK
 float montant
 }

 Acteur ||--o{ Jouer : "joue"
 Film ||--o{ Jouer : "joué par"
 Acteur ||--o{ HistoriqueProfit : "a reçu"
 Film ||--o{ HistoriqueProfit : "pour"
 Film ||--o{ LiensFilm : "a un lien vers"
 Film ||--o{ Investir : "financé par"
 Producteur ||--o{ Investir : "investit"
 Film ||--|| Realisateur : "réalisé par"
 Film ||--|| Scenariste : "écrit par"
```
