import pandas as pd
 
data = pd.read_csv("nba.csv", index_col ="Number")

second = data.loc[36]
 
print(second)