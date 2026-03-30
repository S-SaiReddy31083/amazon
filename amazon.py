import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("Amazon/amazon_1000_products.xlsx")

#Displaying the first few rows of the dataset

print(df.head())

#Checking the missing values in the dataset
print("Null Values in the dataset: ")
print(df.isnull().sum())
print(df.info())

#Checking the duplicates in the dataset
print("Duplicates in the dataset: ")
print(df.duplicated().sum())

#Summary statistics of the dataset
print("Summary Statistics: ")
print(df.describe())

#Distribution of ratings
plt.figure(figsize=(10,6))
plt.bar(df["Rating"].value_counts().index,df["Rating"].value_counts().values)
plt.xlabel("Ratings")
plt.ylabel("Count")
plt.title("Distribution of Ratings")
plt.show()

#Distribution of prices per category
plt.figure(figsize=(12,8))
sns.histplot(data = df, x = "Price (USD)",hue = "Category", multiple = "stack")
plt.xlabel("Price (USD)")
plt.ylabel("Count")
plt.title("Distribution of Prices per Category")
plt.show()



