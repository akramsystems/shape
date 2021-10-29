"""This code simulates the Ronald Ross algorithm
of the distance travel by a misquito given the 
duration of their life.

Author: Ali Akram
"""
from random import random, randint
from enum import Enum
from collections import Counter

final_position=Counter()
final_distances=Counter()
INITIAL_POPULATION_SIZE=1000 # misquitos
INITIAL_LIFESPAN=10 # days

#ACTION (Flying) CHOICES
class Direction(Enum):
    NORTH=(1,0)
    SOUTH=(-1,0)
    EAST=(0,1)
    WEST=(-1,0)

# AGENT
class Misquito:
    def __init__(self, lifespan_in_days:int,initial_x=0, initial_y=0):
        # INITIAL STATE
        self.initial_x = initial_x
        self.initial_y = initial_y
        self.initial_lifespan = lifespan_in_days
        
        # CURRENT STATE
        self.lifespan = lifespan_in_days
        self.x=initial_x
        self.y=initial_y
        
        # POSSIBLE ACTIONS
        ACTIONS={"fly"}
        self.choices = [dir for dir in Direction]
    def get_position(self):
        """get position of the misquito at current state"""        
        return (self.x, self.y)
    def get_distance_travelled(self):
        """see the distance misquito has travelled since initial state"""        
        delta_x = self.x - self.initial_x
        delta_y = self.y - self.initial_y
        distance = (delta_x**2+delta_y**2)**.5 # L2 Norm
        return distance
    def fly(self):
        """one of the possible actions a misquito can do"""        
        delta_x, delta_y = self.decide_on_direction()
        self.x+= delta_x
        self.y+= delta_y
        # print("Misquito is now at position",self.get_position())
        self.lifespan-=1 # lost a day from its lifespan (COST OF FLYING)
    def decide_on_direction(self):
        num_choices = len(self.choices)-1
        direction = self.choices[randint(0, num_choices)] # randomly picking a choice
        # print(f'This Misquito Decided to go {direction.name}')
        return direction.value
    def is_alive(self):
        return True if self.lifespan > 0 else False


#Agent generator Factory
class MisquitoFactory:
    def __init__(self, number_of_misquitos:int, life_span):
        self.Misquitos = [Misquito(life_span) for _ in range(number_of_misquitos)]
        print(f"Created a population of {number_of_misquitos} with a life_span of {life_span}")
    def get_misquitos(self):
        return self.Misquitos


if __name__ == "__main__":
    # Generate the inital population of misquitos
    m_factory = MisquitoFactory(number_of_misquitos=INITIAL_POPULATION_SIZE,life_span=INITIAL_LIFESPAN)
    Misquitos = m_factory.get_misquitos()
    
    # Simulate the misquitos traveling through and environment
    for m in Misquitos:
        while m.is_alive():
            m.fly()
        final_position[m.get_position()]+=1
        # print(f"Misquito died at {m.get_position()}")
    
    final_distances=[]
    for m in Misquitos:
        final_distances.append(m.get_distance_travelled())
    
    avg_distance = sum(final_distances)/len(final_distances)
    print(f'Average distance travelled: {avg_distance}')