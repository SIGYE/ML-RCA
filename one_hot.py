import pandas as pd
data = {
    'color': ['red', 'blue', 'green']
}
df = pd.DataFrame(data)

one_hot_encoded_df = pd.get_dummies(df, columns=['color'])
one_hot_encoded_df = one_hot_encoded_df.astype(int)
print(one_hot_encoded_df)