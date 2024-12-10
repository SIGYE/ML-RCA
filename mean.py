import pandas as pd

data = {
    "A" : [1,2,None,4,5],
    "B" : [None,2,3,4,5],
    "C" : ["cat", "dog", None, "cat", "dog"],
}
df = pd.DataFrame(data)

#mean
df["A"].fillna(df["A"].mean(), inplace=True)
#median 
df["B"].fillna(df["B"].median(), inplace=True)
#mode
df["C"].fillna(df["C"].mode()[0], inplace=True)