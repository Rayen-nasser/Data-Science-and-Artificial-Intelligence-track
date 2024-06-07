import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("tmdb_movies_data.csv")
x = np.random.randn(500)
# plt.hist(x, 5)
# plt.hist(df['vote_average'])
# plt.show()

# print(df['vote_average'].min())
# print(df['vote_average'].max())

# bins_num = [0,2,4,6,8,10]
# plt.hist(df["vote_average"], facecolor='b', edgecolor='red' ,bins= bins_num)
# plt.xlabel('vote average')
# plt.ylabel('frequency')
# plt.title('distribution of vote average')
# plt.show()