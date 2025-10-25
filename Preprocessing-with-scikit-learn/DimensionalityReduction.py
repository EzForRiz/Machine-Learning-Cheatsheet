# In the simplest terms, dimensionality reduction is the process of reducing the number of features or variables in a dataset while preserving the most important information. This is particularly useful when dealing with datasets with a large number of features, as it can help simplify the data, making it easier to work with, as well as providing a form of regularization.


# Principal Component Analysis#




from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# perform PCA
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)

# print results
print("Original data: \n", X[:3])
print("\nTransformed data: \n", X_pca[:3])




from sklearn.datasets import load_iris
from sklearn.decomposition import TruncatedSVD
import matplotlib.pyplot as plt

# load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# perform SVD
svd = TruncatedSVD(n_components=2)
X_svd = svd.fit_transform(X)

# print results
print("Original data: \n", X[:3])
print("\nTransformed data: \n", X_svd[:3])




import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.decomposition import FactorAnalysis
import matplotlib.pyplot as plt

# Load iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Perform factor analysis with 2 components
fa = FactorAnalysis(n_components=2, random_state=0)
X_fa = fa.fit_transform(X)

# Print the loadings of each feature for the first two components
loadings = pd.DataFrame(fa.components_.T, columns=['Factor 1', 'Factor 2'], index=iris.feature_names)
print(loadings)





from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

# load the iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# apply PCA with 4 components
n_components = 4
pca = PCA(n_components=n_components)
pca.fit(X)

# plot cumulative explained variance
fig, ax = plt.subplots(dpi = 300)
x_axis = np.arange(1, n_components+1)
ax.plot(
    x_axis,
    np.cumsum(pca.explained_variance_ratio_),
    'ro-'
    )
plt.xticks(x_axis)

plt.xlabel('Number of Components')
plt.ylabel('Cumulative Explained Variance Ratio')
plt.show()

fig.savefig("output/img.png")
plt.close(fig)