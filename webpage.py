import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Function to calculate SHM displacement
def shm_displacement(theta, h, beta):
    return (h / 2) * (1 - np.cos(np.pi * theta / beta))

# Streamlit app
def main():
    st.title("Cam Profile Simulation: Simple Harmonic Motion")

    # User input parameters
    h = st.sidebar.slider("Maximum Displacement (Lift) [mm]", 1.0, 100.0, 50.0)
    beta = st.sidebar.slider("Rise Angle (Beta) [degrees]", 1, 360, 180)

    # Cam angles (from 0 to 360 degrees)
    theta = np.linspace(0, 360, 500)

    # Calculate SHM displacement
    displacement = np.piecewise(theta, [theta <= beta, theta > beta], 
                                [lambda t: shm_displacement(t, h, beta), 0])

    # Plot Displacement Diagram
    fig, ax = plt.subplots()
    ax.plot(theta, displacement, label='Displacement', color='blue')
    ax.set_title("Displacement Diagram (Simple Harmonic Motion)")
    ax.set_xlabel("Cam Angle (degrees)")
    ax.set_ylabel("Displacement (mm)")
    ax.grid(True)
    ax.legend()

    # Display the plot in Streamlit
    st.pyplot(fig)

if __name__ == "__main__":
    main()
