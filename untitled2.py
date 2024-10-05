import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

# SHM displacement function for follower based on cam angle
def shm_displacement(A, omega, theta, phi=0):
    return A * np.sin(omega * theta + phi)

# Streamlit App
st.title("Real-Time Cam and Follower Animation - Simple Harmonic Motion")
st.write("This app simulates the real-time rotation of a cam and the vertical displacement of a follower using Simple Harmonic Motion.")

# Sidebar for user inputs
st.sidebar.header("SHM Parameters")
amplitude = st.sidebar.slider("Amplitude (A)", 0.1, 10.0, 5.0)
omega = st.sidebar.slider("Angular Velocity (ω)", 0.1, 10.0, 2.0)
phase = st.sidebar.slider("Phase (ϕ)", 0.0, 2 * np.pi, 0.0)
rotation_speed = st.sidebar.slider("Rotation Speed (milliseconds per frame)", 10, 200, 50)

# Set up the cam parameters
num_points = 100
theta = np.linspace(0, 2 * np.pi, num_points)  # Angular positions
cam_radius = 3  # Radius of the cam

# Create placeholders for the cam and follower animation
cam_placeholder = st.empty()

# Infinite loop for continuous animation
while True:
    for i in range(num_points):
        # Current angle for rotation
        current_angle = theta[i]

        # Calculate follower displacement using SHM
        follower_y = shm_displacement(amplitude, omega, current_angle, phase)

        # Create the plot for cam and follower
        fig, ax = plt.subplots()

        # Plot the cam (circle) and the rotating point
        cam_circle = plt.Circle((0, 0), cam_radius, color='b', fill=False, label='Cam')
        ax.add_patch(cam_circle)

        # Plot the current position on the cam (rotating point)
        cam_x = cam_radius * np.cos(current_angle)
        cam_y = cam_radius * np.sin(current_angle)
        ax.plot([0, cam_x], [0, cam_y], 'r-', lw=2, label="Cam Arm")
        ax.plot(cam_x, cam_y, 'ro')  # Cam position

        # Plot the follower (vertical motion)
        ax.plot([cam_x, cam_x], [cam_y, cam_y + follower_y], 'g-', lw=3, label="Follower")
        ax.plot(cam_x, cam_y + follower_y, 'go', label="Follower Position")

        # Adjust plot limits and labels
        ax.set_xlim(-cam_radius * 1.5, cam_radius * 1.5)
        ax.set_ylim(-cam_radius * 1.5, cam_radius * 1.5)
        ax.set_aspect('equal')
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_title("Real-Time Cam and Follower Animation")
        ax.grid(True)

        # Display legend
        ax.legend()

        # Update the plot in real time
        cam_placeholder.pyplot(fig)

        # Pause for the specified rotation speed
        time.sleep(rotation_speed / 1000.0)  

