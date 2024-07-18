import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Sample data for teleportation adventures
locations = {
    'Equinox': [(0, 0), (2, 3), (4, 5), (6, 7), (8, 9)],
    'Solstice': [(0, 0), (-1, 2), (-3, 4), (-5, 6), (-7, 8)]
}

# Function to plot teleportation locations
def plot_teleportation_locations(dog_name):
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(*zip(*locations[dog_name]), marker='o', linestyle='-')
    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    ax.set_title(f'Teleportation Adventures of {dog_name}')
    st.pyplot(fig)

# Streamlit app
def main():
    st.title('Teleportation Adventures of Equinox & Solstice')
    st.sidebar.title('Select Dog')

    dog_name = st.sidebar.radio('Dog Name', ('Equinox', 'Solstice'))

    st.write(f"You selected: {dog_name}")

    st.subheader(f'Teleportation Locations of {dog_name}')
    plot_teleportation_locations(dog_name)

if __name__ == '__main__':
    main()

