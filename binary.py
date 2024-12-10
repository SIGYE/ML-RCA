import pandas as pd
from category_encoders import BinaryEncoder

data = {'color': ['red', 'green', 'blue', 'red']}
df = pd.DataFrame(data)

encoder = BinaryEncoder(cols=['color'])
binary_encoded = encoder.fit_transform(df)
print(binary_encoded)
