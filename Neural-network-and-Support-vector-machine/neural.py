# # Neural Network


# # Although sklearn focuses on traditional Machine Learning, it still provides some methods to build a simple forward neural network. In this lesson, we give a simple introduction about how to use it.


# # Modeling with MLPClassifier


# Let’s skip data loading and splitting, and create an MLPClassifier object from the neural_network module. The MLP stands for a multilayer perceptron. As you can see, the NN requires a lot of parameters. If you are familiar with Deep Learning, you may know that fine-tuning is a very important and time-consuming task in a neural network.



# # Following are some parameters we set below:

# batch_size: In general, a neural network uses stochastic optimizers, so every time it uses a mini-batch sample to train.
# solver: Optimizer is another big topic in Deep Learning, here we just choose the simplest one.
# shuffle: Whether to shuffle samples in each iteration, this can increase the randomness of training and improve the training efficiency.
# tol: Convergence condition, which means the change of loss between two iterations is less than a certain threshold.
# max_iter: The maximum number of iteration.
# learning_rate_init: Learning rate is the most important hyperparameter in Deep Learning, which is also a very big topic. When solver="sgd", you can choose the learning rate schedule for parameter updates. The default setting is constant. Here we only set learning_rate_init, which means the learning rate would always be 0.001 during the training.
# The code below shows how to create a Neural Network with these parameters. The complete code would be shown at the end of this lesson.



from sklearn.neural_network import MLPClassifier

nn = MLPClassifier(batch_size=32,
                   hidden_layer_sizes=(64, 32),
                   solver="sgd",
                   shuffle=True,
                   tol=1e-3,
                   max_iter=300,
                   learning_rate_init=0.001)



# How to fine-tune a network:
# batch_size cannot be too small, otherwise, the training speed of the model will be adversely affected. It should not be too large, or it will affect the performance of the model. If you don’t know what is the suitable number is, 32, 64 or 128 could be your starting point.

# hidden_layer_sizes cannot be too small, otherwise, the model learning ability is insufficient. It can’t be too big, as it will lead to overfitting.

# learning_rate is the most important hyperparameter in deep learning. If the learning rate is too small, the training speed of the model will be affected. If the learning rate is too large, the training is unstable and easy to not converge. 0.001 or 0.00001 are your first choices, then you can fine-tune it according to the performance of your model.

# solver is also important. Different solvers have different effects on different kinds of tasks. sgd is the most commonly used solver. However, there are many solvers and you should pick them carefully based on your task.




# After we fit the model, let’s see the performance of this model. If you are already reading some papers or articles about Deep Learning, you may often see a similar chart, that is, as the number of training iteration increases, the loss decreases. In sklearn, the loss of each iteration is stored in the attribution of a model, loss_curve_.


import matplotlib.pyplot as plt

fig, axe = plt.subplots()
## nn is the model we train
axe.plot(range(len(nn.loss_curve_)), nn.loss_curve_)
axe.set_xlabel("iteration")
axe.set_ylabel("loss")








import sklearn.datasets as datasets
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import sklearn.metrics as metrics
import matplotlib.pyplot as plt

X, y = datasets.make_classification(n_samples=1000,
                                    n_features=30,
                                    random_state=10)

print("the shape of X is {}".format(X.shape))
print("the shape of y is {}".format(y.shape))

train_x, test_x, train_y, test_y = train_test_split(X,
                                                    y,
                                                    test_size=0.2,
                                                    random_state=42)

nn = MLPClassifier(batch_size=32,
                   hidden_layer_sizes=(64, 32),
                   solver="sgd",
                   shuffle=True,
                   tol=1e-3,
                   max_iter=300,
                   learning_rate_init=0.001)

nn.fit(train_x, train_y)

fig, axe = plt.subplots()
axe.plot(range(len(nn.loss_curve_)), nn.loss_curve_)
axe.set_xlabel("iteration")
axe.set_ylabel("loss")
fig.savefig("output/img.png", dpi = 300)
plt.close(fig)