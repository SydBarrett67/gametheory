class bot:
    name = "titfortat"
    def __init__(self):
        self.last = None

    def play(self, choices, last):
        if last == None:
            return True
        return last