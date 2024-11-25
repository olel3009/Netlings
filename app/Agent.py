from .Setting import IDManager
from .Setting import data
class Agent():
    def __init__(self,
                 x: float = -1,
                 y: float = -1,
                 r: float = -1,
                active: bool = False,
                speed: float = 10,
                food: int = 100,
             ):
        self.x = x
        self.y = y
        self.r = r
        self.active = active
        self.food = food
        self.speed = speed
        self.id = IDManager.getID()
        self.width = 10
        self.height = 10
        pass

    def move(self, dx=0, dy=0, dr=0):
        if(self.cordsInGameField(self.x  + dx, self.y + dy)):
            self.x += dx
            self.y += dy
            self.r += dr
        pass
    def cordsInGameField(self, x, y):
        environment_width = data["environmentSize"]["width"]
        environment_height = data["environmentSize"]["height"]

        if x < 0 or x > environment_width or y < 0 or y > environment_height:
            return False
        return True

    def calculate(self):
        pass

    def teleport(self, x, y, r = None):
        self.x = x
        self.y = y
        self.r = r
    
    def collect(self):
        return {
            "x": self.x,
            "y": self.y,
            "r": self.r,
            "active": self.active,
            "id": self.id,
            "type": self.__class__.__name__
        }
    def collision(self, instance):
        return None