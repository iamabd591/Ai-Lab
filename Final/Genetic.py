import random
population_size = 100
chromosome_length = 20
mutation_rate = 0.01
num_generations = 50

def fitness_function(chromosome):

    value = int(''.join(map(str, chromosome)), 2)

    fitness = value * value
    return fitness

def generate_population():
    population = []

    for _ in range(population_size):
        chromosome = [random.randint(0, 1) for _ in range(chromosome_length)]
        population.append(chromosome)
    return population

def crossover(parent1, parent2):
    crossover_point = random.randint(0, chromosome_length - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child


def mutate(individual):
    for i in range(chromosome_length):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]  # Flip the bit


def genetic_algorithm():
    population = generate_population()

    for generation in range(num_generations):

        fitness_scores = [fitness_function(chromosome)
                          for chromosome in population]

        parents = random.choices(population, weights=fitness_scores, k=2)

        offspring = [crossover(parents[0], parents[1])
                     for _ in range(population_size)]

        for individual in offspring:
            mutate(individual)

        population = offspring

    best_individual = max(population, key=fitness_function)
    best_fitness = fitness_function(best_individual)

    return best_individual, best_fitness


best_solution, best_fitness = genetic_algorithm()

print("Best Solution:", best_solution)
print("Best Fitness:", best_fitness)