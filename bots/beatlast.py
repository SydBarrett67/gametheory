class bot:
    name = "beatlast"
    def __init__(self):
        self.last = None

    def play(self, choices, last):
        if last == None:
            return False
        return not last