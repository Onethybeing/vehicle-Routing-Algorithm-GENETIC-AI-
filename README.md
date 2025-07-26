# 🛣️ Solving a global logistics problem :- Vehicle Routing Algorithm (GA-Based)

This Jupyter Notebook implements a **Vehicle Routing Problem (VRP)** solver using a **Genetic Algorithm (GA)**. The aim is to assign a set of delivery locations to a fixed number of vehicles while minimizing total distance and balancing the load between vehicles.

---

## 📦 Features

* Random generation of customer locations
* Central depot (starting point) for all vehicles
* Multiple vehicles supported
* Genetic Algorithm using [DEAP](https://github.com/DEAP/deap) framework
* Fitness function optimizes for:

  * Total route distance (minimized)
  * Balance of load between vehicles

---

## 📁 File Contents

* **Random Location Generation**: Generates a set of random delivery points.
* **Chromosome Representation**: Each chromosome encodes a complete solution (routes for all vehicles).
* **Fitness Function**: Considers total distance and balance between vehicle loads.
* **Genetic Operators**:

  * Selection: Tournament Selection
  * Crossover: Ordered Crossover (OX)
  * Mutation: Swap mutation between locations
* **Visualization**: Uses `matplotlib` to visualize the routes for each vehicle.

---

## ⚙️ Requirements

Install dependencies before running:

```bash
pip install matplotlib deap
```

---

## 🚀 How to Run

1. Open the notebook: `vehicle_Routing_Algorithm.ipynb`
2. Run each cell sequentially.
3. The GA will evolve solutions, and you'll see route visualizations for best individuals in selected generations.

---

## 🧠 Parameters to Tune

* `num_vehicles`: Number of delivery vehicles
* `num_locations`: Number of delivery points
* `population size`, `generations`, `cxpb`, `mutpb`: GA hyperparameters in the `run_ga` function

---

## 📊 Output

The notebook prints and plots the progress of the best route over generations, showing how the solution improves.

---

## ✍️ Author

Designed as an educational implementation of vehicle routing using evolutionary computation.
