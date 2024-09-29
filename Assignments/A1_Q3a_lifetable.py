#For adding latex first run this otherwise the codes given below won't work
!apt-get install -y texlive texlive-latex-extra texlive-fonts-recommended dvipng cm-super
# Question 3(a). Suppose we have a hypothetical insect
# population with a cohort lifetable that looks as
# on the right. Over time, a population of this
# insect will be increasing or decreasing in
# numbers?
import numpy as np
import matplotlib.pyplot as plt

# Define the fixed 2x2 transition matrix
transition_matrix = np.zeros((12, 12))
transition_matrix[0, 3] = 0.551
transition_matrix[0, 4] = 0.412
transition_matrix[0, 5] = 0.251
transition_matrix[0, 6] = 0.99
transition_matrix[0, 7] = 0.95
transition_matrix[0, 8] = 0.71
transition_matrix[0, 9] = 0.49
transition_matrix[0, 10] = 0.135
transition_matrix[1, 0] = 239/250
transition_matrix[2, 1] = 210/239
transition_matrix[3, 2] = 156/210
transition_matrix[4, 3] = 129/156
transition_matrix[5, 4] = 109/129
transition_matrix[6, 5] = 76/109
transition_matrix[7, 6] = 43/76
transition_matrix[8, 7] = 32/43
transition_matrix[9, 8] = 19/32
transition_matrix[10, 9] = 9/19


# Initial population (2x1 matrix) with juveniles = 100 and adults = 0
population = np.array([[250],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0],[0]])


# Lists to store juvenile and adult populations over generations
total_population = []
ratio_total = []
ratio_juvenile = []
ratio_adult = []
iteration = 0
# Number of generations (iterations)
num_generations = 100

# Loop through each generation
for generation in range(num_generations):

    total_population.append(population[0, 0] + population[1, 0] + population[2, 0] + population[3, 0] + population[4, 0] + population[5, 0] + population[6, 0] + population[7, 0] + population[8, 0] + population[9, 0])


    # Multiply the population by the transition matrix
    population = np.dot(transition_matrix, population)

# Plot the results
plt.figure(figsize=(16, 9))

plt.plot(range(num_generations), total_population, label='Total Population')
plt.xlabel('Generation')
plt.ylabel('Population')

plt.legend()
plt.grid(True)
plt.show()

print(f"Population Size: {total_population}")
