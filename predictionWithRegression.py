# In this code, we will fit a linear regression model from scikit-learn to our data.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# First, we load the data
data = np.loadtxt('data.csv', delimiter=',')

# Then, we extract the x and y values
x = data[:, 0]
y = data[:, 1]

# Then, we fit a linear regression model
model = LinearRegression()
model.fit(x.reshape(-1, 1), y)

# Make a prediction on a new previously unseen value of number of goals
x_test=np.array(75)
predictions = model.predict(x_test.reshape(1, -1))

print('Number of matches won, y:',predictions)
# Extracting the coefficient of x and the intercept from the model
b0 = model.intercept_
b1 = model.coef_[0]

print('Coefficients of the line:',b0,b1)



# make the code below a seperate file code called data.csv run...
# 47,19
# 53,30
# 22,7
# 18,18
# 19,4
# 21,12
# 15,11
# 25,10
# 10,9
# 26,15
# 11,9
# 22,11
# 17,19
# 55,30
# 70,41
# 16,3
# 35,14
# 60,35
# 30,14
47,25