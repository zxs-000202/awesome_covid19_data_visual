import pandas as pd
data = pd.read_csv("test2.csv")
print(data)
data["sum"] = data.groupby(data["date"])["value"].transform('sum')
print(data)
data["rate"] = round(data["value"] / data["sum"] * 100,2)

data.to_csv('out.csv',index=False)