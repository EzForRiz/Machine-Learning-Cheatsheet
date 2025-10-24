from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import numpy as np

movies_data = np.loadtxt('data.csv', delimiter=',')
X=movies_data[:,0:2]
y=movies_data[:,2]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
movie_classifier = MLPClassifier(hidden_layer_sizes=(2,), activation='logistic', learning_rate_init=0.04, solver='sgd', max_iter=1500, random_state=1)
movie_classifier.fit(X_train,y_train)
y_predicted = movie_classifier.predict(X_test)
y_true = y_test
acc=accuracy_score(y_true, y_predicted)
print(acc)