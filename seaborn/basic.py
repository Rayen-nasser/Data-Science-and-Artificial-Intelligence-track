import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_csv("mpg_raw.csv")

# 1. Count plot of 'origin'
plt.figure(figsize=(10, 5))
sns.countplot(x='origin', data=df)
plt.title("Count of Cars by Origin")
plt.show()

# 2. Histogram of 'mpg', stacked by 'origin'
plt.figure(figsize=(10, 5))
sns.histplot(df, x='mpg', hue="origin", multiple="stack")
plt.title("MPG Distribution - Histogram")
plt.show()

# 3. Violin plot to show the distribution of 'mpg'
plt.figure(figsize=(10, 5))
sns.violinplot(data=df['mpg'])
plt.title("MPG Distribution - Violin Plot")
plt.show()

# 4. KDE plot of 'mpg', colored by 'origin'
plt.figure(figsize=(10, 5))
sns.kdeplot(data=df, x="mpg", hue="origin")
plt.title("MPG Distribution - KDE Plot")
plt.show()

# 5. Bar plot of 'horsepower' by 'origin', using standard deviation as estimator
plt.figure(figsize=(10, 5))
sns.barplot(x='origin', y='horsepower', data=df, estimator=np.std)
plt.title("Horsepower by Origin (Standard Deviation)")
plt.show()

# 6. Swarm plot of 'mpg' by 'origin', colored by 'cylinders'
plt.figure(figsize=(10, 5))
sns.swarmplot(x='origin', y='mpg', hue="cylinders", data=df)
plt.title("MPG by Origin and Cylinders")
plt.show()

# 7. Box plot of 'mpg' by 'origin', colored by 'cylinders'
plt.figure(figsize=(10, 5))
sns.boxplot(x="origin", y='mpg', data=df, hue="cylinders")
plt.title("MPG Box Plot by Origin and Cylinders")
plt.show()

# 8. Categorical bar plot of 'horsepower' by 'origin', colored by 'cylinders'
sns.catplot(data=df, kind="bar", x="origin", y="horsepower", hue="cylinders")
plt.title("Horsepower by Origin and Cylinders")
plt.show()

# 9. Joint plot of 'mpg' and 'weight' with regression line
sns.jointplot(x='mpg', y="weight", data=df, kind='reg')
plt.show()

# 10. Pair plot of the dataset, colored by 'origin'
sns.pairplot(df, hue="origin", palette="pastel")
plt.show()

# 11. Create a new column 'mpg_level' based on 'mpg'
df['mpg_level'] = df['mpg'].apply(lambda x: 'low' if x < 15 else 'high' if x > 30 else 'medium')

# 12. Count plot of 'mpg_level' by 'model_year'
plt.figure(figsize=(10, 5))
sns.countplot(x='model_year', hue='cylinders', data=df)
plt.title("Count of MPG Level by Model Year")
plt.show()

# 13. Regression plot of 'horsepower' vs 'mpg' with point size based on 'weight'
plt.figure(figsize=(10, 5))
sns.regplot(x="horsepower", y="mpg", data=df, scatter_kws={"s": df["weight"]/50})
plt.title("Horsepower vs MPG Regression Plot")
plt.show()
