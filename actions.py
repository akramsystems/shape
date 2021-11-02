from abc import ABC
from enum import Enum
from agents import State
from random import randint
#ACTION (Flying) CHOICES
class Direction(Enum):
    NORTH=(0,1)
    SOUTH=(0,-1)
    EAST=(1,0)
    WEST=(-1,0)

class Action(ABC):
    def __init__(self, name:str):
        self.name=name
    def planning(self):
        """logic on how we want to execute the action go here
        """        
        raise NotImplementedError
    def execute(self, state: State):
        """This functions goal is to update the state
        """
        raise NotImplementedError

class FlyingAction(Action):
    def __init__(self,x=0,y=0):
        self.name = "Fly"
        self.direction = None
    def planning(self):
        """choose direction to fly in
        """
        self.direction = randint(0, len(Direction)-1)
    def execute(self, state: State):
        """Update state to fly in that direction
        """
        self.planning()
        state.x = self.direction[0]
        state.y = self.direction[1]