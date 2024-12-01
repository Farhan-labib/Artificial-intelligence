import random

def get_input():
    N, T = map(int, input("Enter the number of courses (N) and the number of timeslots (T): ").split())
    courses = []
    for i in range(N):
        course_code = input(f"Enter course code for course: ")
        courses.append(course_code)
    
    return N, T, courses

N, T, courses = get_input()
L = N * T

def chromosome(L):
    chr1 = ""
    for i in range(L):
        chr1 += str(random.randint(0, 1))
    return chr1

def fitness(chr, N, T):
    overlap = 0
    consistency = 0
    for i in range(T):
        count_ones = 0
        for j in range(N):
            count_ones += int(chr[j * T + i])
        if count_ones > 1:
            overlap += count_ones - 1
    
    for j in range(N):
        count_ones = 0
        for i in range(T):
            count_ones += int(chr[j * T + i])
        if count_ones == 0:
            consistency += 1
        elif count_ones > 1:
            consistency += count_ones - 1
    
    fit = -(overlap + consistency)
    return fit

def select_parents(population):
    parent1 = random.choice(population)
    parent2 = random.choice(population)
    return parent1, parent2

def single_point_crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

#PART 2
def two_point_crossover(parent1, parent2):
    point1 = random.randint(1, len(parent1) - 2)
    point2 = random.randint(point1 + 1, len(parent1) - 1)
    
    child1 = parent1[:point1] + parent2[point1:point2] + parent1[point2:]
    child2 = parent2[:point1] + parent1[point1:point2] + parent2[point2:]
    
    print("Two-point crossover:")
    print("Parent 1:", parent1, "Parent 2:", parent2) 
    print("Child 1", child1, "Child 2", child2)

def mutation(chr):
    index = random.randint(0, len(chr) - 1)
    if chr[index] == '0':
        chr = chr[:index] + '1' + chr[index + 1:]
    else:
        chr = chr[:index] + '0' + chr[index + 1:]
    return chr

def create_population(population_size, L):
    population = []
    for i in range(population_size):
        population.append(chromosome(L))
    return population

#PART 3
def tournament_selection(population, tournament_size=3):
    tournament = random.sample(population, tournament_size)
    tournament_fitness = []
    for chromosome in tournament:
        fitness_value = fitness(chromosome, N, T)
        tournament_fitness.append((chromosome, fitness_value))
    tournament_fitness.sort(key=lambda x: x[1], reverse=True)
    
    best_parent = tournament_fitness[0][0]
    
    tournament_participants = []
    for chromosome in tournament_fitness:
        tournament_participants.append(chromosome[0])
    
    print("Tournament Participants:", tournament_participants)
    print("Best Parent (From Tournament Selection):", best_parent)
    return best_parent

def genetic_algorithm(population_size, max_iterations, N, T):
    population = create_population(population_size, N * T)
    best_fitness = -float('inf')
    best_chromosome = None
    iterations = 0
    
    while iterations < max_iterations:
        population_fitness = []
        for chromosome in population:
            fitness_value = fitness(chromosome, N, T)
            population_fitness.append((chromosome, fitness_value))
        
        population_fitness.sort(key=lambda x: x[1], reverse=True)
        
        if population_fitness[0][1] > best_fitness:
            best_fitness = population_fitness[0][1]
            best_chromosome = population_fitness[0][0]
        
        parent1, parent2 = select_parents(population)
        child1, child2 = single_point_crossover(parent1, parent2)
        child1 = mutation(child1)
        child2 = mutation(child2)
        
        population[-2] = child1
        population[-1] = child2
        
        iterations += 1
    
    return best_chromosome, best_fitness

population_size = 4
max_iterations = 100

best_schedule, best_fitness = genetic_algorithm(population_size, max_iterations, N, T)
print("Best Schedule:", best_schedule)
print("Best Fitness:", best_fitness)

#PART 2 AND 3 
#population = create_population(population_size, N * T)
#two_point_crossover(population[0], population[1])
#tournament_selection(population)
