#For adding latex first run this otherwise the codes given below won't work
!apt-get install -y texlive texlive-latex-extra texlive-fonts-recommended dvipng cm-super
# Question 2. Assume a Lotka-Volterra competition scenario with the following parameter values:
# Species 1: r1=1, K1=200, α12 = 0.8; Species 2: r2=0.5, K2=300, α21=2
# Given below are four starting points for the system. For each case, what will be the population sizes
# of Species 1 and Species 2 at equilibrium? For this your answer should consist of the filled table as
# well as the four isocline diagrams showing the trajectory of the system (not merely the vectors).
import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams
from scipy.integrate import solve_ivp

# Enable LaTeX rendering in matplotlib
plt.rcParams['text.usetex'] = True

# Set figure size
rcParams['figure.figsize'] = 10, 10

# Define the grid size for x and y axes
grid_size = 35
x = np.linspace(10, 225, grid_size)  # Reduced number of points for visualization
y = np.linspace(10, 300, grid_size)

# Constants for the system
k1, k2, a12, a21, r1, r2 = (200, 300, 0.8, 2, 1, 0.5)

# Create a meshgrid for the quiver plot
xv, yv = np.meshgrid(x, y)

# Compute the vector field components using the meshgrid
x1 = r1 * xv * (k1 - xv - (a12 * yv)) / k1
y1 = r2 * yv * (k2 - yv - (a21 * xv)) / k2

# Normalize the vectors for better visibility
magnitude = np.sqrt(x1**2 + y1**2)
magnitude[magnitude == 0] = 1  # To avoid division by zero
x1_normalized = x1 / magnitude
y1_normalized = y1 / magnitude

# Create the figure and axes
fig, ax1 = plt.subplots()

# Plot the nullclines
ax1.plot(k1 - (a12 * y), y, label=r'$\frac{dN_1}{dt} = 0$')
ax1.plot(x, k2 - (a21 * x), label=r'$\frac{dN_2}{dt} = 0$')

# Add quiver plot (vector field) with normalized vectors
ax1.quiver(xv, yv, x1_normalized, y1_normalized, scale=50)

# Set axis limits and labels
ax1.set_xlim([0, 235])
ax1.set_ylim([0, 310])
ax1.set_xlabel(r'$N_1 (K = 200)$')
ax1.set_ylabel(r'$N_2 (K = 300)$')
# Define the system of equations for Lotka-Volterra
def lotka_volterra(t, z):
    N1, N2 = z
    dN1dt = r1 * N1 * (k1 - N1 - a12 * N2) / k1
    dN2dt = r2 * N2 * (k2 - N2 - a21 * N1) / k2
    return [dN1dt, dN2dt]

# Initial conditions for the trajectory
initial_conditions1 = [70, 175]  # Starting population sizes for N1 and N2
initial_conditions2 = [70, 75]
initial_conditions3 = [30, 120]
initial_conditions4 = [30,100]

# Time span for the simulation
t_span = [0, 100]  # From time 0 to 100
t_eval = np.linspace(0, 100, 500)  # Points at which to evaluate the solution

# Solve the system of equations
sol = solve_ivp(lotka_volterra, t_span, initial_conditions1, t_eval=t_eval)
sol2 = solve_ivp(lotka_volterra, t_span, initial_conditions2, t_eval=t_eval)
sol3 = solve_ivp(lotka_volterra, t_span, initial_conditions3, t_eval=t_eval)
sol4 = solve_ivp(lotka_volterra, t_span, initial_conditions4, t_eval=t_eval)

# Plot the trajectory
ax1.plot(sol.y[0], sol.y[1], color='red', label='Trajectory 1')
ax1.plot(sol2.y[0], sol2.y[1], color='blue', label='Trajectory 2')
ax1.plot(sol3.y[0], sol3.y[1], color='green', label='Trajectory 3')
ax1.plot(sol4.y[0], sol4.y[1], color='black', label='Trajectory 4')

# Add title and legend
ax1.set_title(r'Lotka-Volterra ($a_{12} = 0.8, a_{21} = 2.0$)')
ax1.legend()

# Show the plot
plt.show()
