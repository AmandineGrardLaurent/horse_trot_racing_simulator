#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
"""
Horse Trot Racing Simulator

This program simulates a harness trotting race. Horses advance based on a die roll and
a speed update table. Players can choose between different race types (tiercé, quarté, quinté),
and the results are displayed based on the elapsed time to finish the race.
"""


# Speed update table based on {(current_speed, die roll): new speed } or disqualification ("DQ")
speed_update_table = {
    (0,1):0, (0,2):1, (0,3):1, (0,4):1, (0,5):2, (0,6):2,
    (1,1):0, (1,2):0, (1,3):1, (1,4):1, (1,5):1, (1,6):2,
    (2,1):0, (2,2):0, (2,3):1, (2,4):1, (2,5):1, (2,6):2,
    (3,1):-1, (3,2):0, (3,3):0, (3,4):1, (3,5):1, (3,6):1,
    (4,1):-1, (4,2):0, (4,3):0, (4,4):0, (4,5):1, (4,6):1,
    (5,1):-2, (5,2):-1, (5,3):0, (5,4):0, (5,5):0, (5,6):1,
    (6,1):-2, (6,2):-1, (6,3):0, (6,4):0, (6,5):0, (6,6):"DQ",
}

# Distance in meters covered per speed level
distance_by_speed = { 0:0 , 1:23, 2:46, 3:69, 4:92, 5:115, 6:138 }

# Number of winning horses required for each race type
type_values = {"tiercé" : 3 , "quarté" : 4, "quinté" : 5}

MAX_HORSES = 20
MIN_HORSES = 12
FINAL_DISTANCE = 2400
TIME_ONE_TURN = 10


def get_number_horses():
    """
    Prompt the user to enter the number of horses participating in the race.

    Ensures the number is within MIN_HORSES and MAX_HORSES.
    :return: int - The validated number of horses.
    """
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
            print("Merci de saisir un nombre positif.")
    return nb


def get_race_type():
    """
    Prompt the user to choose the race type: tiercé, quarté, or quinté.

    :return: str - The race type in lowercase.
    """
    valid_input = ""
    print(f"Jouez-vous pour un tiercé, un quarté ou un quinté ? ")
    while valid_input not in type_values:
        print("Choisissez entre tiercé, quarté et quinté")
        valid_input = input().strip().lower()
    return valid_input


def initialize_horses(nb_horses):
    """
    Initialize each horse with default attributes.

    :param nb_horses: int - The number of horses.
    :return: list - A list of horses, each represented as [horse_id, speed, distance, time].
    """
    horses_positions_list = []
    for horse_id in range(1, nb_horses + 1):
        horses_positions_list.append([horse_id, 0, 0, 0])
    return horses_positions_list


def new_speed_calculation(current_speed, horse_id):
    """
    Roll the dice for a horse and calculate its new speed.

    :param current_speed: int - The horse's current speed.
    :param horse_id: int - The horse's ID.
    :return: int or str: The new speed or "DQ" if disqualified.
    """
    random_nb = random.randint(1, 6)
    print(f"Jet du dé du cheval n°{horse_id}: {random_nb}")
    if speed_update_table[(current_speed, random_nb)] == "DQ":
        return "DQ"
    else:
        return current_speed + speed_update_table[(current_speed, random_nb)]


def run_one_turn(horses_position):
    """
    Run one turn of the race: update each horse’s speed, distance, and time.

    :param horses_position: list - The list of horses and their current state.
    :return: list - The updated list of horse states after the turn.
    """
    new_horses_position = []

    for horse in horses_position:
        horse_id = horse[0]
        speed = horse[1]
        distance = horse[2]
        time = horse[3]

        if speed == "DQ" or distance == "DQ":
            print(f"Cheval {horse_id} est disqualifié.")
            new_horses_position.append(horse)
            continue

        updated_speed = new_speed_calculation(speed, horse_id)

        if updated_speed == "DQ":
            print(f"Cheval {horse_id} est disqualifié.")
            updated_horse = [horse_id, "DQ", "DQ", time]
            new_horses_position.append(updated_horse)
            continue

        speed = updated_speed

        if distance < FINAL_DISTANCE:
            distance += distance_by_speed[speed]
            time += TIME_ONE_TURN
            print(f"Cheval {horse_id} - Vitesse actuelle: {speed} - Distance parcourue: {distance} m - Temps écoulé: {time} s")

        updated_horse = [horse_id, speed, distance, time]
        new_horses_position.append(updated_horse)
    return new_horses_position

