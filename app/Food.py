from pyparsing import oneOf
from EventManager import Events
from .Object import BaseModell
from .Agent import Agent
from EventManager import Events
class Food(BaseModell):
    def __init__(self, x, y, r, foodCount, height=10, width=10, eventManager=None):
        super().__init__(x, y, r, height, width)
        self.foodCount = foodCount
        self.eventManager = eventManager

    def onCollision(self, object):
        if isinstance(object, Agent):
            object.feed(self.foodCount)
        self.eventManager.add_event(Events.DEATH, self)
        pass

    def onDeath(self):
        self.events.append(Events.isDeath)

