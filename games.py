import random

games = [
    {
        "rounds": [
            {(True, True): (3, 3), (True, False): (0, 5), (False, True): (5, 0), (False, False): (1, 1)},
            {(True, True): (3, 3), (True, False): (0, 5), (False, True): (5, 0), (False, False): (1, 1)},
            {(True, True): (3, 3), (True, False): (0, 5), (False, True): (5, 0), (False, False): (1, 1)},
            {(True, True): (3, 3), (True, False): (0, 5), (False, True): (5, 0), (False, False): (1, 1)},
            {(True, True): (3, 3), (True, False): (0, 5), (False, True): (5, 0), (False, False): (1, 1)},
            {(True, True): (3, 3), (True, False): (0, 5), (False, True): (5, 0), (False, False): (1, 1)},
            {(True, True): (3, 3), (True, False): (0, 5), (False, True): (5, 0), (False, False): (1, 1)},
            {(True, True): (3, 3), (True, False): (0, 5), (False, True): (5, 0), (False, False): (1, 1)},
            {(True, True): (3, 3), (True, False): (0, 5), (False, True): (5, 0), (False, False): (1, 1)},
            {(True, True): (3, 3), (True, False): (0, 5), (False, True): (5, 0), (False, False): (1, 1)},
        ]
    }
]

def getRandom():
    return random.choice(games)