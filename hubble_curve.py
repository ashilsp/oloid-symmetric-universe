import numpy as np
import matplotlib.pyplot as plt

def calculate_hubble_gradient(x):
    """
    Translates the S2 OCM expansion metric equation into Python.
    Transitioning H0 from laminar baseline (67.4) to turbulent local (73.0).
    """
    H_laminar = 67.4
    H_turbulent = 73.0
    inflection_point = 5.0
    
    H_r = H_laminar + (H_turbulent - H_laminar) / (1 + np.exp(-1 * (x - inflection_point)))
    return H_r

# Generate data points mirroring the supplementary Figure
cosmic_time = np.linspace(0, 10, 100)
h_values = calculate_hubble_gradient(cosmic_time)

print("OCM Hubble Gradient Engine Initialized Successfully.")
print(f"Early Universe Boundary H(0): {h_values[0]:.2f}")
print(f"Late Universe Boundary H(10): {h_values[-1]:.2f}")
