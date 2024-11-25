from app.Setting import IDManager
class BaseModell():
    def __init__(self, x, y, r, height, width, eventManager):
        self.x = x
        self.y = y
        self.r = r
        self.id = IDManager.getID()
        self.width = width
        self.height = height
        self.eventManager = eventManager

    def teleport(self, x, y, r = None):
        self.x = x
        self.y = y
        self.r = r

    def onCollision(self, object):
        pass

    def onDeath(self):
        pass

    def getType(self):
        return self.__class__.__name__

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