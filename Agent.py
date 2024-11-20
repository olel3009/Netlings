class Agent:

    def __init__(self, x: float, y: float, r: float):
        self.x = x
        self.y = y
        self.r = r
        pass

    def move(self, dx, dy, dr):
        self.x = dx
        self.y = dy
        self.r = dr
        pass
