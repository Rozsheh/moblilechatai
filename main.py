import numpy as np
import requests

# Using numpy to create an array
array = np.array([1, 2, 3, 4, 5])
print("Numpy Array:", array)

# Using requests to fetch data from an example API
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
if response.status_code == 200:
    print("\nResponse from API:", response.json())
else:
    print("Failed to fetch data")
