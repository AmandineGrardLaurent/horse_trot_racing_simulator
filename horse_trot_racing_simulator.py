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





if __name__ == '__main__':
    print()