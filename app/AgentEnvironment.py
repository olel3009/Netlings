import random
import neat

from app.Netling import Netling
from app.Setting import data
from app.Quadtree import Quadtree

class Enviroment:
    def __init__(self) -> None:
        self.agent = []

        #Load Settings:
        self.config = data

        #Load Quadtree
        self.quadtree = Quadtree(0,0, data["environmentSize"]["width"], data["environmentSize"]["height"])

        #add Netlings to Enviroment:
        for i in range(self.config["netlingSpawnCount"]):
            x, y = self.randomPos()
            x = 0
            y = 0
            genome = neat.DefaultGenome(random.randint(0, 10000))
            netling = Netling(genome, x, y, True)
            self.agent.append(netling)
            self.quadtree.insert(netling)
        pass

    def moveAll(self):
        for agent in self.agent:
            #agent.calculate()
            pass
        self.checkCollision()
        return self.collectAll(False)

    def _overlaps(self, rect1, rect2):
        """Prüft, ob zwei Rechtecke sich überlappen."""
        return not (
            rect1[0] + rect1[2] <= rect2[0] or  # rect1 liegt links von rect2
            rect1[0] >= rect2[0] + rect2[2] or  # rect1 liegt rechts von rect2
            rect1[1] + rect1[3] <= rect2[1] or  # rect1 liegt oberhalb von rect2
            rect1[1] >= rect2[1] + rect2[3]    # rect1 liegt unterhalb von rect2
        )

    def checkCollision(self):
        for agent in self.agent:
            # Hole alle potenziell kollidierenden Agenten in der Nähe
            nearby_agents = self.quadtree.query(agent.getHitBox())

            # Prüfe jeden Agenten gegen die anderen in der Nähe
            for agent1 in nearby_agents:
                for agent2 in nearby_agents:
                    if agent1 != agent2:  # Vermeide Selbstvergleich
                        if self._overlaps(agent1.getHitBox().boundary, agent2.getHitBox().boundary):
                            print(f"Kollision erkannt zwischen {agent1} und {agent2}")
                            agent1.collision(agent2)
                            agent2.collision(agent1)

    def collectAll(self, debugging: bool):
        info = []
        for agent in self.agent:
            info.append(agent.collect())
        return info

    def randomPos(self):
        x = random.randint(0, data["environmentSize"]["width"])
        y = random.randint(0, data["environmentSize"]["height"])
        return x, y

    def getID(self, id):
        for agent in self.agent:
            if agent.id == id:
                return agent.collect()