import pandas as pd

# Create a simple test DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'London', 'San Francisco']
}
df = pd.DataFrame(data)

# Save the DataFrame as a Parquet file
df.to_parquet('test.parquet', engine='pyarrow')

print('Parquet file saved as test.parquet')