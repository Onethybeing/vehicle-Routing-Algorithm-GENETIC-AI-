import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from vehicle_Routing_Algorithm import run_genetic_vrp

st.set_page_config(page_title="VRP Genetic Algorithm", layout="wide")

st.title("🚚 Vehicle Routing Problem - Genetic Algorithm Visualizer")

# Sidebar inputs
st.sidebar.header("GA Parameters")
n_locations = st.sidebar.slider("Number of Locations", 5, 50, 10)
n_vehicles = st.sidebar.slider("Number of Vehicles", 1, 10, 3)
pop_size = st.sidebar.number_input("Population Size", min_value=10, max_value=1000, value=300, step=10)
mutation_rate = st.sidebar.slider("Mutation Rate", 0.0, 1.0, 0.2, 0.01)
ngen = st.sidebar.number_input("Number of Generations", min_value=10, max_value=1000, value=300, step=10)
seed = st.sidebar.number_input("Random Seed", min_value=0, max_value=9999, value=42)

if st.sidebar.button("Run Algorithm"):
    with st.spinner("Running Genetic Algorithm..."):
        best_route, fitness_history, locations, depot = run_genetic_vrp(
            n_locations=n_locations,
            n_vehicles=n_vehicles,
            pop_size=pop_size,
            mutation_rate=mutation_rate,
            ngen=ngen,
            seed=seed
        )

    # --- Plot routes ---
    fig, ax = plt.subplots()
    ax.set_title("Optimal Vehicle Routes")
    ax.set_xlabel("X Coordinate")
    ax.set_ylabel("Y Coordinate")

    # Plot locations and depot
    for (x, y) in locations:
        ax.plot(x, y, 'bo')
    ax.plot(depot[0], depot[1], 'rs', markersize=10, label="Depot")

    # Plot each vehicle's route
    for i in range(n_vehicles):
        vehicle_route = [depot] + [locations[best_route[j]] for j in range(i, len(best_route), n_vehicles)] + [depot]
        xs, ys = zip(*vehicle_route)
        ax.plot(xs, ys, marker='o', label=f"Vehicle {i+1}")

    ax.legend()
    st.pyplot(fig)

    # --- Fitness chart ---
    st.subheader("Best Fitness Over Generations")
    df = pd.DataFrame({"Generation": range(1, len(fitness_history) + 1), "Best Distance": fitness_history})
    st.line_chart(df.set_index("Generation"))

    st.success("Algorithm completed!")
