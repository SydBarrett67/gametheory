class bot:
    name = "beatlast"
    def __init__(self):
        self.last = None

    # Return False for the first turn, opposes opponents in later rounds
    def play(self, choices, last):
        if last == None:
            return False
        return not last