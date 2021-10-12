"""This code simulates the Ronald Ross algorithm
of the distance travel by a misquito given the 
duration of their life.

Author: Ali Akram
"""
from random import random, randint
from enum import Enum
from collections import Counter

final_distance=Counter()

class Direction(Enum):
    NORTH=(1,0)
    SOUTH=(-1,0)

class Misquito:
    def __init__(self, lifespan_in_days:int):
        self.lifespan = lifespan_in_days
        self.x=0
        self.y=0
        self.choices = [dir for dir in Direction]
    def get_position(self):
        return (self.x, self.y)
    def fly(self):
        delta_x, delta_y = self.make_decision()
        self.x+= delta_x
        self.y+= delta_y
        print("Misquito is now at position",self.get_position())
        self.lifespan-=1 # lost a day from its lifespan
    def make_decision(self):
        num_choices = len(self.choices)-1
        direction = self.choices[randint(0, num_choices)]
        print(f'This Misquito Decided to go {direction.name}')
        return direction.value
    def is_alive(self):
        return True if self.lifespan > 0 else False

class MisquitoFactory:
    def __init__(self, number_of_misquitos:int, life_span):
        self.Misquitos = [Misquito(life_span) for _ in range(number_of_misquitos)]
    def get_misquitos(self):
        return self.Misquitos

if __name__ == "__main__":
    m_factory = MisquitoFactory(number_of_misquitos=1000, life_span=10)
    Misquitos = m_factory.get_misquitos()
    for m in Misquitos:
        while m.is_alive():
            m.fly()
        final_distance[m.get_position()]+=1
        print(f"Misquito died at {m.get_position()}")
