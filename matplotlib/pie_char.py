import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("tmdb_movies_data.csv")

# Calculate the top 5 genres by total revenue
top_genres = df.groupby('genres')['revenue'].sum().sort_values(ascending=False).head(5)

# Plot a pie chart of the top 5 genres by revenue
plt.figure(figsize=(8, 8))  # Set the figure size
plt.pie(
    top_genres.values,
    labels=top_genres.index,
    explode=[0.1, 0, 0, 0, 0],  # Explode the first slice for emphasis
    autopct='%1.2f%%',  # Show percentages with two decimal places
    startangle=140,  # Start the pie chart at an angle for better visualization
    colors=plt.cm.Paired(np.arange(len(top_genres)))  # Use a colormap for colors
)
plt.title('Top 5 Genres by Revenue', fontsize=16)
plt.show()
