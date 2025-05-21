import numpy as np
import matplotlib.pyplot as plt

# Frequency range
w = np.logspace(-1, 2, 500)
s = 1j * w
RC = 1
alpha = s * RC

# --- Goal 1: Plot for a fixed k ---
k = 1  # You can vary this

# Transfer functions for real and ideal
H_real = 1 / (1 + (3 + k)*alpha + k*alpha**2)
H_ideal = (1 / (1 + alpha))*(1/(1 + k*alpha))
# Relative error and triangle bound
relative_error = np.abs((H_real - H_ideal) / H_real)
triangle_bound = np.abs((H_real + H_ideal) / H_real)

# Plot gain error vs frequency
plt.figure(figsize=(8, 5))
plt.semilogx(w, relative_error, label="Relative Gain Error")
plt.semilogx(w, triangle_bound, '--', label="Triangle Inequality Bound")
plt.xlabel("Frequency (rad/s)")
plt.ylabel("Magnitude")
plt.title(f"Gain Error vs Frequency for k = {k}")
plt.grid(True)
plt.legend()
plt.show()

# --- Goal 2: Sweep k values to find min error under 1% ---
k_values = np.linspace(0.1, 1000, 5000)
max_errors = []

for k_val in k_values:
    H_real = 1 / (1 + (3 + k_val)*alpha + k_val*alpha**2)
    H_ideal = 1 / ((1 + alpha) * (1 + k_val*alpha))
    rel_err = np.abs((H_real - H_ideal) / H_real)
    max_errors.append(np.max(rel_err))

max_errors = np.array(max_errors)

# Find min k where max error ≤ 1%
threshold = 0.01
valid_indices = np.where(max_errors <= threshold)[0]

if valid_indices.size > 0:
    k_min = k_values[valid_indices[0]]
    print(f" Minimum k for ≤1% gain error: {k_min:.4f}")
else:
    print("No value of k found with max error ≤ 1%.")

# Plot max error vs k
plt.figure(figsize=(8, 5))
plt.plot(k_values, max_errors * 100)
plt.axhline(y=1, color='r', linestyle='--', label='1% Error Threshold')
plt.xlabel("k (R2 = k * R1)")
plt.ylabel("Max Relative Gain Error (%)")
plt.title("Max Gain Error vs. k")
plt.grid(True)
plt.legend()
plt.show()