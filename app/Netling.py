import neat
import math
from .Agent import Agent
from .Setting import NEATConfig
from .Quadtree import Quadtree

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

        # Berechnung des hypothetischen Werts (hyp)
        hyp = (output[0] - 0.5) * self.speed

        # Umrechnen von output[1] in den Winkelbereich [0, 360]
        angle = output[1] * 360

        # Umrechnung in Radianten für die trigonometrischen Funktionen
        angle_rad = math.radians(angle)

        # Berechnung der relativen Koordinaten
        dx = math.cos(angle_rad) * hyp
        dy = math.sin(angle_rad) * hyp

        # Bewegung durchführen
        self.move(dx, dy, angle)

    def getHitBox(self):
        return Quadtree(self.x - 10, self.y - 10, self.width + 10, self.height + 10)

    def brain_activate(self):
        act = self.brain.activate([self.x, self.y])
        return act

    def collect(self):
        return super().collect()