import streamlit as st
import pandas as pd
import plotly.express as px
from vehicle_Routing_Algorithm import run_genetic_vrp  # adjust if needed

st.title("Vehicle Routing Genetic Algorithm Visualizer 🚚")

n_locations = st.sidebar.slider("Number of Locations", 5, 50, 20)
n_vehicles = st.sidebar.slider("Number of Vehicles", 1, 10, 3)
pop_size = st.sidebar.number_input("Population Size", 10, 500, 100)
mutation_rate = st.sidebar.slider("Mutation Rate", 0.0, 1.0, 0.1)

if st.sidebar.button("Run Algorithm"):
    best_routes, fitness_history = run_genetic_vrp(
        n_locations, n_vehicles, pop_size, mutation_rate
    )

    st.subheader("Fitness Over Generations")
    df = pd.DataFrame({"Generation": range(len(fitness_history)),
                       "Fitness": fitness_history})
    st.line_chart(df.set_index("Generation"))

    st.subheader("Final Route")
    fig = px.line(best_routes, x="x", y="y", title="Best Route")
    st.plotly_chart(fig)
