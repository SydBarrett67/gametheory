class bot:
    name = "greedy"
    def __init__(self):
        self.last = None

    def play(self, choices, last):
        best_val = -1
        best_move = True
        
        for (m1, m2), (p1, p2) in choices.items():
            if p1 > best_val:
                best_val = p1
                best_move = m1
        return best_move