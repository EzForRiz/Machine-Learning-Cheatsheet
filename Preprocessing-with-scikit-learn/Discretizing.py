# Discretizing features refers to the process of converting continuous numerical features into categorical features by dividing the range of the feature into intervals, called bins. It can be useful for transforming continuous features into a form that can be visualized and interpreted more easily.



import numpy as np
from sklearn.preprocessing import KBinsDiscretizer

# Define the numerical variables
X = np.array(
    [[1.9, 2.8, 6],
    [4.7, 5.6, 8],
    [0.1, 2.8, 12],
    [0.4, 8.2, 99]]
    )

# Create the KBinsDiscretizer object
discretizer = KBinsDiscretizer(n_bins=3, encode='ordinal')

# Transform the numerical variables
X_discretized = discretizer.fit_transform(X)

# Print the original variables and the resulting discretized variables
print("Original: \n",X)
print("Discretized: \n",X_discretized.round(2))




import numpy as np
from sklearn.preprocessing import QuantileTransformer

# Define the numerical variables
X = np.array(
    [[1.9, 2.8, 6],
    [4.7, 5.6, 8],
    [0.1, 2.8, 12],
    [0.4, 8.2, 99]]
    )

# Create the QuantileTransformer object
discretizer = QuantileTransformer(n_quantiles=3)

# Transform the numerical variables
X_discretized = discretizer.fit_transform(X)

# Print the original variables and the resulting discretized variables
print("Original: \n",X)
print("Discretized: \n",X_discretized.round(2))