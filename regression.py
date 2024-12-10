import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "X" : [1,2,3,4,5],
    "Y" : [2, None,6,8,10]
}

df = pd.DataFrame(data)
train = df[df["Y"].notnull()]
x_train = train[["X"]]
y_train = train["Y"]

model = LinearRegression()
model.fit(x_train, y_train)

missing = df[df["Y"].isnull()]
X_missing = missing[["X"]]
df.loc[df["Y"].isnull(), "Y"] = model.predict(X_missing)
print(df)