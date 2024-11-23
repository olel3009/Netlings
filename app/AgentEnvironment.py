from app.Netling import Netling
from app.Setting import data

class Enviroment:
    def __init__(self) -> None:
        self.agent = []

        #Load Settings:
        self.config = data

        #add Netlings to Enviroment:
        for i in range(self.config["netlingSpawnCount"]):
            self.agent.append(Netling())
        pass

    def move(self):
        for agent in self.agent:
            agent.calculate()
        return self.collectAll()

    def calculate(self):
        #TODO
        pass

    def collectAll(self, debugging: bool):
        info = []
        for agent in self.agent:
            info.append(agent.collect())
        return info