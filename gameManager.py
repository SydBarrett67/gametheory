import random

import bots.titfortat as tft
import bots.beatlast as bl
import bots.greedy as gd
import games
games = games.games

# Globali
tournament = []
bots = [tft.bot(), bl.bot(), gd.bot()]
champ_pairs = []
for i in range(len(bots)):
    for j in range(i + 1, len(bots)):
        champ_pairs.append((bots[i], bots[j]))

#print(champ_pairs)

#p1 = random.choice(bots).bot()
#p2 = random.choice(bots).bot()

def playRound(p1, p2, game, round, turn):
    if turn == 0:
        res1 = p1.play(round, None)
        res2 = p2.play(round, None)
    else:
        res1 = p1.play(round, game[turn - 1]["results"][1])
        res2 = p2.play(round, game[turn - 1]["results"][0])

    # Punteggi
    pts1, pts2 = round[(res1, res2)]

    return {"results": [res1, res2], "pts": [pts1, pts2]}

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

def displayGameStats(res):
    
    s1 = sum(r["pts"][0] for r in res)
    s2 = sum(r["pts"][1] for r in res)
    
    print("----- RISULTATI FINALI GIOCO -----")
    print(f"P1 ({p1.name}): {s1} punti")
    print(f"P2 ({p2.name}): {s2} punti")
    print("----------------------------------\n")
    
    return s1, s2

def displayTournamentStats(bots = []):
    print("-" * 10)
    print("P1's final score: ", totalSums[0])
    print("P2's final score: ", totalSums[1])

def displayChampionshipStats(results):
    
    points = []

    # Get formatted string
    for name, score in results.items():
        # Formatted string
        str_points = f"{name}: {score}"
        points.append(str_points)

    print("----- FINAL STANDING -----")
    for i in points:
        print(i)

pair_index = 0
standings = {bot.name: 0 for bot in bots}

# Championship loop
while (pair_index < len(champ_pairs)):

    # Select two bots
    selected_bots = champ_pairs[pair_index]

    p1 = selected_bots[0]
    p2 = selected_bots[1]

    print(f"----- TOURNAMENT #", pair_index + 1, " -----")
    print(f"CHOSEN BOTS:\n P1: {p1.name}\n P2: {p2.name}\n")

    # Tournament
    gameIndex = 0
    while (gameIndex < len(games)):
        # Choose new game
        game = games[gameIndex]

        #print(f"CHOSEN GAME: {game['name']}\n")       

        # Game loop
        gameHistory = []
        turn = 0
        while (turn < len(game["rounds"])):
            
            # Select round
            round = game["rounds"][turn]

            # Get round results
            roundResults = playRound(p1, p2, gameHistory, round, turn)

            # Add round to game history
            gameHistory.append(roundResults)

            # Add to global point sum
            standings[p1.name] += roundResults["results"][0]
            standings[p2.name] += roundResults["results"][1]
            
            turn += 1

        tournament.append(gameHistory)
        #displayGameStats(gameHistory)
        gameIndex = gameIndex + 1

    pair_index += 1

    #displayTournamentStats()

displayChampionshipStats(standings)