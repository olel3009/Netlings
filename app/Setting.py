import neat
from IDManager import IDManager

data = {
    "environmentSize": {"width": 1000, "height": 1000},
    "netlingSpawnCount": 10
}
config_path = "app/config-feedforward"
NEATConfig =  neat.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

IDManager = IDManager()