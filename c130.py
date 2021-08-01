import pandas as pd
import csv

df = pd.read_csv("total_stars.csv")
print(df.shape)
del df ["Luminosity"]
print(df.shape)
del df ["Star_name"]
del df ["Distance"]
del df ["Mass"]
del df ["Radius"]
print(df.shape)
print(list(df))
df.to_csv('main.csv')