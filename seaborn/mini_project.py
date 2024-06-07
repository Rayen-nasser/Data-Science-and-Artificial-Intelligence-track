import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
tips_dataset = sns.load_dataset('tips')
print(tips_dataset.head())

# histogram --------> tip with day
sns.set_style('whitegrid')
sns.histplot(tips_dataset, x='tip', hue='day', element='step')
plt.show()

# displot  --------> tip with day
sns.displot(data=tips_dataset, x='day', hue='sex',  shrink = 0.8, palette= 'Set1', hue_order = ['Female', 'Male'])
plt.show()

# ecdf plot --------> tip with time
sns.set_style('darkgrid')
sns.set(font_scale=1.25)
sns.ecdfplot(x = tips_dataset.tip, hue=tips_dataset.time, palette='summer', linewidth=3)
plt.show()