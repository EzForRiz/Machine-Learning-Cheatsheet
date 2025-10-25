# Applying CV to Decision Trees
# Apply K-Fold cross-validation to decision trees.

# Chapter Goals:
# Apply K-Fold cross-validation to a decision tree
# A. Decision tree depth
# We've previously discussed cross-validation for tuning hyperparameters such as the α value for regularized regression. For decision trees, we can tune the tree's maximum depth hyperparameter (max_depth) by using K-Fold cross-validation.

# K-Fold cross-validation gives an accurate measurement of how good the decision tree is for the dataset. We can use K-Fold cross-validation with different values of the max_depth hyperparameter and see which one gives the best cross-validation scores.

# The code below demonstrates how to apply K-Fold CV to tune a decision tree's maximum depth. It uses the cv_decision_tree function that you will implement later in this chapter.



is_clf = True  # for classification
for depth in range(3, 8):
  # Predefined data and labels
  scores = cv_decision_tree(
    is_clf, data, labels, depth, 5)  # k = 5
  mean = scores.mean()  # Mean acc across folds
  std_2 = 2 * scores.std()  # 2 std devs
  print('95% C.I. for depth {}: {} +/- {:.2f}\n'.format(
    depth, mean, std_2))



def cv_decision_tree(is_clf, data, labels,
                     max_depth, cv):
  if is_clf:
    d_tree = tree.DecisionTreeClassifier(max_depth=max_depth)
  else:
    d_tree = tree.DecisionTreeRegressor(max_depth=max_depth)
  scores = cross_val_score(d_tree, data, labels, cv=cv)
  return scores
