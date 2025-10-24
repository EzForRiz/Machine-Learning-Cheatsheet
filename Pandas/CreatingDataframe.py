import pandas as pd

df = pd.DataFrame({
  "Names": ["Jane", "John", "Matt", "Ashley"],
  "Ages": [26, 24, 28, 25],
  "Score": [91.2, 94.1, 89.5, 92.3]
})

print(df)



import numpy as np
import pandas as pd

arr = np.random.randint(1, 10, size=(3,5))

df = pd.DataFrame(arr, columns=["A","B","C","D","E"])

print(df)



#DataFrame is a two-dimensional data structure that consists of rows and columns. Thus, we can convert a two-dimensional array into a DataFrame. For instance, the DataFrame constructor accepts NumPy arrays.

# The code below creates a DataFrame using a NumPy array. By default, column names are assigned integer index, but we can change it using the columns parameter.



