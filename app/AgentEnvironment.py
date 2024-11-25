import random
import neat
import logging

from .Netling import Netling
from .Setting import data
from .Quadtree import Quadtree
from .Setting import NEATConfig
from .EventManager import EventManager
from .EventManager import Events

class Enviroment:
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
        self.agent = []

        self.eventManager = EventManager()
        self.logger.info("EventManager created")

        self.config = data
        self.logger.info("Config loaded")

        self.quadtree = Quadtree(0,0, data["environmentSize"]["width"], data["environmentSize"]["height"])
        self.logger.info("Quadtree created")

        for i in range(self.config["netlingSpawnCount"]):
            x, y = self.randomPos()
            genome = NEATConfig.genome_type(i)
            genome.configure_new(NEATConfig.genome_config)
            netling = Netling(genome, x, y, True, eventManager=self.eventManager)
            self.agent.append(netling)
            self.quadtree.insert(netling)
        self.logger.info("Netlings created")

    def moveAll(self):
        for agent in self.agent:
            agent.calculate()
            pass
        self._checkCollision()
        self._evalEvents()
        return self.collectAll(False)

    def _overlaps(self, rect1, rect2):
        return not (
            rect1[0] + rect1[2] <= rect2[0] or  # rect1 liegt links von rect2
            rect1[0] >= rect2[0] + rect2[2] or  # rect1 liegt rechts von rect2
            rect1[1] + rect1[3] <= rect2[1] or  # rect1 liegt oberhalb von rect2
            rect1[1] >= rect2[1] + rect2[3]
        )

    def _checkCollision(self):
        for agent in self.agent:
            nearby_agents = self.quadtree.query(agent.getHitBox())
            for agent1 in nearby_agents:
                for agent2 in nearby_agents:
                    if agent1 != agent2:
                        if self._overlaps(agent1.getHitBox().boundary, agent2.getHitBox().boundary):
                            self.eventManager.add_event(Events.COLLISSION, agent1, target=agent2)
                            self.logger.debug(f"Collision detected between {agent1.id} and {agent2.id}")

    def _evalEvents(self):
        events_to_process = []
        while not self.eventManager.events.empty():
            events_to_process.append(self.eventManager.events.get()) #TODO: Check if this is the right way to get the event

        for e in events_to_process:
            if e["type"] == Events.DEATH:
                e["source"].onDeath()
                self._removeObject(e["source"])
                self.logger.debug(f"Death of {e['source'].id} evaluated")
            elif e["type"] == Events.COLLISSION:
                e["source"].onCollission(e["target"])
                e["target"].onCollission(e["source"])
                self.logger.debug(f"Collision between {e['source'].id} and {e['target'].id} evaluated")

    def _removeObject(self, object):
        self.agent.remove(object)
        self.quadtree.remove(object)
        self.logger.debug(f"Object {object.id} removed")

    def collectAll(self, debugging: bool):
        info = []
        for agent in self.agent:
            info.append(agent.collect())
        self.logger.debug(f"Collected all objects")
        return info

    def randomPos(self):
        x = random.randint(0, data["environmentSize"]["width"])
        y = random.randint(0, data["environmentSize"]["height"])
        self.logger.debug(f"Random position generated: {x}, {y}")
        return x, y

    def getID(self, id):
        for agent in self.agent:
            if agent.id == id:
                return agent.collect()