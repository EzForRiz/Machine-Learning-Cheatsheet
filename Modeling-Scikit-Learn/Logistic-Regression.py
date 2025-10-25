# Logistic Regression

# Classification
# Thus far we've learned about several linear regression models and implemented them with scikit-learn. The logistic regression model, despite its name, is actually a linear model for classification. It is called logistic regression because it performs regression on logits, which then allows us to classify the data based on model probability predictions.

# For a more detailed explanation of logistic regression, check out the Intro to Deep Learning section of this course, which implements logistic regression via a single layer perceptron model in TensorFlow.

# We implement logistic regression with the LogisticRegression object (part of the linear_model module). The default setting for LogisticRegression is binary classification, i.e. classifying data observations that are labeled with either a 0 or 1.


# predefined dataset
print('Data shape: {}\n'.format(data.shape))
# Binary labels
print('Labels:\n{}\n'.format(repr(labels)))

from sklearn import linear_model
reg = linear_model.LogisticRegression()
reg.fit(data, labels)

new_data = np.array([
  [  0.3,  0.5, -1.2,  1.4],
  [ -1.3,  1.8, -0.6, -8.2]])
print('Prediction classes: {}\n'.format(
  repr(reg.predict(new_data))))



# The code above created a logistic regression model from a labeled dataset. The model predicts 1 and 0, respectively, as the labels for the observations in new_data.

# For multiclass classification, i.e. when there are more than two labels, we initialize the LogisticRegression object with the multi_class keyword argument. The default value is 'ovr', which signifies a One-Vs-Rest strategy. In multiclass classification, we want to use the 'multinomial' strategy.

# The code below demonstrates multiclass classification. Note that to use the 'multinomial' strategy, we need to choose a proper solver (see below for details on solvers). In this case, we choose 'lbfgs'.



# predefined dataset
print('Data shape: {}\n'.format(data.shape))
# Multiclass labels
print('Labels:\n{}\n'.format(repr(labels)))

from sklearn import linear_model
reg = linear_model.LogisticRegression(
  solver='lbfgs',
  multi_class='multinomial', max_iter=200)
reg.fit(data, labels)

new_data = np.array([
  [ 1.8, -0.5, 6.2, 1.4],
  [ 3.3,  0.8, 0.1, 2.5]])
print('Prediction classes: {}\n'.format(
  repr(reg.predict(new_data))))




# cross validated model

from sklearn import linear_model
reg = linear_model.LogisticRegressionCV(
  solver='multinomial', max_iter=1000)



def multiclass_lr(data, labels, max_iter):
  reg = linear_model.LogisticRegression(solver='lbfgs',
    max_iter=max_iter, multi_class='multinomial')
  reg.fit(data, labels)
  return reg

