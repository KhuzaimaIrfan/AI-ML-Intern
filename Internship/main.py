import pandas as pd 

df = pd.read_csv("Titanic-Dataset.csv")

print(df)

print(df.head)
print(df.info)
print(df.shape)
print(df.describe)
print(df.isnull)