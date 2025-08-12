import random
import numpy as np
from deap import base, creator, tools, algorithms

def run_genetic_vrp(n_locations=10, n_vehicles=3, pop_size=300, mutation_rate=0.2, ngen=300, seed=42):
    """
    Runs the Vehicle Routing Problem Genetic Algorithm.
    
    Parameters:
        n_locations (int): Number of locations (excluding depot).
        n_vehicles (int): Number of vehicles.
        pop_size (int): Population size.
        mutation_rate (float): Mutation probability.
        ngen (int): Number of generations.
        seed (int): Random seed for reproducibility.

    Returns:
        best_route (list): Best individual (route) found.
        fitness_history (list): Best fitness value per generation.
        locations (list): Coordinates of locations.
        depot (tuple): Coordinates of the depot.
    """

    # Set random seed
    random.seed(seed)
    np.random.seed(seed)

    # Generate locations and depot
    locations = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(n_locations)]
    depot = (50, 50)

    # Create DEAP classes
    creator.create("FitnessMin", base.Fitness, weights=(-1.0, -1.0))
    creator.create("Individual", list, fitness=creator.FitnessMin)

    toolbox = base.Toolbox()
    toolbox.register("indices", random.sample, range(n_locations), n_locations)
    toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)

    # Evaluation function
    def evalVRP(individual):
        total_distance = 0
        distances = []
        for i in range(n_vehicles):
            vehicle_route = [depot] + [locations[individual[j]] for j in range(i, len(individual), n_vehicles)] + [depot]
            vehicle_distance = sum(
                np.linalg.norm(np.array(vehicle_route[k+1]) - np.array(vehicle_route[k]))
                for k in range(len(vehicle_route) - 1)
            )
            total_distance += vehicle_distance
            distances.append(vehicle_distance)
        balance_penalty = np.std(distances)
        return total_distance, balance_penalty

    # Register GA operators
    toolbox.register("evaluate", evalVRP)
    toolbox.register("select", tools.selTournament, tournsize=3)
    toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
    toolbox.register("mate", tools.cxPartialyMatched)

    # Prepare statistics
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", np.mean)
    stats.register("min", np.min)

    # Initialize population & Hall of Fame
    pop = toolbox.population(n=pop_size)
    hof = tools.HallOfFame(1)
    fitness_history = []

    # Modified eaSimple to track best fitness
    for gen in range(ngen):
        offspring = algorithms.varAnd(pop, toolbox, cxpb=0.7, mutpb=mutation_rate)
        fits = list(map(toolbox.evaluate, offspring))
        for fit, ind in zip(fits, offspring):
            ind.fitness.values = fit
        pop = toolbox.select(offspring, k=len(pop))
        hof.update(pop)
        best_fit = min(ind.fitness.values[0] for ind in pop)
        fitness_history.append(best_fit)

    return hof[0], fitness_history, locations, depot
