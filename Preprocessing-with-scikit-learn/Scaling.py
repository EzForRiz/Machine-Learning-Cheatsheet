# Scaling means transforming numerical variables so that they have a similar scale. It’s an important step in the ML process because some algorithms are sensitive to the scale of the input variables. The scikit-learn library provides several methods for scaling numerical variables, including StandardScaler, MinMaxScaler, and RobustScaler.

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

# load the breast cancer dataset
cancer = load_breast_cancer()

# split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(cancer.data, cancer.target, random_state=42)

# fit an SVM model to the training data and evaluate its performance on the test data
svm = SVC(random_state=42)
svm.fit(X_train, y_train)
y_pred = svm.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Accuracy without scaling: {acc:.2f}")  # output: Accuracy without scaling: 0.94

# scale the input features using StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# fit an SVM model to the scaled training data and evaluate its performance on the scaled test data
svm_scaled = SVC(random_state=42)
svm_scaled.fit(X_train_scaled, y_train)
y_pred_scaled = svm_scaled.predict(X_test_scaled)
acc_scaled = accuracy_score(y_test, y_pred_scaled)
print(f"Accuracy with scaling: {acc_scaled:.2f}")  # output: Accuracy with scaling: 0.97





import numpy as np
from sklearn.preprocessing import StandardScaler

# Define the numerical variables
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Create the StandardScaler object
scaler = StandardScaler()

# Transform the numerical variables
X_scaled = scaler.fit_transform(X)

# Print the original variables and the resulting scaled variables
print("Original: \n",X)
print("Scaled: \n",X_scaled.round(2))





import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Define the numerical variables
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Create the MinMaxScaler object
scaler = MinMaxScaler()

# Transform the numerical variables
X_scaled = scaler.fit_transform(X)

# Print the original variables and the resulting scaled variables
print("Original: \n",X)
print("Scaled: \n",X_scaled.round(2))






import numpy as np
from sklearn.preprocessing import RobustScaler

# Define the numerical variables
X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9999]])

# Create the RobustScaler object
scaler = RobustScaler()

# Transform the numerical variables
X_scaled = scaler.fit_transform(X)

# Print the original variables and the resulting scaled variables
print("Original: \n",X)
print("Scaled: \n",X_scaled.round(2))