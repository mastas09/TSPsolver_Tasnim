# TSPsolver_Tasnim

## 🗂️ Project Structure
tsp_solver_Tasnim/
├── algorithms/
│   ├── random_search.py
│   ├── hill_climbing.py
│   ├── simulated_annealing.py
│   ├── Asearch.py
│   └── __init__.py
├── utils.py
├── __init__.py
├── tests/
│   └── test_random_search.py
├── example_usage.py
├── setup.py
└── README.md

# tsp_solver_Tasnim

A simple and modular Python library that implements multiple algorithms to solve the **Traveling Salesman Problem (TSP)** — including:

- 🔁 Random Search
- 🧗 Hill Climbing
- 🔥 Simulated Annealing
- 🌟 A* Search (heuristic-based)

---

## 📦 Installation

You can install this package directly from **PyPI**:

```bash
pip install tsp_solver_Tasnim


## Or install it from source (local clone):

git clone https://github.com/mastas09/tsp_solver_Tasnim.git
cd tsp_solver_Tasnim
pip install .

## 📚 Example Usage

from tsp_solver_Tasnim import random_search, hill_climbing, simulated_annealing

cities = [(0, 0), (1, 1), (2, 2), (3, 3)]

print("Random Search:", random_search(cities, iterations=1000))
print("Hill Climbing:", hill_climbing(cities))
print("Simulated Annealing:", simulated_annealing(cities, temp=1000, cooling_rate=0.995))


## 🧪 Running Unit Tests
pip install pytest
pytest tsp_solver_Tasnim/tests/




