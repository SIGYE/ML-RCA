import pandas as pd

data = {'color': ['red', 'green', 'blue', 'red', 'green'],
        'price': [15, 20, 10, 25, 30]}  # Target variable
df = pd.DataFrame(data)

# Calculate target mean
means = df.groupby('color')['price'].mean()
df['color_target_encoded'] = df['color'].map(means)

print(df)
