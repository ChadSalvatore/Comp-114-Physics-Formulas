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


def calc_circle_area(radius):
    return math.pi * radius ** 2


def calc_circle_perimeter(radius):
    return 2 * math.pi * radius


def calc_rectangle_area(length, width):
    return length * width


def calc_triangle_area(base, height):
    return 0.5 * base * height


# --- Streamlit app UI ---
st.set_page_config(page_title="Formula Calculator")

st.title("Formula Calculator")
st.write("Select a category and a formula to use.")

category = st.radio("Choose category:", ("Physics", "Geometry"))

if category == "Physics":
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

else:  # Geometry
    st.subheader("Geometry Formulas")
    formula = st.selectbox("Select a formula:",
                           ("Area of Circle (πr²)",
                            "Perimeter of Circle (2πr)",
                            "Area of Rectangle (L×W)",
                            "Area of Triangle (½ b h)"))

    if formula == "Area of Circle (πr²)":
        radius = st.number_input("Radius (m)", min_value=0.0, format="%.2f")
        if st.button("Calculate Area of Circle"):
            result = calc_circle_area(radius)
            st.success(f"Result = {result:.2f} m²")

    elif formula == "Perimeter of Circle (2πr)":
        radius = st.number_input("Radius (m)", min_value=0.0, format="%.2f")
        if st.button("Calculate Perimeter of Circle"):
            result = calc_circle_perimeter(radius)
            st.success(f"Result = {result:.2f} m")

    elif formula == "Area of Rectangle (L×W)":
        length = st.number_input("Length (m)", min_value=0.0, format="%.2f")
        width = st.number_input("Width (m)", min_value=0.0, format="%.2f")
        if st.button("Calculate Area of Rectangle"):
            result = calc_rectangle_area(length, width)
            st.success(f"Result = {result:.2f} m²")

    elif formula == "Area of Triangle (½ b h)":
        base = st.number_input("Base (m)", min_value=0.0, format="%.2f")
        height = st.number_input("Height (m)", min_value=0.0, format="%.2f")
        if st.button("Calculate Area of Triangle"):
            result = calc_triangle_area(base, height)
            st.success(f"Result = {result:.2f} m²")

# Footer / credits
st.markdown("---")
st.markdown("*Reden and Nisar, at BSEE 2B*")
