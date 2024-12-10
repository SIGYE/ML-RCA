import pandas as pd

data = {
    "A" : [1,2,None,4,5]
}
df = pd.DataFrame(data)

df["A"].fillna(0, inplace=True)
print(df)