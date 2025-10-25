import numpy as np
import pandas as pd

df = pd.DataFrame({
    "A": [1, 2, 3, np.nan],
    "B": [2.4, 6.2, 5.1, np.nan],
    "C": ["foo","zoo","bar", np.nan]
})

print(df)





import numpy as np
import pandas as pd

df = pd.DataFrame({
    "A": [1, 2, 3, np.nan],
    "B": [2.4, 6.2, 5.1, np.nan],
    "C": ["foo","zoo","bar", np.nan]
})

df["A"] = df["A"].astype(pd.Int64Dtype())

print(df)





# The isna and notna functions
import numpy as np
import pandas as pd

df = pd.DataFrame({
    "A": [1, 2, 3, np.nan, 7],
    "B": [2.4, np.nan, 5.1, np.nan, 2.6],
    "C": [np.nan, "foo","zoo","bar", np.nan],
    "D": [11.5, np.nan, 6.2, 21.1, 8.7]
})

print(df.isna())



import numpy as np
import pandas as pd

df = pd.DataFrame({
    "A": [1, 2, 3, np.nan, 7],
    "B": [2.4, np.nan, 5.1, np.nan, 2.6],
    "C": [np.nan, "foo","zoo","bar", np.nan],
    "D": [11.5, np.nan, 6.2, 21.1, 8.7]
})

print(df.isna().sum())




import numpy as np
import pandas as pd

df = pd.DataFrame({
    "A": [1, 2, 3, np.nan, 7],
    "B": [2.4, np.nan, 5.1, np.nan, 2.6],
    "C": [np.nan, "foo","zoo","bar", np.nan],
    "D": [11.5, np.nan, 6.2, 21.1, 8.7]
})

print(df.isna().sum(axis=1))




import numpy as np
import pandas as pd

df = pd.DataFrame({
    "A": [1, 2, 3, np.nan, 7],
    "B": [2.4, np.nan, 5.1, np.nan, 2.6],
    "C": [np.nan, "foo","zoo","bar", np.nan],
    "D": [11.5, np.nan, 6.2, 21.1, 8.7]
})

print(df.notna().sum())







# Dropping Rows and Columns with Missing Values



import numpy as np
import pandas as pd

df = pd.DataFrame({
    "A": [1, 2, 3, np.nan, 7],
    "B": [2.4, np.nan, 5.1, np.nan, 2.6],
    "C": [np.nan, "foo","zoo","bar", np.nan],
    "D": [11.5, np.nan, 6.2, 21.1, 8.7],
    "E": [1, 2, 3, 4, 5]
})

# Drop rows that have at least one missing value
print(df.dropna(axis=0, how="any"))





import numpy as np
import pandas as pd

df = pd.DataFrame({
    "A": [1, 2, 3, np.nan, 7],
    "B": [2.4, np.nan, 5.1, np.nan, 2.6],
    "C": [np.nan, "foo","zoo","bar", np.nan],
    "D": [11.5, np.nan, 6.2, 21.1, 8.7],
    "E": [1, 2, 3, 4, 5]
})

# Drop columns that have at least one missing value
print(df.dropna(axis=1, how="any"))




# dropna

import numpy as np
import pandas as pd

df = pd.DataFrame({
    "A": [1, 2, 3, np.nan, 7],
    "B": [2.4, np.nan, 5.1, np.nan, 2.6],
    "C": [np.nan, "foo","zoo","bar", np.nan],
    "D": [11.5, np.nan, 6.2, 21.1, 8.7],
    "E": [1, 2, 3, 4, 5]
})

# Drop rows that have less than 4 non-missing values
print(df.dropna(thresh=4))






# inplace parameter

import numpy as np
import pandas as pd

df = pd.DataFrame({
    "A": [1, 2, 3, np.nan, 7],
    "B": [2.4, np.nan, 5.1, np.nan, 2.6],
    "C": [np.nan, "foo","zoo","bar", np.nan],
    "D": [11.5, np.nan, 6.2, 21.1, 8.7],
    "E": [1, 2, 3, 4, 5]
})

# Drop rows that have less than 4 non-missing values
df.dropna(thresh=4, inplace=True)

print(df)








# Replacing the Missing Values



# fillna function

import numpy as np
import pandas as pd

df = pd.DataFrame({
    "A": [1, 2, 3, np.nan, 7],
    "B": [2.4, np.nan, 5.1, np.nan, 2.6],
    "C": [np.nan, "foo","zoo","bar", np.nan],
    "D": [11.5, np.nan, 6.2, 21.1, 8.7],
    "E": [1, 2, 3, 4, 5]
})

print(df["A"].fillna(value = df["A"].mean()))





df = pd.DataFrame({
    "A": [1, 2, 3, np.nan, 7],
    "B": [2.4, np.nan, 5.1, np.nan, 2.6],
    "C": [np.nan, "foo","zoo","bar", np.nan],
    "D": [11.5, np.nan, 6.2, 21.1, 8.7],
    "E": [1, 2, 3, 4, 5]
})

# find the replacement values
value_a = df["A"].mean()
value_d = df["D"].mean()

# replace the missing values
print(df.fillna({"A": value_a, "D": value_d}))







import numpy as np
import pandas as pd

df = pd.DataFrame({
    "A": [1, 2, 3, np.nan, 7],
    "B": [2.4, np.nan, 5.1, np.nan, 2.6],
    "C": [np.nan, "foo","zoo","bar", np.nan],
    "D": [11.5, np.nan, 6.2, 21.1, 8.7],
    "E": [1, 2, 3, 4, 5]
})

print("Filling backward")
print(df["A"].fillna(method="bfill"))

print("\nFilling forward")
print(df["A"].fillna(method="ffill"))







import numpy as np
import pandas as pd

df = pd.DataFrame({
    "A": [1, 2, np.nan, np.nan, 8]
})

print("Without the limit parameter")
print(df.fillna(method="bfill"))

print("\nWith the limit parameter")
print(df.fillna(method="bfill", limit=1))









# Filling the Missing Values

import numpy as np
import pandas as pd

df = pd.DataFrame({
    "Date": pd.date_range(start="2021-10-01", periods=10),
    "Measurement": [16, 13, 14, 12, np.nan, np.nan, np.nan, 8, 7, 5]
})

def fill_missing_values():
  try:
    
    df.fillna(method="ffill", limit=2, inplace=True)
    df.fillna(value=df["Measurement"].mean(), inplace=True)
    return list(df["Measurement"])
    
  except:
    pass