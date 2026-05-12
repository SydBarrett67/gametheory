class bot:
    name = "A100"
    def __init__(self):
        self.last = None

    # Always returns True
    def play(self, choices, last):
        return True