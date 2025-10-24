# Import required libraries
import matplotlib.pyplot as plt
import numpy as np

# Read data from csv file
movies_data = np.loadtxt('data.csv', delimiter=',')

# Create empty lists to store good and bad movies' x and y values
good_movies_x = []
good_movies_y = []

bad_movies_x = []
bad_movies_y = []

# Loop through the movies data
for movie in movies_data:
    # If the movie is labeled as good, add its x and y values to the respective lists
    if movie[2] == 1:
        good_movies_x.append(movie[0])
        good_movies_y.append(movie[1])
    # If the movie is labeled as bad, add its x and y values to the respective lists
    else:
        bad_movies_x.append(movie[0])
        bad_movies_y.append(movie[1])

# Plot the values using Matplotlib
plt.scatter(good_movies_x, good_movies_y, label='Good movies', marker='x')
plt.scatter(bad_movies_x, bad_movies_y, label='Bad movies', marker='o')

# Add labels to the axes
plt.xlabel('Acting')
plt.ylabel('Direction')


