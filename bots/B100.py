class bot:
    name = "B100"
    def __init__(self):
        self.last = None

    # Always returns False
    def play(self, choices, last):
        return False