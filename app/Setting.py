import neat
from .IDManager import IDManager
from app.Quadtree import Quadtree

data = {
    "environmentSize": {"width": 1000, "height": 1000},
    "netlingSpawnCount": 100
}
config_path = "app/config-feedforward"

NEATConfig =  neat.Config(neat.DefaultGenome, neat.DefaultReproduction, neat.DefaultSpeciesSet, neat.DefaultStagnation, config_path)

IDManager = IDManager()