def display_results(horses, race_type):
    """
    Display the final results of the race, sorted by time.

    :param horses: list - The list of horses after the final turn.
    :param race_type: str - The race type (tiercé, quarté, quinté).
    """
    valid_finishers = [horse for horse in horses if horse[2] != "DQ"]
    sorted_horses_by_time = sorted(valid_finishers, key=lambda x: x[3])
    print("~"*50)
    print(f"les gagnants du {race_type} sont : ")
    for i in range(0, type_values[race_type]):
        horse = sorted_horses_by_time[i]
        print(f"le cheval n°{horse[0]} avec {horse[3]} sec")
    return

def display_race(race_history):
    """
    Display the current state of the race based on the last turn.

    :param race_history: dict - The race history with each turn's state.
    """

    for horse in race_history[list(race_history.keys())[-1]]:
        horse_id = horse[0]
        distance = horse[2]
        time = horse[3]

        print(f"Cheval {horse_id:2}", end=" ")
        if distance == "DQ":
            print("est disqualifié")
        elif distance > FINAL_DISTANCE:
            print("est arrivé en", end=" ")
            print(f"{time} sec")
        else:
            print(f"|" * (distance // 23), end="")
            print(f">  {distance}m")
    return

def ask_continue():
    """
    Asks the user if they want to continue to the next turn.

    Returns: bool - True if the user wants to continue, False otherwise.
    """
    while True:
        user_input = input("Tour suivant ? (oui/non) ").strip().lower()
        if user_input in ("oui", "o"):
            return True
        elif user_input in ("non", "n"):
            return False
        else:
            print("Veuillez répondre par 'oui' ou 'non'.")


def is_finished(horse):
    """
    Check whether a horse has finished the race or has been disqualified.

    :param horse: list - The horse's current state [id, speed, distance, time].
    :return: bool - True if the horse has finished or is disqualified, False otherwise.
    """
    return horse[2] == "DQ" or horse[2] >= FINAL_DISTANCE

def start_game():
    """
    Starts and runs the harness race simulation.

    This function handles the complete flow of the race:
    - Prompts the user for the number of horses and the type of race.
    - Initializes horses with default values.
    - Simulates each turn by rolling dice and updating horse positions.
    - Continues until all horses are either disqualified or have completed the final distance.
    - Displays race progress turn by turn and shows the final results at the end.
    """

    # example race_history = { Turn 1 : [[horse 1, speed, distance, time], [horse 2, speed, distance, time]...]}
    race_history = {}
    turn_count = 1

    # get horses
    nb_horses = get_number_horses()

    # get race type
    race_type = get_race_type()

    # initialize positions
    current_positions = initialize_horses(nb_horses)

    print(f"Le {race_type} est lancé : {nb_horses} chevaux en lice !")

    # display one turn
    while True:

        print(f"Tour n°{turn_count} " + ("-" * 70))

        # update horse positions
        current_positions = run_one_turn(current_positions)

        # store updated positions in race_history
        race_history[f"Turn {turn_count}"] = current_positions

        # display current race state
        display_race(race_history)

        # check if all horses are either finished or disqualified
        latest_turn = race_history[list(race_history.keys())[-1]]
        all_horses_finished = all(is_finished(horse) for horse in latest_turn)


        if all_horses_finished:
            print("Tous les chevaux ont terminés la course.")
            break

        if not ask_continue():
            break

    # display the final result
    display_results(latest_turn, race_type)


if __name__ == '__main__':
    start_game()
