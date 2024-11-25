from .Object import BaseModell
from .Setting import IDManager
from .Setting import data
from .Object import BaseModell
class Agent(BaseModell):
    def __init__(self,
                 x: float = -1,
                 y: float = -1,
                 r: float = -1,
                active: bool = False,
                speed: float = 10,
                food: int = 100,
                width: int = 10,
                height: int = 10
             ):
        super().__init__(x, y, r, width, heigt)
        self.active = active
        self.food = food
        self.speed = speed
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

    def collision(self, instance):
        return None