#For adding latex first run this otherwise the codes given below won't work
#!apt-get install -y texlive texlive-latex-extra texlive-fonts-recommended dvipng cm-super



# Q4. The government is planning to reintroduce 10 Namibian cheetahs to Madhya Pradesh's Gandhi
# Sagar Wildlife Sanctuary in January 2025. At the same time, they plan to introduce 30 Sangai deers
# from Manipur into the sanctuary as prey. No further introduction of either prey or the predator is
# planned. The government has decided to celebrate the introduction after a few years through a
# major celebration in the park inviting many world leaders. Park authorities have determined that the
# optimal viewing densities for the dignitaries would be 15 cheetahs and 18 sangais in the park. They
#have also determined that the cheetah-sangai system can be modelled as a Lotka-Volterra prey-
# predator system
# \frac{dN}{dt} = r_1N - CNP \\
#\frac{dP}{dt} = -d_2P + gCNP
# where N and P denote the prey and the predator population respectively, and the other constants
# have their usual meaning as per the Lotka-Volterra prey-predator model. As per data from the
# scientists, the yearly rates are r1= 1.05, C = 0.1, d2=0.6 and g = 0.45. Based on this information, in
# which year will the celebratory event happen for the first time? Assume that all the assumptions of
# the Lotka-Volterra continuous prey-predator model are true for this system, and one needs to have
# both the cheetah’s and the sangai’s numbers to be simultaneously as per specifications.
import numpy as np
import matplotlib.pyplot as plt
from pylab import rcParams
from scipy.integrate import solve_ivp

# Enable LaTeX rendering in matplotlib
plt.rcParams['text.usetex'] = True

# Set figure size
rcParams['figure.figsize'] = 15, 10

# Define the grid size for x and y axes
grid_size = 33
x = np.linspace(1, 59, grid_size)  # Reduced number of points for visualization
y = np.linspace(1, 35, grid_size)

# Constants for the system
r1, C, d2, g = (1.05, 0.1, 0.6, 0.45)

# Create a meshgrid for the quiver plot
xv, yv = np.meshgrid(x, y)

# Compute the vector field components using the meshgrid
x1 = r1 * xv - C * xv * yv
y1 = -d2 * yv + g * C * xv * yv

# Normalize the vectors for better visibility
magnitude = np.sqrt(x1**2 + y1**2)
magnitude[magnitude == 0] = 1  # To avoid division by zero
x1_normalized = x1/magnitude
y1_normalized = y1/magnitude

# Create the figure and axes
fig, ax1 = plt.subplots()

# Plot the nullclines
N_nullcline = np.linspace(5, 30, grid_size)
P_nullcline = r1 / C #- N_nullcline
P_nullcline_dP = d2 / (g * C)

# Use raw strings (r'') and remove newlines to prevent issues with LaTeX code
ax1.axhline( P_nullcline, color='blue', linestyle='--', label=r'$\frac{dN}{dt} = 0$') # Removed newline and escaped $
ax1.axvline(P_nullcline_dP, color='green', linestyle='--', label=r'$\frac{dP}{dt} = 0$') # Removed newline and escaped $

# Add quiver plot (vector field) with normalized vectors
ax1.quiver(xv, yv, x1_normalized, y1_normalized, scale=50, color='darkcyan')

# Set axis limits and labels
ax1.set_xlim([0, 32])
ax1.set_ylim([0, 22])
ax1.set_xlabel(r'$N$ (Sangai Deer)')
ax1.set_ylabel(r'$P$ (Cheetah)')

# Define the system of equations for Lotka-Volterra
def lotka_volterra(t, z):
    N, P = z
    dNdt = r1 * N - C * N * P
    dPdt = -d2 * P + g * C * N * P
    return [dNdt, dPdt]

# Initial conditions for the trajectory (Corrected: 30 prey and 10 predator)
initial_conditions = [30.0, 10.0]  # 30 Sangai deer (prey), 10 Cheetahs (predators)

# Time span for the simulation
t_span = [0, 50]  # From time 0 to 50
t_eval = np.linspace(0, 50, 50000)  # Points at which to evaluate the solution

# Solve the system of equations
sol = solve_ivp(lotka_volterra, t_span, initial_conditions, t_eval=t_eval, method='DOP853')

# Plot the trajectory
ax1.plot(sol.y[0], sol.y[1], color='gold', label='Trajectory')

# Add title and legend
ax1.set_title(r'Lotka-Volterra ($r_1 = 1.05, C = 0.1, d_2 = 0.6, g = 0.45$)')
ax1.legend()

# Plot the target point (18 Sangai deer and 15 Cheetahs)
plt.plot(18, 15, 'r*', label="Target: 18 Sangai, 15 Cheetahs")
plt.plot(30, 10, 'r+', markersize= 10, label="Initial Point: 30 Sangai, 10 Cheetahs")

# Show legend and grid
plt.legend(loc='upper right', edgecolor="black", framealpha=1)
plt.grid(True)

# Show the plot
plt.show()
