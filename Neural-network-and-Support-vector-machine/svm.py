# # # Support Vector Machine
# # In this lesson, we introduce a very popular model, Support Vector Machine.



# # What is Support Vector Machine?
# Support Vector Machine (SVM) is widely used for classification (SVM also supports regression tasks). In general, SVM finds a hyperplane that separates data points with the greatest amount of margin.

# The core idea of SVM is to find a maximum marginal hyperplane that divides the dataset. For a data set with two classes, if they’re linearly separable, then you can find an infinite number of hyperplanes to separate them. The SVM finds only one of these hyperplanes, which is the maximum marginal hyperplane.



# SVM is a method with a rich theoretical basis and very beautiful mathematical definition and derivation. But we’re not going to cover that in this course; if you’re interested in this topic, you can refer to the wikipedia.



# Difference between SVM and logistic regression. 


# You may have already learned logistic regression before. SVM and logistic regression are all classifiers, so what are the differences between them?




# SVM is a geometrical method. Logistic regression is a statistical approach.
# The risk of overfitting is less in SVM.
# SVM works well on unstructured and semi-structured data.
# Logistic regression works well on large scale data sets.
# SVM’s performance is pretty good.
# Theoretically, the SVM only needs to know a few points, so it consumes very little memory.




from sklearn.svm import LinearSVC

svm = LinearSVC(dual=False)
# train_x and train_y are training samples and labels.
svm.fit(train_x, train_y)









import sklearn.datasets as datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
import sklearn.metrics as metrics
import matplotlib.pyplot as plt
from sklearn.svm import SVC
import numpy as np

cancer = datasets.load_breast_cancer()
print("The data shape of breast cancer is {}".format(cancer.data.shape))
print("There are {} classes in this dataset".format(cancer.target_names.size))

train_x, test_x, train_y, test_y = train_test_split(cancer.data,
                                                    cancer.target,
                                                    test_size=0.2,
                                                    random_state=42)

print("The first five samples {}".format(train_x[:5]))
print("The first five targets {}".format(train_y[:5]))

svm = LinearSVC(dual=False)
svm.fit(train_x, train_y)

pred_y = svm.predict(test_x)
print("The first five prediction {}".format(pred_y[:5]))
print("The real first five labels {}".format(test_y[:5]))

cm = metrics.confusion_matrix(test_y, pred_y)
print(cm)



# Polynomial kernel = k(xi,xj) = (xi *xj +1)^d


#Gaussian kernel: 
#   k(x, y) = exp(- ||x - y||^2 / (2 * sigma^2))

# Gaussian radial basis:
# k(x_i, x_j) = exp(-gamma * ||x_i - x_j||^2)





# First, let’s create a data set that is not linearly separable. make_circle is the function we used. As you can see from the plot below, the yellow points are at the center of the whole plot and the purple points go around the outside. Such data is not linearly separable.


import sklearn.metrics as metrics
import matplotlib.pyplot as plt

X, y = datasets.make_circles(200, noise=0.2, factor=0.1, random_state=12)




# Creating an SVM with a kernel is very simple. Just create an SVC object with the kernel parameter. In this demo, we choose rbf as our kernel function.

from sklearn.svm import SVC

svc = SVC(kernel='rbf')
svc.fit(X, y)


import sklearn.datasets as datasets
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
import sklearn.metrics as metrics
import matplotlib.pyplot as plt
from sklearn.svm import SVC
import numpy as np

X, y = datasets.make_circles(200, noise=0.2, factor=0.1, random_state=12)

fig, axe = plt.subplots()
axe.scatter(X[:, 0], X[:, 1], c=y)

svc = SVC(kernel='rbf')
svc.fit(X, y)

xlim = axe.get_xlim()
ylim = axe.get_ylim()

xlin = np.linspace(xlim[0], xlim[1], 30)
ylin = np.linspace(ylim[0], ylim[1], 30)
Yc, Xc = np.meshgrid(ylin, xlin)
xy = np.vstack([Xc.ravel(), Yc.ravel()]).T
P = svc.decision_function(xy).reshape(Xc.shape)
axe.contour(Xc, Yc, P, levels=[0], colors='r')

fig.savefig("output/img.png", dpi = 300)
plot.close(fig)