from tsp_solver_Tasnim import random_search, hill_climbing, simulated_annealing

cities = [(0, 0), (1, 1), (2, 2), (3, 3)]

print("Random Search:", random_search(cities, iterations=1000))
print("Hill Climbing:", hill_climbing(cities))
print("Simulated Annealing:", simulated_annealing(cities, temp=1000, cooling_rate=0.995))
