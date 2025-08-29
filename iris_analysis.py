import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Task 1: Load and Explore the Dataset
iris_data = load_iris()
df = pd.DataFrame(
    data=iris_data.data, 
    columns=iris_data.feature_names
)
df['species'] = pd.Categorical.from_codes(iris_data.target, iris_data.target_names)

print("First 5 rows of the dataset:")
print(df.head())
print("\nDataset info:")
print(df.info())
print("\nMissing values per column:")
print(df.isnull().sum())

# Task 2: Basic Data Analysis
print("\nBasic statistics:")
print(df.describe())

grouped = df.groupby('species').mean()
print("\nMean of numerical columns by species:")
print(grouped)

# Task 3: Data Visualization
plt.figure(figsize=(8,5))
for species in df['species'].unique():
    subset = df[df['species'] == species]
    plt.plot(subset.index, subset['sepal length (cm)'], label=species)
plt.title("Sepal Length Trend by Species")
plt.xlabel("Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2 Bar chart: Average petal length per species
plt.figure(figsize=(6,4))
sns.barplot(x=grouped.index, y=grouped['petal length (cm)'], palette="viridis")
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.show()

# 3 Histogram: Distribution of sepal width
plt.figure(figsize=(6,4))
plt.hist(df['sepal width (cm)'], bins=10, color='skyblue', edgecolor='black')
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4 Scatter plot: Sepal length vs. Petal length
plt.figure(figsize=(6,4))
sns.scatterplot(
    data=df, 
    x='sepal length (cm)', 
    y='petal length (cm)', 
    hue='species', 
    palette='deep'
)
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()
