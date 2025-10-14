#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Simulateur de course de trot attelé
"""
# 12 à 20 chevaux, parcourt de 2400m

# valeur de la nouvelle vitesse en fonction de la vitesse actuelle et du jet de dé
# mise à jour de la vitesse = { (vitesse actuelle, jet de dé) : nouvelle vitesse pour ce tour }
speed_update_table = {
    (0,1):0, (0,2):1, (0,3):1, (0,4):1, (0,5):2, (0,6):2,
    (1,1):0, (1,2):0, (1,3):1, (1,4):1, (1,5):1, (1,6):2,
    (2,1):0, (2,2):0, (2,3):1, (2,4):1, (2,5):1, (2,6):2,
    (3,1):-1, (3,2):0, (3,3):0, (3,4):1, (3,5):1, (3,6):1,
    (4,1):-1, (4,2):0, (4,3):0, (4,4):0, (4,5):1, (4,6):1,
    (5,1):-2, (5,2):-1, (5,3):0, (5,4):0, (5,5):0, (5,6):1,
    (6,1):-2, (6,2):-1, (6,3):0, (6,4):0, (6,5):0, (6,6):"DQ",
}

# distance parcourue en fonction de la vitesse actuelle
distance_by_speed = { 0:0 , 1:23, 2:46, 3:69, 4:92, 5:115, 6:138 }

MAX_HORSES = 20
MIN_HORSES = 12
TYPE_VALUES = ["tiercé", "quarté", "quinté"]

def get_nb_horses():
    valid_nb = False
    nb = None
    print(f"Combien de chevaux pour cette course : ")
    while not valid_nb:
        nb_horses = input().strip()
        if nb_horses.isdigit():
            nb = int(nb_horses)
            valid_nb = (MIN_HORSES <= nb <= MAX_HORSES)
            if not valid_nb:
                print(f"Choisissez un nombre entre {MIN_HORSES} et {MAX_HORSES}")
        else:
            print("Merci de saisir un nombre.")
    return nb

def get_type_racing():
    valid_input = ""
    print(f"Jouez-vous pour un tiercé, un quarté ou un quinté ? ")
    while valid_input not in TYPE_VALUES:
        print("Choisissez entre tiercé, quarté et quinté")
        valid_input = input().strip()
    return valid_input

    return input_user

if __name__ == '__main__':
    nb_horses = get_nb_horses()
    type_racing = get_type_racing()
    print(f"Le {type_racing} est lancé : {nb_horses} chevaux en lice !")