"""This code simulates the Ronald Ross algorithm
of the distance travel by a misquito given the 
duration of their life.

Author: Ali Akram
"""
from collections import Counter
import matplotlib.pyplot as plt
from agents import MisquitoFactory
from plotter import ScatterPlot

final_position=Counter(); final_distances=Counter()
INITIAL_POPULATION_SIZE=100 # misquitos
INITIAL_LIFESPAN=10 # days


def calculateAverageDistanceTravelled(Misquitos):
    final_distances=[m.get_distance_travelled() for m in Misquitos]
    
    avg_distance = sum(final_distances)/len(final_distances)
    
    print(f'Average distance travelled: {avg_distance}')

if __name__ == "__main__":
    # Generate the inital population of misquitos
    m_factory = MisquitoFactory(number_of_misquitos=INITIAL_POPULATION_SIZE,life_span=INITIAL_LIFESPAN)
    Misquitos = m_factory.get_misquitos()
    Plot = ScatterPlot() 
    
    # Simulate the misquitos traveling through and environment
    for m in Misquitos:
        while m.is_alive():
            m.fly()
        final_x,final_y = m.get_position()
        final_position[(final_x,final_y)]+=1
        Plot.addPoint(final_x,final_y)

    calculateAverageDistanceTravelled(Misquitos)
    
    Plot.display()