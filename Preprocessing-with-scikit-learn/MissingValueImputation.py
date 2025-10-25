# Missing data is a common problem in real-world datasets that can arise due to a variety of reasons, such as measurement errors, data corruption, or simply because the data was not collected. When working with such datasets, we need to handle missing values appropriately, since many ML algorithms cannot handle missing data.

# Imputation is the process of filling in missing values with estimated values based on the available data. This can be a challenging task because it requires us to carefully consider the type of missing data, the nature of the dataset, and the problem we are trying to solve.




# SimpleImputer class


import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.impute import SimpleImputer

# Load the Iris dataset
data = load_iris()
X = data.data

# Introduce missing values in the dataset
X[0, 0] = np.nan
X[1, 2] = np.nan
X[2, 3] = np.nan

# Create an instance of SimpleImputer with the mean strategy
imputer = SimpleImputer(strategy='mean')

# Transform the data
X_transformed = imputer.fit_transform(X)

# Print the results
print("Original data: \n", X)
print("\nTransformed data: \n", X_transformed)




# IterativeImputer

from sklearn.datasets import load_diabetes
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import IterativeImputer
import numpy as np

# load the diabetes dataset
diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target

# create a sample with missing values
rng = np.random.RandomState(0)
missing_mask = rng.binomial(1, 0.1, size=X.shape).astype(bool)
X[missing_mask] = np.nan

# create an instance of IterativeImputer
imputer = IterativeImputer(
    random_state=0,
    n_nearest_features=2,
    initial_strategy = 'median'
    )

# fit and transform the imputer
X_imputed = imputer.fit_transform(X)

# print the results
print("Original data: \n", X[:3])
print("\nImputed data: \n", X_imputed[:3])





# KNNImputer

import numpy as np
from sklearn.impute import KNNImputer
from sklearn.datasets import load_iris

# Load the Iris dataset
data = load_iris()
X = data.data

# Introduce missing values in the dataset
X[0, 0] = np.nan
X[1, 2] = np.nan
X[2, 3] = np.nan

# apply KNNImputer
imputer = KNNImputer(n_neighbors=2)
X_imputed = imputer.fit_transform(X)

# print the results
print("Original data: \n", X)
print("\nImputed data: \n", X_imputed)