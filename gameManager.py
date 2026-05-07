import random

import bots.titfortat as tft
import bots.beatlast as bl
import bots.greedy as gd
import games

# Globali
gameHistory = []
bots = [tft, bl, gd]

games = games.games
p1 = random.choice(bots).bot()
p2 = random.choice(bots).bot()

def playRound(p1, p2, round):
    global turn
    if turn == 0:
        res1 = p1.play(round, None)
        res2 = p2.play(round, None)
    else:
        res1 = p1.play(round, gameHistory[turn - 1]["results"][1])
        res2 = p2.play(round, gameHistory[turn - 1]["results"][0])

    # Punteggi
    pts1, pts2 = round[(res1, res2)]

    gameHistory.append({"results": [res1, res2], "pts": [pts1, pts2]})
    return [pts1, pts2]

def displayRoundStats(round_data):
    global turn
    print(f"----- ROUND {turn} -----\n")
    print(f"Payoffs: \n{round_data}\n")
    print("--------------------")
    
    print(f"P1 played: {gameHistory[turn]['results'][0]}")
    print(f"P2 played: {gameHistory[turn]['results'][1]}")
    
    print("----- RESULTS -----\n")
    print(f"P1 gained {gameHistory[turn]['pts'][0]} points\n")
    print(f"P2 gained {gameHistory[turn]['pts'][1]} points\n")
    print("--------------------\n\n\n")

def displayGameStats(game_data):
    rounds = len(game_data["rounds"])
    res = gameHistory[-rounds:] 
    
    s1 = sum(r["pts"][0] for r in res)
    s2 = sum(r["pts"][1] for r in res)
    
    print("----- RISULTATI FINALI GIOCO -----")
    print(f"P1 ({p1.name}): {s1} punti")
    print(f"P2 ({p2.name}): {s2} punti")
    print("----------------------------------\n")
    
    return s1, s2

gameIndex = 0
totalSums = [0,0]
while (gameIndex < len(games)):
    turn = 0
    game = games[gameIndex]

    print(f"CHOSEN GAME {game['name']}\n")
    print(f"CHOSEN BOTS:\n P1: {p1.name}\n P2: {p2.name}]\n")
    while (turn < len(game["rounds"])):
        pts = playRound(p1, p2, game["rounds"][turn])

        totalSums[0] += pts[0]
        totalSums[1] += pts[1]
        
        turn = turn + 1

    displayGameStats(game)
    gameIndex = gameIndex + 1