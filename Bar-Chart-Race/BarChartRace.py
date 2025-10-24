import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import imageio


# Load the dataset from the CSV file
df = pd.read_csv('country_population.csv')
colors = {'Bangladesh': 'skyblue', 'Brazil': 'pink', 'China': 'orange', 'India': 'blue',
          'Indonesia': 'purple', 'Nigeria': 'brown', 'Pakistan': 'Green', 'Russia': 'gray',
          'United States': 'red'}
fig, ax = plt.subplots(figsize=(10, 6))
def population_to_millions(population):
    return population / 1000000  # Assuming population is in units of individuals

def create_frame(df, frame, colors):
    ax.clear()
    year = df.iloc[frame]['Year']  # Get the year for the current frame
    data = df.iloc[frame].drop('Year')  # Exclude the 'Year' column
    data_sorted = data.sort_values(ascending=True)  # Sort data in ascending order of population, excluding China

    normalized_data = population_to_millions(data_sorted)
    countries = normalized_data.index  # Get the countries
    populations = normalized_data.values  # Get the normalized population values
    
    # Create the horizontal bar chart
    ax.barh(countries, populations, color=[colors[country] for country in countries])
    
    # Set title and labels
    ax.set_title(f'Population by Country ({year})')
    ax.set_xlabel('Population')
    ax.set_ylabel('Country')
    
    # Adjust the x-axis limit to start from 50 million
    ax.set_xlim(50, populations[-1] + 30)
         
    # Create a frame from the plot
    plt.tight_layout()
    fig.canvas.draw()
    frame_data = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
    frame_data = frame_data.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    return frame_data

# Generate frames for the animation
frames = [create_frame(df, frame, colors) for frame in range(len(df))]

# Save the animation
imageio.mimsave('output/country_race.gif', frames, fps=4)











#another one below

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import imageio

# Load the dataset from the CSV file
df = pd.read_csv('programming_language_popularity.csv')
colors = {'Python': 'skyblue', 'Java': 'orange', 'JavaScript': 'green', 'C/C++': 'red', 'C#': 'purple',
          'PHP': 'brown', 'Ruby': 'pink', 'R': 'gray', 'Go': 'pink'}

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])
def create_frame(frame):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.clear()
    date = df.iloc[frame]['Date']  # Get the date for the current frame
    data = df.iloc[frame].drop('Date')  # Exclude the 'Date' column
    data_sorted = data.sort_values(ascending=True)  # Sort data in descending order of popularity
    most_popular_language = data_sorted.index[0]  # Get the most popular language
    remaining_languages = data_sorted.index[1:]  # Get the remaining languages
    languages = [most_popular_language] + list(remaining_languages)  # Combine languages with the most popular at the top
    popularity = data_sorted.values  # Get the sorted popularity values
   
    # Create the horizontal bar chart
    ax.barh(languages, popularity, color=[colors[lang] for lang in languages])
    
    # Set title and labels
    ax.set_title(f'Programming Language Popularity in {date.strftime("%B %Y")}')
    ax.set_xlabel('Popularity')
    ax.set_ylabel('Language')
   
    # Adjust the x-axis limit based on the maximum popularity
    ax.set_xlim(0, popularity[0] + 30)
    
    # Create a frame from the plot
    plt.tight_layout()
    fig.canvas.draw()
    frame_data = np.frombuffer(fig.canvas.tostring_rgb(), dtype=np.uint8)
    frame_data = frame_data.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    plt.close(fig)
    return frame_data

# Generate frames for the animation
frames = [create_frame(frame) for frame in range(len(df))]

# Save the animation
imageio.mimsave('output/language_race.gif', frames, fps=10)