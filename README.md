# 🛣️ Solving a global logistics problem :- Vehicle Routing Algorithm (GA-Based)

This Jupyter Notebook implements a **Vehicle Routing Problem (VRP)** solver using a **Genetic Algorithm (GA)**. The aim is to assign a set of delivery locations to a fixed number of vehicles while minimizing total distance and balancing the load between vehicles.

---
# 🚚 Vehicle Routing Problem - Genetic Algorithm

This project implements a **Vehicle Routing Problem (VRP)** solver using a Genetic Algorithm, with an interactive **Streamlit** web app for visualization.


https://github.com/user-attachments/assets/dff0f33d-9ab0-4a66-8a4a-8e7c0e8d7cf1


## 🌐 Live Demo
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://jw8q2tyhrrjzf35avb6eck.streamlit.app/)

Click the badge above to launch the app in your browser — no installation required.

---

## 📸 Preview
<!-- Replace with your own screenshot -->
![App Screenshot](screenshot.png)

---

## ✨ Features
- **Customizable Parameters**:
  - Number of vehicles
  - Number of locations
  - Population size
  - Mutation rate
  - Number of generations
- **Real-time Visualization**:
  - Plots optimal vehicle routes on a 2D map
  - Shows best fitness score over generations
- **Genetic Algorithm Engine**:
  - Built using [DEAP](https://deap.readthedocs.io/en/master/) evolutionary computation framework

---

## ⚙ How It Works
1. Generates random coordinates for delivery locations.
2. Uses a Genetic Algorithm to find the optimal set of routes for the given number of vehicles.
3. Evaluates routes by:
   - Total travel distance
   - Balance of distance between vehicles
4. Visualizes:
   - The optimal route per vehicle
   - Convergence of fitness score over time

---

## 🛠 Run Locally
Clone the repository and install dependencies:
```bash
git clone https://github.com/YourUsername/vehicle-Routing-Algorithm-GENETIC-AI-.git
cd vehicle-Routing-Algorithm-GENETIC-AI-
pip install -r requirements.txt


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
