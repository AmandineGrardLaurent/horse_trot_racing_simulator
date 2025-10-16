# Horse Trot Racing Simulator

## Description

Ce programme simule une course de trot attelé entre plusieurs chevaux. Chaque cheval avance en fonction d'un lancer de dé et d'un tableau de mise à jour de vitesse. Le joueur peut choisir différents types de courses (tiercé, quarté, quinté), et les résultats sont affichés en fonction du temps mis par les chevaux pour terminer la course.

---

## Fonctionnement

### 1. Choix du nombre de chevaux

L'utilisateur est invité à choisir le nombre de chevaux participant à la course.  
Le nombre doit être compris entre 12 et 20.

### 2. Choix du type de course

L'utilisateur choisit ensuite le type de course parmi :

- **tiercé** (les 3 premiers gagnants)
- **quarté** (les 4 premiers gagnants)
- **quinté** (les 5 premiers gagnants)

### 3. Initialisation des chevaux

Chaque cheval commence avec :

- une vitesse initiale de 0
- une distance parcourue de 0 mètres
- un temps écoulé de 0 secondes

### 4. Déroulement de la course

La course se déroule en tours successifs :

- Pour chaque cheval, un lancer de dé (1 à 6) est effectué.
- En fonction de la vitesse actuelle et du résultat du dé, la vitesse du cheval est mise à jour selon un tableau prédéfini.
- Si un cheval est disqualifié ("DQ"), il est exclu de la course.
- Sinon, le cheval avance d'une distance proportionnelle à sa vitesse.
- Le temps de course augmente de 10 secondes à chaque tour.

La course continue jusqu'à ce que tous les chevaux soient soit arrivés au bout des 2400 mètres, soit disqualifiés, ou jusqu'à ce que l'utilisateur décide d'arrêter.

### 5. Affichage

- À chaque tour, l'état de la course est affiché :  
  - Le numéro du cheval  
  - La distance parcourue représentée graphiquement par des barres verticales `|`  
  - Le statut (disqualifié, arrivé, ou en course)

- À la fin de la course, les résultats sont affichés, classant les chevaux terminant la course par temps, avec les premiers du tiercé/quarté/quinté.

---

## Structure du programme

- **speed_update_table** : dictionnaire pour déterminer la nouvelle vitesse selon la vitesse actuelle et le lancer de dé.
- **distance_by_speed** : distance parcourue en mètres par niveau de vitesse.
- **type_values** : nombre de chevaux gagnants selon le type de course.
- Fonctions principales :
  - `get_number_horses()` : saisie du nombre de chevaux.
  - `get_race_type()` : saisie du type de course.
  - `initialize_horses()` : initialise la liste des chevaux avec leurs attributs.
  - `new_speed_calculation()` : calcule la nouvelle vitesse d'un cheval à partir d'un lancer de dé.
  - `run_one_turn()` : simule un tour complet en mettant à jour chaque cheval.
  - `display_race()` : affiche l'état de la course.
  - `display_results()` : affiche les résultats finaux.
  - `ask_continue()` : demande à l'utilisateur s'il souhaite continuer la course.
  - `is_finished()` : vérifie si un cheval a terminé la course ou est disqualifié.
  - `start_game()` : orchestre le déroulement complet de la simulation.

---

## Dictionnaires utilisés dans le programme

### 1. Tableau de mise à jour de la vitesse (`speed_update_table`)

Ce dictionnaire détermine la nouvelle vitesse d'un cheval en fonction de sa vitesse actuelle et du résultat du lancer de dé. La clé est un tuple `(vitesse_actuelle, résultat_du_dé)` et la valeur est la modification de vitesse (un entier), ou `"DQ"` si le cheval est disqualifié.

```python
speed_update_table = {
    (0,1):0, (0,2):1, (0,3):1, (0,4):1, (0,5):2, (0,6):2,
    (1,1):0, (1,2):0, (1,3):1, (1,4):1, (1,5):1, (1,6):2,
    (2,1):0, (2,2):0, (2,3):1, (2,4):1, (2,5):1, (2,6):2,
    (3,1):-1, (3,2):0, (3,3):0, (3,4):1, (3,5):1, (3,6):1,
    (4,1):-1, (4,2):0, (4,3):0, (4,4):0, (4,5):1, (4,6):1,
    (5,1):-2, (5,2):-1, (5,3):0, (5,4):0, (5,5):0, (5,6):1,
    (6,1):-2, (6,2):-1, (6,3):0, (6,4):0, (6,5):0, (6,6):"DQ",
}
```


### 2. Distance parcourue par niveau de vitesse(`distance_by_speed`)

Ce dictionnaire associe à chaque niveau de vitesse la distance en mètres parcourue durant un tour.

```
distance_by_speed = {
    0: 0,
    1: 23,
    2: 46,
    3: 69,
    4: 92,
    5: 115,
    6: 138,
}
```

---

## Comment utiliser

1. Lancer le script Python.
2. Suivre les instructions à l'écran pour :
   - Choisir le nombre de chevaux.
   - Choisir le type de course.
3. Valider à chaque tour si vous souhaitez continuer.
4. Consulter le classement final à la fin de la course.

---

## Exemple d'exécution

```plaintext
Combien de chevaux pour cette course : 
12
Jouez-vous pour un tiercé, un quarté ou un quinté ? 
tiercé
Le tiercé est lancé : 12 chevaux en lice !
Tour n°1 ----------------------------------------------------------------------
Jet du dé du cheval n°1: 4
Cheval  1 - Vitesse actuelle: 1 - Distance parcourue: 23 m - Temps écoulé: 10 s
...
Cheval  1 | > 23m
...
Tour suivant ? (oui/non)
```
---

## Exemple d’affichage final à la fin d’une course

Lorsque tous les chevaux ont terminé la course (ou sont disqualifiés), le programme affiche les résultats finaux, classés par ordre de temps mis pour parcourir les 2400 mètres. Voici un exemple typique d’affichage final dans le terminal :

```plaintext
Tous les chevaux ont terminés la course.
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
les gagnants du tiercé sont : 
le cheval n°5 avec 220 sec
le cheval n°3 avec 225 sec
le cheval n°1 avec 230 sec
```

Dans cet exemple, le cheval n°5 est arrivé premier avec un temps de 220 secondes, suivi des chevaux n°3 et n°1, qui complètent le tiercé.