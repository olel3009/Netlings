class IDManager:
    def __init__(self):
        self.id = -1

    def getID(self):
        self.id += 1
        return self.id