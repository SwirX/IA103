# TD3 (ALI BOUYAKHSASS)

## Execice 3

### I

#### Question 1

| Code | Designation | Type | Taille | Observation |
| ---- | ----------- | ---- | ------ | ----------- |
| dprtLn | Station depart de la ligne | Numerique | 16 | |
| arrvLn | Station d'arrive de la ligne | Numerique | 16 | |
| LongLn | Longueur de la ligne | Numerique | 8 | |
| MsServLn | Date de mise en service de la ligne | Date | | |
| psgrLn | Nombre de passagers dans la ligne | Numerique | 7 | |
| NumSt | Numero de station | Numerique | 16 | |
| NomSt | Nom de la station | Alphabetique | 30 | |
| NrArrSt | Numero d'arrondissement de station | Numerique | 16 | |
| SprfArr | Superficie d'arroundissement | Numerique | 10 | |
| NbrHbtArr | Nombre d'habitants d'arrondissement | Numerique | 10 | |
| LieuTrv | Lieu des traveaux | Alphanumerique | 16 | |
| DtDebTrv | Date de debut des traveaux | Date | | |
| DureeTrv | Duree des traveaux | Numerique | 19 | |
| ChntTrv | Chantier des traveau de station | Alphanumerique | 30 | |

---

#### Question 2

MCD

Ligne n,1 --> 1,1 station

station 1,1 --> 1,n arrondissement

station 0,n --> 1,1 travail

### II

#### MLD

| Ligne |
| -- |
| __<u>NumLigne</u>__ |
| longueur |
| DateMisSrv |
| NbrPassager |
| __NumDep#__ |
| __NumArr#__ |

---

| Station |
| -- |
| __<u>NumStation</u>__ |
| nomStation |
| __Arrondissement#__ |

---

| Arrondissement |
| -- |
| __<u>NumArrondissement</u>__ |
| NbrHabArrondissement |
| Superficie |

---

| Traveaux |
| -- |
| __NumStation#__ |
| LieuTrveaux |
| dateDeb |
| durrTraveaux |
