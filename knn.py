import pandas as pd
from sklearn.impute import KNNImputer

data = {
    "A": [1,2, None, 4, 5],
    "B" : [None, 2,3,4,5],
    "C" : ["cat", "dog", None, "cat", "dog"],
}

df = pd.DataFrame(data)
print("Original data frame: \n", df)
imputer = KNNImputer(n_neighbors=2)

df_encoded = pd.get_dummies(df, columns=["C"], drop_first=True)
imputed_data = imputer.fit_transform(df_encoded)

imputed_df = pd.DataFrame(imputed_data, columns=df_encoded.columns)
print(imputed_df)