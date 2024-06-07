import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("tmdb_movies_data.csv")

# Count the number of movies released each year
movies_count = pd.DataFrame(df['release_year'].value_counts(ascending=True)).reset_index()
movies_count.columns = ['year', 'count']

# Sort the DataFrame by 'year'
movies_count = movies_count.sort_values(by=['year'])

# Plot the number of movies released each year
plt.figure(figsize=(12, 6))  # Set the figure size
plt.plot(movies_count['year'], movies_count['count'], color='0.2', marker='o')  # Plot with a line and markers
plt.xlabel('Year', fontsize=15)  # Label for the x-axis
plt.ylabel('Movie Count', fontsize=15)  # Label for the y-axis
plt.title('Number of Released Movies Annually', fontsize=18)  # Title of the plot
plt.xlim(1960, 2000)  # Limit the x-axis range
plt.xticks(range(1960, 2001, 5))  # Set x-axis ticks
plt.grid(True)  # Enable grid for better readability
plt.show()  # Display the plot
