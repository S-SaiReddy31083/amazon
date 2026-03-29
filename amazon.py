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



