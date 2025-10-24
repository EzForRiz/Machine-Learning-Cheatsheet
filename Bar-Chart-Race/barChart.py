import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset from the CSV file
df = pd.read_csv('programming_language_popularity.csv')

date = df['Date'].iloc[0]  # Get the date for January 2011
data = df.drop(columns=['Date']).iloc[0]  # Exclude the 'Date' column and get the data for January 2011
data_sorted = data.sort_values(ascending=True)  # Sort data in descending order of popularity
languages = data_sorted.index.tolist()  # Get the languages
popularity = data_sorted.values  # Get the popularity values

colors = {'Python': 'blue', 'Java': 'orange', 'JavaScript': 'yellow', 'C/C++': 'red', 'C#': 'purple',
          'PHP': 'brown', 'Ruby': 'pink', 'R': 'gray', 'Go': 'pink'}
plt.figure(figsize=(10, 6))

# Create the horizontal bar chart
plt.barh(languages, popularity, color=[colors[lang] for lang in languages])

# Set title and labels
plt.title('Programming Language Popularity in January 2011')
plt.xlabel('Popularity')
plt.ylabel('Language')
plt.tight_layout()
plt.show()