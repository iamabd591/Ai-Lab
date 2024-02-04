import numpy as np


def initialize_population(population_size, chromosome_length):
    return np.random.randint(2, size=(population_size, chromosome_length))


def evaluate_fitness(chromosome):
    x = int(''.join(map(str, chromosome)), 2)
    return -x**2 + 200*x


def roulette_wheel_selection(population, fitness_values):
    probabilities = fitness_values / np.sum(fitness_values)
    selected_indices = np.random.choice(
        range(len(population)), size=len(population), p=probabilities)
    return population[selected_indices]


def crossover(parent1, parent2):
    crossover_point = np.random.randint(1, len(parent1))
    child1 = np.concatenate(
        (parent1[:crossover_point], parent2[crossover_point:]))
    child2 = np.concatenate(
        (parent2[:crossover_point], parent1[crossover_point:]))
    return child1, child2


def mutate(chromosome, mutation_rate):
    if np.random.rand() < mutation_rate:
        mutation_point = np.random.randint(1, len(chromosome) - 1)
        chromosome[mutation_point-1:mutation_point+1] = 1 - \
            chromosome[mutation_point-1:mutation_point+1]


def genetic_algorithm(chromosome_length=8, population_size=8, max_iterations=3, fitness_criteria=0.9 * (-13999), crossover_prob=0.7, mutation_rate=0.1):
    # Initialize population
    population = initialize_population(population_size, chromosome_length)

    for iteration in range(max_iterations):
        # Evaluate Fitness
        fitness_values = np.array([evaluate_fitness(chromosome)
                                  for chromosome in population])

        # Check if fitness criteria met
        if np.any(fitness_values >= fitness_criteria):
            print("Fitness criteria met!")
            break

        # Roulette Wheel Selection
        selected_parents = roulette_wheel_selection(population, fitness_values)

        # Crossover
        crossed_children = []
        for i in range(0, len(selected_parents), 2):
            if np.random.rand() < crossover_prob:
                child1, child2 = crossover(
                    selected_parents[i], selected_parents[i+1])
                crossed_children.extend([child1, child2])
            else:
                crossed_children.extend(
                    [selected_parents[i], selected_parents[i+1]])

        # Mutation
        for i in range(len(crossed_children)):
            mutate(crossed_children[i], mutation_rate)

        # Update population
        population = np.vstack([population, crossed_children])
        sorted_indices = np.argsort(fitness_values)
        population = population[sorted_indices[:population_size]]

        # Display information
        best_chromosome = population[np.argmax(fitness_values)]
        print(
            f"Iteration {iteration+1}, Best Chromosome: {best_chromosome}, Fitness: {max(fitness_values)}")

    # Display the chromosome with the minimum value
    min_fitness_index = np.argmin(fitness_values)
    best_chromosome = population[min_fitness_index]
    print(
        f"Chromosome with minimum value: {best_chromosome}, Fitness: {fitness_values[min_fitness_index]}")


# Run the genetic algorithm
genetic_algorithm()
