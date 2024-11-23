class Agent:
    def __init__(self,
                x: float,
                y: float,
                r: float,
                active: bool
                ):
        self.x = x
        self.y = y
        self.r = r
        self.active = active
        pass

    def move(self, dx, dy, dr):
        self.x += dx
        self.y += dy
        self.r += dr
        pass

    def teleport(self, x, y, r = None):
        self.x = x
        self.y = y
        if self.r != None:
            self.r = r
    
    def collect(self):
        return {
            "x": self.x,
            "y": self.y,
            "r": self.r,
            "active": self.active,
            "type": self.__class__.__name__
        }

