# Encoding refers to the process of converting categorical features into numerical features so that ML algorithms can use them. Categorical features can take on a limited number of values and are unordered, making them difficult for algorithms to handle. By encoding these features, we can convert them into numerical representations that can be useful for ML algorithms.



from sklearn.preprocessing import LabelEncoder
import pandas as pd

# Read data
data = pd.read_csv("data.csv", sep=',')
print("Original: \n",data)

# Define the label variable
label_col = 'sex'

# Create the LabelEncoder object
encoder = LabelEncoder()

# Transform the label variable
data[label_col] = encoder.fit_transform(data[label_col])

# Print the resulting encoded variable
print("Encoded: \n",data)



from sklearn.preprocessing import OneHotEncoder
import pandas as pd

# Read data
data = pd.read_csv("data.csv", sep=',')
print("Original: \n",data.head())

# Define categorical variables
categorical_cols = ['name','sex','zip code','profession']

# Create the OneHotEncoder object
encoder = OneHotEncoder(handle_unknown='error', drop='first')

# Fit and transform the categorical columns
encoded_cols = encoder.fit_transform(data[categorical_cols]).toarray()

# Create a DataFrame for the encoded columns
columns = encoder.get_feature_names(categorical_cols)
encoded_df = pd.DataFrame(encoded_cols, columns=columns)

# Replace the original columns with the encoded columns
data = pd.concat([data.drop(categorical_cols, axis=1), encoded_df], axis=1)

# Print the resulting encoded variables
print("Encoded: \n",data.head())




import pandas as pd
from sklearn.preprocessing import OrdinalEncoder

# Define the categorical variables
size_categories = ['Small', 'Medium', 'Large']

X = pd.DataFrame({'Size': ['Large', 'Small', 'Medium', 'Small']})

# Create the OrdinalEncoder object
encoder = OrdinalEncoder(categories=[size_categories])

# Transform the categorical variables
X_encoded = encoder.fit_transform(X)

# Print the original variables and the resulting encoded variables
print("Original: \n",X)
print("Encoded: \n",X_encoded)