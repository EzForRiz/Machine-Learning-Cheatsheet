# # Cross-Validation

# # Additional evaluation datasets 
# Sometimes, it's not enough to just have a single testing set for model evaluation. Having additional sets of data for evaluation gives us a more accurate measurement of how good the model is for the original dataset.

# If the original dataset is big enough, we can actually split it into three subsets: training, testing, and validation. The validation set is about the same size as the testing set, and it is used for evaluating the model after training. The testing set is then used for final evaluation once the model is done training and tuning.

# However, partitioning the original dataset into three distinct sets will cut into the size of the training set. This can reduce the performance of the model if our original dataset is not large enough. A solution to this problem is cross-validation (CV).

# Cross-validation creates synthetic validation sets by partitioning the training set into multiple smaller subsets. One of the most common algorithms for cross-validation, K-Fold CV, partitions the training set into k approximately equal sized subsets (referred to as folds). There are k "rounds" of the algorithm, and each "round" chooses one of the k subsets for the validation set (a different subset is chosen each round), while the remaining k - 1 subsets are aggregated into the round's training set and used to train the model.





# # Scored cross-validation 
# In scikit-learn, we can easily implement K-Fold cross-validation with the cross_val_score function (also part of the model_selection module). The function returns an array containing the evaluation score for each round.

# The code below demonstrates K-Fold CV with 3 folds for classification. The evaluation metric is classification accuracy.

# Python 3.5


from sklearn import linear_model
from sklearn.model_selection import cross_val_score
# We can skip max_iter argument here, but it will produce a
# ConvergenceWarning. Therefore we explicity give a bigger value to
# avoid the warning.
clf = linear_model.LogisticRegression(max_iter=3000)
# Predefined data and labels
cv_score = cross_val_score(clf, data, labels, cv=3)  # k = 3

print('{}\n'.format(repr(cv_score)))



from sklearn import linear_model
from sklearn.model_selection import cross_val_score
reg = linear_model.LinearRegression()
# Predefined data and labels
cv_score = cross_val_score(reg, data, labels, cv=4)  # k = 4

print('{}\n'.format(repr(cv_score)))




