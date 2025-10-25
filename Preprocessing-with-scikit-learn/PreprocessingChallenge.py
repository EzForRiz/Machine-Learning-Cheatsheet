# Coding Challenge: Preprocessing
# Practice preprocessing data with scikit-learn.

# Now we’ll work with a dataset containing information about a bank’s customer base, featuring the following variables:

# customerID: The customer’s unique ID.

# gender: The customer’s gender.

# SeniorCitizen: The customer’s senior citizen status.

# Partner: The customer’s relationship status.

# Dependents: The customer’s number of dependents?

# tenure: The length of time (in months) the the individual has been a customer.

# Services that the customer has subscribed to:

# PhoneService

# MultipleLines

# InternetService

# OnlineSecurity

# OnlineBackup

# DeviceProtection

# TechSupport

# StreamingTV

# StreamingMovies

# Contract: The customer’s current contract type: “Month-to-Month,” “One Year,” “Two Year.”

# PaperlessBilling: The customer’s preference regarding paperless billing.

# PaymentMethod: The customer’s preferred method of bank payment: bank withdrawal, credit card, mailed check.

# MonthlyCharges: The customer’s current total monthly charge.

# TotalCharges: The customer’s total charges.

# Churn: Whether or not the customer has exited or churned (our target variable).





import pandas as pd

data = pd.read_csv('data.csv')

# Defining column types
id_col = ['customerID']
num_cols = ['SeniorCitizen', 'tenure', 'MonthlyCharges', 'TotalCharges']
cat_cols = [
    'gender', 'Partner', 'Dependents',
    'PhoneService', 'MultipleLines', 'InternetService',
    'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
    'TechSupport', 'StreamingTV', 'StreamingMovies',
    'Contract', 'PaperlessBilling', 'PaymentMethod',
    'Churn'
    ]

# Imputation of missing values

# Encoding

# Discretizing

# Scaling

print(data.head())




# Solution below:


import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, KBinsDiscretizer

data = pd.read_csv('data.csv')

# Defining column types
id_col = ['customerID']
num_cols = ['SeniorCitizen', 'tenure', 'MonthlyCharges', 'TotalCharges']
cat_cols = [
    'gender', 'Partner', 'Dependents',
    'PhoneService', 'MultipleLines', 'InternetService',
    'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
    'TechSupport', 'StreamingTV', 'StreamingMovies',
    'Contract', 'PaperlessBilling', 'PaymentMethod',
    'Churn'
    ]

# Imputation of missing values
imputer = SimpleImputer(strategy='mean')
data[num_cols] = imputer.fit_transform(data[num_cols])

# Encoding
encoder = OneHotEncoder(handle_unknown='error', drop='first')
encoded = encoder.fit_transform(data[cat_cols])
encoded_df = pd.DataFrame(
    encoded.toarray(),
    columns=encoder.get_feature_names(cat_cols)
)
data = pd.concat([data[id_col+num_cols], encoded_df], axis=1)

# Discretizing
discretizer = KBinsDiscretizer(n_bins=3, encode='ordinal')
data[num_cols] = discretizer.fit_transform(data[num_cols])

# Scaling
scaler = StandardScaler()
data[num_cols] = scaler.fit_transform(data[num_cols])

print(data.head())



# make one ur self to understand preprocessing
