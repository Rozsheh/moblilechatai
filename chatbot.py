# Importing the libraries
import numpy as np
import pandas as pd

# Using NumPy to create an array and perform a calculation
array = np.array([1, 2, 3, 4])
doubled_array = array * 2
print("Doubled Array:", doubled_array)

# Using pandas to create a small DataFrame (a table of data)
data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [24, 27, 22]
}
df = pd.DataFrame(data)
print("\nDataFrame:")
print(df)
