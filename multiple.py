import pandas as pd
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer

data = {
    "A" : [1,2,None,4],
    "B" : [None,2,3,4],
}
df = pd.DataFrame(data)

imputer = IterativeImputer()
imputed_data = imputer.fit_transform(df)

print(pd.DataFrame(imputed_data, columns=df.columns))