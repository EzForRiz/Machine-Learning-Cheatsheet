# Your challenge as an ML engineer is to achieve maximum accuracy, given the challenging dataset. Currently, the model has one hidden layer with 2 neurons in it, a sigmoid activation function given by logistic, learning rate of 0.04, and maximum iterations over the dataset as 1500.

# At the moment, with the given parametric values, the neural network does not learn to classify the dataset with 100% accuracy on the test set, as you’ll see when you click the “Run” button.

# Your challenge is to hit 100% accuracy (output shall be 1.0 when you click the “Run" button) by using the minimum number of hidden layer neurons and minimum iterations.



from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

data = np.loadtxt('data.csv', delimiter=',')
X=data[:,0:2]
y=data[:,2]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
classifier = MLPClassifier(hidden_layer_sizes=(2,), activation='logistic', learning_rate_init=0.04, solver='sgd', max_iter=1500, random_state=1)

classifier.fit(X_train,y_train)
y_predicted = classifier.predict(X_test)
y_true = y_test
acc=accuracy_score(y_true, y_predicted)
print(acc)























# solution

# tanh handles non-linear decision boundaries more effectively than logistic, which is why it can learn the complex circular decision boundary between your two classes better.
# If you look closely at the plot of the dataset, you'll see that we really only need a traingular decision boundary to separate the inner and outer circle, hence only 3 hidden layer neurons suffice
# With tanh as activation function and 3 hidden layer layer neurons, only 50 iterations at max are required to learn the dataset with 100% accuracy


# classifier = MLPClassifier(hidden_layer_sizes=(3,), activation='tanh', learning_rate_init=0.2, solver='sgd', max_iter=50, random_state=1)

