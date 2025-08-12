!pip install matplotlib deap

import random
import matplotlib.pyplot as plt
import numpy as np
from deap import base,creator,tools,algorithms

num_locations = 10
locations = [(random.randint(0,100),random.randint(0,100)) for _ in range(num_locations)]
depot = (50,50)
num_vehicles = 3
creator.create("FitnessMin",base.Fitness,weights = (-1.0,-1.0))
creator.create("Individual",list,fitness=creator.FitnessMin)

creator.create("FitnessMin",base.Fitness,weights=(-1.0,-1.0))
creator.create("Individual",list,fitness = creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("indices",random.sample,range(num_locations),num_locations)
toolbox.register("individual",tools.initIterate,creator.Individual,toolbox.indices)
toolbox.register("population",tools.initRepeat,list,toolbox.individual)

def evalVRP(individual):
    # TODO: Task 3 - Write the fitness evaluation function
    # HINT: Calculate the total distance of routes and the standard deviation among the distances and return (distance, std dev)
    total_distance =0
    distances = []
    for i in range(num_vehicles):
      vehicle_route = [depot]+[locations[individual[j]] for j in range(i,len(individual),num_vehicles)]+[depot]
      vehicle_distance = sum(np.linalg.norm(np.array(vehicle_route[k+1])-np.array(vehicle_route[k])) for k in range(len(vehicle_route)-1))
      total_distance += vehicle_distance
      distances.append(vehicle_distance)
    balance_penalty = np.std(distances)
    return total_distance, balance_penalty

toolbox.register("evaluate", evalVRP)
toolbox.register("select",tools.selTournament,tournsize=3)
toolbox.register("mutate",tools.mutShuffleIndexes,indpb=0.05)
toolbox.register("mate",tools.cxPartialyMatched)


def plot_routes(individual,title ="Routes"):
  plt.figure()
  for(x,y) in locations:
      plt.plot(x,y,'bo')
  plt.plot(depot[0],depot[1],'rs')
  for i in range(num_vehicles):
    vehicle_route = [depot]+[locations[individual[j]] for j in range(i,len(individual),num_vehicles)] + [depot]
    plt.plot(depot[0],depot[1],'rs')
  for i in range(num_vehicles):
        vehicle_route = [depot] + [locations[individual[j]] for j in range(i, len(individual), num_vehicles)] + [depot]
        plt.plot(*zip(*vehicle_route), '-')

  plt.title(title)
  plt.xlabel('X Coordinate')
  plt.ylabel('Y Coordinate')
  plt.show()

def main():
  random.seed(42)
  pop = toolbox.population(n=300)
  hof = tools.HallOfFame(1)

  stats = tools.Statistics(lambda ind:ind.fitness.values)
  stats.register("avg", np.mean)
  stats.register("min", np.min)

  algorithms.eaSimple(pop, toolbox, 0.7,0.2,300,stats = stats,halloffame=hof)

  plot_routes(hof[0],"optimal Route")
  return pop,stats,hof

if __name__ == "__main__":
  main()


