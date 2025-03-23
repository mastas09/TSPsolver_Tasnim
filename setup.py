from setuptools import setup, find_packages

setup(
    name='tsp_solver_Tasnim',  # ✅ PyPI-safe unique name
    version='0.1.0',
    packages=find_packages(),  # ✅ This auto-finds your package and sub-packages
    description='TSP Solver with multiple algorithms (Random Search, Hill Climbing, Simulated Annealing, A*).',
    author='Masrura Tasnim',
    author_email='masrura.niti@gmail.com',
    url='https://github.com/mastas09/tsp_solver_Tasnim',  # ✅ Your actual repo link
    license='MIT',
    install_requires=[],
    python_requires='>=3.6',
)
