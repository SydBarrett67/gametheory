class bot:
    name = "generous"
    def __init__(self):
        self.last = None

    # Return the highest payoff for the opponent
    def play(self, choices, last):
        best_val = -1
        best_move = True
        
        for (m1, m2), (p1, p2) in choices.items():
            if p2 > best_val:
                best_val = p2
                best_move = m1
        return best_move