import neat

from app.Agent import Agent
from app.Setting import NEATConfig
from app.Quadtree import Quadtree

class Netling(Agent):
    def __init__(self, genome, x, y, activate):
        super().__init__(x, y, 0, activate)
        self.brain = neat.nn.FeedForwardNetwork.create(genome, NEATConfig)
        self.genome = genome
        pass

    def move(self, dx, dy, dr):
        super().move(dx, dy, dr)

    def calculate(self):
        output = self.brain_activate()
        dx = (output[0] - 0.5) * self.speed
        dy = (output[0] - 0.5) * self.speed
        dr = 0
        self.move(dx, dy, dr)

    def getHitBox(self):
        return Quadtree(self.x - 10, self.y - 10, self.width + 10, self.height + 10)

    def brain_activate(self):
        return self.brain.activate([self.x, self.y])

    def collect(self):
        return super().collect()