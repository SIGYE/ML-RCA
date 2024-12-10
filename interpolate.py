import pandas as pd

data = {
    "Value": [1,None,3,None,5]
}
df = pd.DataFrame(data)

df["Interpolated"] = df["Value"].interpolate()
print(df)