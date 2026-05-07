import random

games = [
    {
        "name": "Dilemma del Prigioniero Standard",
        "rounds": [{(True, True): (3, 3), (True, False): (0, 5), (False, True): (5, 0), (False, False): (1, 1)}] * 10
    },
    {
        "name": "Sprint Breve",
        "rounds": [{(True, True): (2, 2), (True, False): (0, 3), (False, True): (3, 0), (False, False): (1, 1)}] * 3
    },
    {
        "name": "Stag Hunt (Caccia al Cervo)",
        "rounds": [{(True, True): (5, 5), (True, False): (0, 4), (False, True): (4, 0), (False, False): (2, 2)}] * 8
    },
    {
        "name": "Gioco del Pollo (Chicken)",
        "rounds": [{(True, True): (0, 0), (True, False): (-1, 1), (False, True): (1, -1), (False, False): (-10, -10)}] * 5
    },
    {
        "name": "Dilemma Generoso",
        "rounds": [{(True, True): (10, 10), (True, False): (0, 12), (False, True): (12, 0), (False, False): (2, 2)}] * 6
    },
    {
        "name": "Maratona di Resistenza",
        "rounds": [{(True, True): (3, 3), (True, False): (0, 5), (False, True): (5, 0), (False, False): (1, 1)}] * 20
    },
    {
        "name": "Battaglia a Somma Zero",
        "rounds": [{(True, True): (0, 0), (True, False): (-1, 1), (False, True): (1, -1), (False, False): (0, 0)}] * 7
    },
    {
        "name": "Incentivi Calanti",
        "rounds": [
            {(True, True): (10, 10), (True, False): (0, 15), (False, True): (15, 0), (False, False): (1, 1)},
            {(True, True): (5, 5), (True, False): (0, 7), (False, True): (7, 0), (False, False): (1, 1)},
            {(True, True): (2, 2), (True, False): (0, 3), (False, True): (3, 0), (False, False): (1, 1)},
        ]
    },
    {
        "name": "Harmony Game",
        "rounds": [{(True, True): (4, 4), (True, False): (3, 1), (False, True): (1, 3), (False, False): (0, 0)}] * 5
    },
    {
        "name": "Dilemma Estremo",
        "rounds": [{(True, True): (1, 1), (True, False): (0, 100), (False, True): (100, 0), (False, False): (0, 0)}] * 4
    },
    {
        "name": "Gioco Simmetrico Povero",
        "rounds": [{(True, True): (1, 1), (True, False): (-1, 2), (False, True): (2, -1), (False, False): (0, 0)}] * 10
    }
]

def getRandom():
    return random.choice(games)