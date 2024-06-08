import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load datasets
tips = sns.load_dataset("tips")
diamonds = sns.load_dataset("diamonds")

# Set the aesthetic style of the plots
sns.set(style="whitegrid")

# 1. Line plot: Relationship between size of the party and tip amount
plt.figure(figsize=(10, 6))
sns.lineplot(data=tips, x="size", y="tip")
plt.title('Line Plot: Tip Amount vs. Size of Party')
plt.xlabel('Size of Party')
plt.ylabel('Tip Amount')
plt.show()

# Analysis:
# The line plot shows how the tip amount varies with the size of the party.

# 2. Scatter plot: Relationship between total bill and tip amount
plt.figure(figsize=(10, 6))
sns.scatterplot(data=tips, x="total_bill", y="tip")
plt.title('Scatter Plot: Tip Amount vs. Total Bill')
plt.xlabel('Total Bill')
plt.ylabel('Tip Amount')
plt.show()

# Analysis:
# The scatter plot shows a positive correlation between the total bill and the tip amount.

# 3. Bar plot: Total bill by day and gender
plt.figure(figsize=(10, 6))
sns.barplot(data=tips, x='day', y='total_bill', hue='sex')
plt.title('Bar Plot: Total Bill by Day and Gender')
plt.xlabel('Day of the Week')
plt.ylabel('Total Bill')
plt.show()

# Analysis:
# The bar plot shows how the total bill varies by day of the week, split by gender.

# 4. Histogram: Distribution of diamond clarity, colored by cut
plt.figure(figsize=(12, 8))
sns.histplot(data=diamonds.sort_values('clarity').reset_index(), x='clarity', hue='cut', alpha=0.3, multiple='dodge')
plt.title('Histogram: Diamond Clarity Distribution by Cut')
plt.xlabel('Clarity')
plt.ylabel('Count')
plt.show()

# Analysis:
# The histogram shows the distribution of diamond clarity, with different cuts represented by different colors.

# 5. Bar plot: Average price of diamonds by color
plt.figure(figsize=(10, 6))
sns.barplot(data=diamonds, x="color", y="price")
plt.title('Bar Plot: Average Price of Diamonds by Color')
plt.xlabel('Color')
plt.ylabel('Average Price')
plt.show()

# Analysis:
# The bar plot shows the average price of diamonds for each color grade.
