class bot:
    name = "minimax"
    def __init__(self):
        self.last = None

    # Return the option that doesn't contain the largest payoff for the opponent
    def play(self, choices, last):
        bad_move = max(choices.items(), key=lambda x: x[1][1])[0][0]
        
        possible_moves = list({m1 for (m1, m2) in choices.keys()})
        
        for m in possible_moves:
            if m != bad_move:
                return m
        
        return possible_moves[0]