import random
import neat

from app.Netling import Netling
from app.Setting import data

class Enviroment:
    def __init__(self) -> None:
        self.agent = []

        #Load Settings:
        self.config = data

        #add Netlings to Enviroment:
        for i in range(self.config["netlingSpawnCount"]):
            x, y = self.randomPos()
            genome = neat.DefaultGenome(random.randint(0, 10000))
            self.agent.append(Netling(genome, x, y, True))
        pass

    def moveAll(self):
        for agent in self.agent:
            agent.move()
        return self.collectAll(False)

    def collectAll(self, debugging: bool):
        info = []
        for agent in self.agent:
            info.append(agent.collect())
        return info

    def randomPos(self):
        x = random.randint(0, data["environmentSize"]["width"])
        y = random.randint(0, data["environmentSize"]["height"])
        return x, y