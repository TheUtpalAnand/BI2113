#For adding latex first run this otherwise the codes given below won't work
#!apt-get install -y texlive texlive-latex-extra texlive-fonts-recommended dvipng cm-super


import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from scipy.integrate import solve_ivp
from IPython.display import HTML

# Constants for the system
r1 = 1.05
C = 0.1
d2 = 0.6
g = 0.45

# Define the system of equations for Lotka-Volterra
def lotka_volterra(t, z):
    N, P = z
    dNdt = r1 * N - C * N * P
    dPdt = -d2 * P + g * C * N * P
    return [dNdt, dPdt]

# Initial conditions
initial_conditions = [30, 10]  # Starting population sizes for N (Sangai Deer) and P (Cheetahs)

# Time span and evaluation points
t_span = [0, 50]
t_eval = np.linspace(0, 50, 500)

# Solve the system of equations
sol = solve_ivp(lotka_volterra, t_span, initial_conditions, t_eval=t_eval)

# Extract solutions
N_pop = sol.y[0]  # Prey population (Sangai Deer)
P_pop = sol.y[1]  # Predator population (Cheetah)
time = sol.t

# Set up the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 50)
ax.set_ylim(0, 35)
line1, = ax.plot([], [], lw=2, color='blue', label="Sangai Deer (N)")  # Line for Sangai
line2, = ax.plot([], [], lw=2, color='red', label="Cheetah (P)")       # Line for Cheetah
ax.set_xlabel('Time (Years)')
ax.set_ylabel('Population')
ax.set_title('Predator-Prey Population Over Time')
ax.legend()

# Adding labels for N (prey) and P (predator) populations
prey_label = ax.text(0.8, 0.9, '', transform=ax.transAxes, color='blue')
pred_label = ax.text(0.8, 0.85, '', transform=ax.transAxes, color='red')

# Function to initialize the plot
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    prey_label.set_text('')
    pred_label.set_text('')
    return line1, line2, prey_label, pred_label

# Function to animate the plot
def animate(i):
    x = time[:i]
    y1 = N_pop[:i]  # Prey population (Sangai Deer)
    y2 = P_pop[:i]  # Predator population (Cheetah)
    line1.set_data(x, y1)
    line2.set_data(x, y2)
    prey_label.set_text(f'Sangai (N): {N_pop[i]:.1f}')
    pred_label.set_text(f'Cheetah (P): {P_pop[i]:.1f}')
    return line1, line2, prey_label, pred_label

# Create the animation
ani = animation.FuncAnimation(fig, animate, init_func=init, frames=len(time), interval=20, blit=True)

# Display the animation
HTML(ani.to_jshtml())
