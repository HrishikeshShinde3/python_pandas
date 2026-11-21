import pandas as pd

data = pd.read_csv("nba.csv", index_col="Name")

first = data["College"]
print("\nSingle Column selected from Dataset")
print(first.head(3))