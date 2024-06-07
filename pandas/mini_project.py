import pandas as pd

# Data
data = {
    "LEVEL": [100, 100, 100, 200, None, 200, 300, 300, None],
    "COURSE NAME": ["Introduction to IT", "Programming Fundamentals", "Introduction to MIS", "Database Management",
                    "Data Structures", "Systems Analysis and Design", "Network Security", "Algorithms", None],
    "MAJOR": ["IT", "CS", "MIS", None, "CS", "MIS", None, "CS", None]
}

# Creating the DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Description DataFrame
print(df.describe(include=[object]))

print(df['LEVEL'].astype(float))

print(df.head(4))

print(df.dropna(how='any', axis=0))



