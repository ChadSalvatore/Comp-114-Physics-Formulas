import streamlit as st
import math

# --- Formula Functions ---
def calc_speed(distance, time):
    return distance / time

def calc_force(mass, acceleration):
    return mass * acceleration

def calc_kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2

def calc_potential_energy(mass, height):
    return mass * 9.8 * height

# --- Streamlit app UI ---
st.set_page_config(page_title="Formula Calculator")

st.title("Formula Calculator")
st.write("Select a category and a formula to use.")

# Only Physics category now
category = "Physics"

st.subheader("Physics Formulas")
formula = st.selectbox("Select a formula:",
                       ("Speed (distance / time)",
                        "Force (mass × acceleration)",
                        "Kinetic Energy (½ m v²)",
                        "Potential Energy (m g h)"))

if formula == "Speed (distance / time)":
    distance = st.number_input("Distance (m)", min_value=0.0, format="%.2f")
    time = st.number_input("Time (s)", min_value=0.0, format="%.2f")
    if st.button("Calculate Speed"):
        if time > 0:
            result = calc_speed(distance, time)
            st.success(f"Result = {result:.2f} m/s")
        else:
            st.error("Time must be greater than zero.")

elif formula == "Force (mass × acceleration)":
    mass = st.number_input("Mass (kg)", min_value=0.0, format="%.2f")
    acceleration = st.number_input("Acceleration (m/s²)", format="%.2f")
    if st.button("Calculate Force"):
        result = calc_force(mass, acceleration)
        st.success(f"Result = {result:.2f} N")

elif formula == "Kinetic Energy (½ m v²)":
    mass = st.number_input("Mass (kg)", min_value=0.0, format="%.2f")
    velocity = st.number_input("Velocity (m/s)", format="%.2f")
    if st.button("Calculate Kinetic Energy"):
        result = calc_kinetic_energy(mass, velocity)
        st.success(f"Result = {result:.2f} J")

elif formula == "Potential Energy (m g h)":
    mass = st.number_input("Mass (kg)", min_value=0.0, format="%.2f")
    height = st.number_input("Height (m)", format="%.2f")
    if st.button("Calculate Potential Energy"):
        result = calc_potential_energy(mass, height)
        st.success(f"Result = {result:.2f} J")

# Footer / credits
st.markdown("---")
st.markdown("*Reden and Nisar, at BSEE 2B*")
