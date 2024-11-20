class Enviroment:
    def __init__(self) -> None:
        self.agent = []
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