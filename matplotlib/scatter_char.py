import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("tmdb_movies_data.csv")

# Create a scatter plot for vote average vs revenue
plt.figure(figsize=(10, 6))  # Set the figure size
plt.scatter(df['vote_average'], df['revenue'], alpha=0.8, marker='*', label='Vote Average')
plt.scatter(df['vote_count'], df['revenue'], alpha=0.7, marker='+', label='Vote Count')

# Add legend to differentiate the scatter points
plt.legend(loc='upper right')

# Label the axes
plt.xlabel('Vote Average', fontsize=14)
plt.ylabel('Revenue', fontsize=14)

# Set the title of the plot
plt.title('Relationship Between Vote Average and Revenue', fontsize=16)

# Display the plot
plt.show()
