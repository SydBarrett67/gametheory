class bot:
    name = "titfortat"
    def __init__(self):
        self.last = None

    # Return True for the first turn, copies opponent in later rounds
    def play(self, choices, last):
        if last == None:
            return True
        return last