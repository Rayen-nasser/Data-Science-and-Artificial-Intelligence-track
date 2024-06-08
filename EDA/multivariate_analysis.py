import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

tips = sns.load_dataset("tips")
diamonds = sns.load_dataset("diamonds")

# sns.scatterplot(data=tips, x='total_bill', y='tip', hue='smoker')
# plt.show()

sns.catplot(data=tips, x="time", y="total_bill",col="day" ,hue="sex", kind="bar")
plt.show()