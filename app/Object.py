from .IDManager import IDManager
class BaseModell():
    def __init__(self, x, y, r, height, width):
        self.x = x
        self.y = y
        self.r = r
        self.id = IDManager.getID()
        self.width = width
        self.height = height

    def teleport(self, x, y, r = None):
        self.x = x
        self.y = y
        self.r = r

    def collect(self):
        return {
            "x": self.x,
            "y": self.y,
            "r": self.r,
            "width": self.width,
            "height": self.height,
            "active": self.active,
            "id": self.id,
            "type": self.__class__.__name__
        }