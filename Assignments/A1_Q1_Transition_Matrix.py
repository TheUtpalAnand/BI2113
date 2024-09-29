#For adding latex first run this
#!apt-get install -y texlive texlive-latex-extra texlive-fonts-recommended dvipng cm-super


#Question 1 Q1. For the population described by the transition matrix given below ([0.4,3],[0.32,0.7])
# a) What is the ratio of the total population sizes (i.e. sum of both stage classes in a generation) in
# two successive generations at equilibrium?
# b) At equilibrium what is the fraction of the juveniles in any given generation? This refers to the ratio
# of juveniles to the total population size.
import numpy as np
import matplotlib.pyplot as plt

# Define the fixed 2x2 transition matrix
transition_matrix = np.array([[0.4, 3.0],
                              [0.32, 0.7]])

# Initial population (2x1 matrix) with juveniles = 100 and adults = 0
population = np.array([[100],
                       [100]])

# Lists to store juvenile and adult populations over generations
juvenile_population = []
adult_population = []
total_population = []
ratio_total = []
ratio_juvenile = []
ratio_adult = []
iteration = 0
# Number of generations (iterations)
num_generations = 100


# Loop through each generation
for generation in range(num_generations):
    # Append the current population of juveniles and adults to respective lists
    juvenile_population.append(population[0, 0])
    adult_population.append(population[1, 0])
    total_population.append(population[0, 0] + population[1, 0])
    if iteration > 0:
      ratio_total.append((population[0, 0] + population[1, 0])/total_population[iteration-1])
      ratio_juvenile.append(100*juvenile_population[iteration-1]/total_population[iteration-1])
      ratio_adult.append(100*adult_population[iteration-1]/total_population[iteration-1])
    iteration += 1
    # Print the current population
    #print(f"Generation {generation + 1}: Juveniles = {population[0, 0]}, Adults = {population[1, 0]}")
    # Multiply the population by the transition matrix
    population = np.dot(transition_matrix, population)

# Plot the results
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# First subplot: Juvenile, Adult, and Total Population over Generations
axs[0].plot(range(num_generations), juvenile_population, label='Juveniles')
axs[0].plot(range(num_generations), adult_population, label='Adults')
axs[0].plot(range(num_generations), total_population, label='Total Population')
axs[0].set_xlabel('Generation')
axs[0].set_ylabel('Population')
axs[0].set_title('Juvenile and Adult Population Over Generations')
axs[0].legend()  # To show the legend
axs[0].grid(True)

# Second subplot: Eigenvalue Ratio Over Generations
axs[1].plot(range(num_generations - 1), ratio_total, label='EigenValues')
axs[1].set_xlabel('Generation')
axs[1].set_ylabel('Eigenvalue')
axs[1].set_title('Ratio of Total Population Over Generations')
axs[1].legend()  # To show the legend
axs[1].grid(True)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plots
plt.show()


print(ratio_total)
print(f"Percentage of Juvenile: {ratio_juvenile}")
print(f"Percenatge of adults: {ratio_adult}")

