class beatlast:
    def __init__(self):
        self.last = None

    def play(self, last):
        if last == None:
            return False
        return not last