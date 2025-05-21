import numpy as np
import matplotlib.pyplot as plt

R = 1
C = 1
RC = R * C 
w = np.logspace(-1, 2, 500) 
s = 1j * w 
alpha = s * RC

# Transfer functions
H_ideal = 1 / (1 + alpha)**2
H_real = 1 / (1 + 3*alpha + alpha**2)

# Relative gain error
relative_error = np.abs((H_real - H_ideal) / H_real)
triangle_bound = np.abs((H_real + H_ideal) / H_real)


max_relative_error = np.max(relative_error)
max_triangle_bound = np.max(triangle_bound)

print(f"Maximum Relative Gain Error: {max_relative_error:.6f}")
print(f"Maximum Triangle Inequality Bound: {max_triangle_bound:.6f}")

# Find the index of the max relative gain error
max_index = np.argmax(relative_error)

# Get the corresponding frequency and s value
max_freq = w[max_index]         # in rad/s
max_s = s[max_index]            # complex frequency s = jω

print(f"Occurs at frequency ω = {max_freq:.6f} rad/s")
print(f"Corresponding s = {max_s}")

# Plot both
plt.figure(figsize=(8, 5))
plt.semilogx(w, relative_error, label="Relative Gain Error")
plt.semilogx(w, triangle_bound, '--', label="Triangle Inequality Bound")
plt.xlabel("Frequency (rad/s)")
plt.ylabel("Magnitude")
plt.title("Relative Gain Error and Triangle Inequality Bound")
plt.grid(True)
plt.legend()
plt.show()