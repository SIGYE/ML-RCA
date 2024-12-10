import pandas as pd

data = {
    "Value" : [1,None,None,4,5,None]
}
df = pd.DataFrame(data)

df["forward_fill"] = df["Value"].fillna(method="ffill")
df["backward_fill"] = df["Value"].fillna(method="bfill")
print(df)