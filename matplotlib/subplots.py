import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv("tmdb_movies_data.csv")

# Create a figure for subplots
plt.figure(figsize=(15, 10))  # Set the figure size

# First chart: Bar plot of top 5 movies by revenue
plt.subplot(2, 2, 1)
top_revenue = df.groupby('original_title').sum().sort_values(by="revenue", ascending=False)
top_5_movies = top_revenue.head(5)
movies = top_5_movies.index
revenue = top_5_movies['revenue'].values
plt.bar(movies, revenue, color='skyblue')
plt.xlabel('Movies', fontsize=12)
plt.ylabel('Revenue', fontsize=12)
plt.title('Top 5 Movies by Revenue', fontsize=14)
plt.xticks(rotation=45, ha='right')

# Second chart: Pie chart of top 5 genres by revenue
plt.subplot(2, 2, 2)
top_genres = df.groupby('genres')['revenue'].sum().sort_values(ascending=False).head(5)
plt.pie(top_genres.values, labels=top_genres.index, explode=[0.1, 0, 0, 0, 0], autopct='%1.2f%%', startangle=140, colors=plt.cm.Paired(np.arange(5)))
plt.title('Top 5 Genres by Revenue', fontsize=14)

# Third chart: Scatter plot of vote average and vote count vs revenue
plt.subplot(2, 2, 3)
plt.scatter(df['vote_average'], df['revenue'], alpha=0.8, marker='*', label='Vote Average')
plt.scatter(df['vote_count'], df['revenue'], alpha=0.7, marker='+', label='Vote Count')
plt.xlabel('Vote Average / Vote Count', fontsize=12)
plt.ylabel('Revenue', fontsize=12)
plt.title('Vote Average and Vote Count vs Revenue', fontsize=14)
plt.legend(loc='upper right')

# Fourth chart: Line plot of the number of movies released annually
plt.subplot(2, 2, 4)
movies_count = df['release_year'].value_counts().reset_index()
movies_count.columns = ['year', 'count']
movies_count = movies_count.sort_values(by='year')
plt.plot(movies_count['year'], movies_count['count'], color='0.2', marker='o')
plt.xlabel('Year', fontsize=12)
plt.ylabel('Movie Count', fontsize=12)
plt.title('Number of Movies Released Annually', fontsize=14)

# Adjust layout for better readability
plt.tight_layout()

# Display the plots
# plt.savefig("subplot-v2.png", dpi=300)
plt.show()
