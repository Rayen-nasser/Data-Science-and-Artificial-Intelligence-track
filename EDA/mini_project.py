import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the tips dataset
tips = sns.load_dataset("tips")

# Display the first few rows of the dataset
print(tips.head())

# Set the aesthetic style of the plots
sns.set(style="whitegrid")

# أولا: تحليل متغير واحد
# 1. توزيع متغير total_bill
plt.figure(figsize=(10, 6))
sns.histplot(tips['total_bill'], kde=True, bins=30)
plt.title('Distribution of Total Bill')
plt.xlabel('Total Bill')
plt.ylabel('Frequency')
plt.show()
# Insights:
# 1. The distribution of total bills is right-skewed, with most bills being between $10 and $20.
# 2. There are some outliers with total bills exceeding $50, indicating a few high-spending customers.

# 2. توزيع متغير tip
plt.figure(figsize=(10, 6))
sns.histplot(tips['tip'], kde=True, bins=30)
plt.title('Distribution of Tip Amount')
plt.xlabel('Tip Amount')
plt.ylabel('Frequency')
plt.show()
# Insights:
# 1. The tip amount distribution is also right-skewed, with most tips ranging between $2 and $3.
# 2. There are some higher tips given, with the maximum tip amount going beyond $9, showing generosity in tipping for some customers.

# ثانيا: تحليل متغيرين
# 1. العلاقة بين total_bill و tip
plt.figure(figsize=(10, 6))
sns.scatterplot(data=tips, x='total_bill', y='tip')
plt.title('Scatter Plot: Total Bill vs. Tip Amount')
plt.xlabel('Total Bill')
plt.ylabel('Tip Amount')
plt.show()
# Insights:
# 1. There is a positive correlation between total bill and tip amount, indicating that higher bills tend to have higher tips.
# 2. Despite the positive trend, there is a wide variation in tips for similar total bill amounts, suggesting individual tipping behavior differences.

# 2. متوسط الفاتورة الكلية حسب اليوم
plt.figure(figsize=(10, 6))
sns.barplot(data=tips, x='day', y='total_bill', ci=None)
plt.title('Average Total Bill by Day')
plt.xlabel('Day of the Week')
plt.ylabel('Average Total Bill')
plt.show()
# Insights:
# 1. The average total bill is highest on Sundays, indicating higher spending on that day.
# 2. Thursdays have the lowest average total bill, suggesting lighter spending or fewer customers.

# ثالثا: تحليل عدة متغيرات
# 1. متوسط الفاتورة الكلية وتوزيع البقشيش حسب الجنس واليوم
plt.figure(figsize=(12, 8))
sns.boxplot(data=tips, x='day', y='total_bill', hue='sex')
plt.title('Total Bill Distribution by Day and Gender')
plt.xlabel('Day of the Week')
plt.ylabel('Total Bill')
plt.show()
# Insights:
# 1. Males generally have higher total bills compared to females across all days.
# 2. There is a noticeable variation in total bills, especially on Saturdays and Sundays, indicating diverse spending patterns on weekends.

# 2. العلاقة بين حجم المجموعة ومتوسط الفاتورة الكلية
plt.figure(figsize=(10, 6))
sns.barplot(data=tips, x='size', y='total_bill')
plt.title('Average Total Bill by Party Size')
plt.xlabel('Party Size')
plt.ylabel('Average Total Bill')
plt.show()
# Insights:
# 1. The average total bill increases with the party size, reflecting more consumption with larger groups.
# 2. Parties of size 6 have the highest average total bill, which is significantly higher than parties of smaller sizes.

# Conclusion
# This EDA provided insights into the distribution and relationships between various features in the tips dataset.
# Single variable analyses revealed the skewed nature of total bills and tips, while bivariate analyses highlighted correlations between total bill, tips, days, and genders.
# Finally, multivariate analyses underscored the influence of party size and gender on total bills, offering a comprehensive understanding of the dataset.
