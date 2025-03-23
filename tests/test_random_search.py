import unittest
from tsp_solver.algorithms.random_search import solve_tsp

def test_random_search():
    cities = [(0, 0), (1, 1), (2, 2)]
    route, distance = solve_tsp(cities, iterations=100)
    assert len(route) == len(cities)
    assert distance > 0
