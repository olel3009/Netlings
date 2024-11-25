import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.AgentEnvironment import Enviroment

environment = Enviroment()
environment.moveAll()