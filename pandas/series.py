import pandas as pd

# Creating a simple Series from a list
lst = [1, 2, 3, 4]
s = pd.Series(lst)
print(s)

# Creating a Series with specific data type and index
s = pd.Series(lst, dtype=float, index=['A', 'B', 'C', 'D'])
print(s)

# Creating two Series objects
x = pd.Series(['rami', 'sami'])
y = pd.Series(['razi', 'omar', 'omar'])

# Concatenating the two Series into one
z = pd.concat([x, y], ignore_index=True)
print(z)

# Dropping duplicates from the Series
z.drop_duplicates(inplace=True)
print(z)

# Copying the Series
w = z.copy()
print(w)

# Performing arithmetic operations on a Series
s2 = pd.Series([5, 15, 45])
print(s2.add(8))      # Adding 8 to each element
print(s2.multiply(8)) # Multiplying each element by 8
print(s2.div(2))      # Dividing each element by 2
