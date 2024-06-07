import pandas as pd

# Create a DataFrame from the list of dictionaries
data = [
    {"name": "Alice", "gpa": 3.5, "major": "Computer Science"},
    {"name": "Bob", "gpa": 3.8, "level": "Undergraduate", "major": "Mathematics"},
    {"name": "Charlie", "gpa": 3.2, "level": "Graduate", "major": "Physics"},
    {"name": "David", "gpa": 3.9, "major": "Chemistry"},
    {"name": "Eva", "gpa": 3.7, "level": "Undergraduate", "major": "Biology"},
    {"name": "Frank", "gpa": 3.4, "level": "Undergraduate", "major": "Computer Science"},
    {"name": "Grace", "gpa": 3.6, "level": "Graduate", "major": "Physics"},
]

students = pd.DataFrame(data)

# Group by 'major' and calculate mean GPA
mean_gpa_by_major = students[['major', 'gpa']].groupby('major').mean()
print(mean_gpa_by_major)

# Description of categorical columns
print(students.describe(include=[object]))

# Select specific columns
print(students[['name', 'level']])

# Slice rows 3 to 5
print(students[3:5])

# Select specific rows and columns using loc
print(students.loc[3:5, ['name', 'level']])

# Random sample of 5 students
print(students.sample(5, random_state=3))

# Filter students with GPA > 3.5
print(students[students['gpa'] > 3.5])

# Filter students with missing 'level'
print(students[students['level'].isnull()])

# GPA statistics
print(f"Max GPA: {students['gpa'].max()}")
print(f"Min GPA: {students['gpa'].min()}")
print(f"Sum GPA: {students['gpa'].sum()}")

# Function to add bonus to GPA
def gpa_bonus(gpa):
    return gpa + 0.15

# Apply GPA bonus
print("\nBefore:\n", students['gpa'])
print("\nAfter:\n", students['gpa'].apply(gpa_bonus))

# Drop row with index 1
print(students.drop(1, axis=0))

# Drop rows with any missing values
print(students.dropna(how="any", axis=0))

# Drop columns with any missing values
print(students.dropna(how="any", axis=1))

# Fill missing values with 'Undergraduate'
print(students.fillna('Undergraduate'))

# Sort by GPA in descending order
print(students.sort_values(by='gpa', ascending=False))

# Sort by index in descending order
print(students.sort_index(axis=0, ascending=False))
