import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("tmdb_movies_data.csv")

# Group by 'original_title' and sum the 'revenue', then sort by 'revenue' in descending order
top_revenue = df.groupby('original_title').sum().sort_values(by="revenue", ascending=False)

# Get the top 5 movies based on revenue
top_5_movies = top_revenue.head()

# Extract movie titles and revenue values
movies = top_5_movies.index
revenue = top_5_movies['revenue'].values

# Plotting the bar chart
plt.figure(figsize=(12, 6))  # Set the figure size
plt.bar(movies, revenue, color=['blue', '#1147B2', '#1144B5', '#114285', '#114495'])  # Bar chart with custom colors
plt.xlabel('Movies', fontsize=15)  # Set the label for the x-axis
plt.ylabel('Revenue', fontsize=15)  # Set the label for the y-axis
plt.title('Top 5 Movies Based on Revenue')  # Set the title of the chart
plt.xticks(rotation=45, ha='right', fontsize=12)  # Rotate x-axis labels for better readability
plt.show()  # Display the plot
