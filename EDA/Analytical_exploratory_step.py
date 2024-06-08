import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

tips = sns.load_dataset("tips")
diamonds = sns.load_dataset("diamonds")

# print(tips.info)
# print(diamonds.info)

# print(tips.head())
# print(diamonds.head())

# print(tips.tail())
# print(diamonds.tail())

# print(tips.shape)
# print(diamonds.shape)

# print(tips.info())
# print(diamonds.info())

# print(tips.describe(exclude='number'))
# print(diamonds.describe(exclude='number'))

# print(diamonds['cut'].value_counts(normalize=True))
# print(diamonds['cut'].unique())

# sns.histplot(data=tips, x='total_bill', bins=10)
# sns.kdeplot(data=tips, x='total_bill')
# plt.show()

# sns.histplot(data=diamonds, x='price', bins=10)
# sns.kdeplot(data=diamonds, x='price')
# plt.show()

# sns.displot(data=tips, x='total_bill', kind="hist", col="sex", kde=True)
# plt.show()

# sns.countplot(data=diamonds, x='color')
# sns.countplot(data=diamonds, x='cut')
# sns.countplot(data=diamonds, x='clarity')

# plt.pie(tips.smoker.value_counts(), labels=["non-smoker", "smoker"], autopct="%1.2f%%")
plt.pie(tips.smoker.value_counts(), labels=tips.smoker.value_counts().index, autopct="%1.2f%%")
plt.show()