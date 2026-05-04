import bots.titfortat as tft
import bots.beatlast as bl
import games

# Globali
turn = 0
gameHistory = []

def playRound(p1, p2, round):
    global turn
    if turn == 0:
        res1 = p1.play(None)
        res2 = p2.play(None)
    else:
        res1 = p1.play(gameHistory[turn - 1]["results"][1])
        res2 = p2.play(gameHistory[turn - 1]["results"][0])

    # Punteggi
    pts1, pts2 = round[(res1, res2)]

    gameHistory.append({"results": [res1, res2], "pts": [pts1, pts2]})

    

game = games.getRandom()
p1 = bl.beatlast()
p2 = tft.titfortat()

while (turn < len(game["rounds"])):
    playRound(p1, p2, game["rounds"][turn])
    turn = turn + 1

sums = [0, 0]
for i in range(len(gameHistory)):
    sums[0] = sums[0] + gameHistory[i]["pts"][0]
    sums[1] = sums[1] + gameHistory[i]["pts"][1]

print("P1: ", sums[0], "\nP2: ", sums[1])