from Agent import Agent

class Netling(Agent):
    def __init__(self):
        self.x = -1
        self.y = -1
        self.r = -1
        pass

    def collect(self):
        return super().collect()