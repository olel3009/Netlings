from app.Agent import Agent

class Netling(Agent):
    def __init__(self):
        super().__init__(-1, -1, -1, False)
        pass

    def collect(self):
        return super().collect()