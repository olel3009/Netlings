from Netling import Netling

class Enviroment:
    def __init__(self, agentlen) -> None:
        self.agent = []
        for i in range(agentlen):
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
            info.append(agent.collect(debugging))
        pass