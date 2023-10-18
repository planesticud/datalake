import pandas as pd
import pandasql as ps

# Read the Parquet file into a DataFrame
df = pd.read_parquet('1111500036.parquet', engine='pyarrow')


# Define your SQL query
query = """
SELECT * 
FROM df 

"""

# Use pandasql to execute the SQL query on the DataFrame
result = ps.sqldf(query, locals())

print(result)