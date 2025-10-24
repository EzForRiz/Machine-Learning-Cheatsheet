import numpy as np

# Code for predict() showing a single forward pass
def predict_label(x1, x2, w1, w2, w0):
  # Calcualte the value correcponding to the x and y values and the weights.
  val = x1*w1 + x2*w2 + 1*w0
  if val < 0:
    return 1
  else:
    return 0
    
# Read data from csv file. The data has a total of 100 points.
movies_data = np.loadtxt('data.csv', delimiter=',')

# Split the data into train and test sets.
train_set = movies_data[:80]
test_set = movies_data[80:]

# Separating the labels and x, y values
test_values = []
test_labels = []

train_values = []
train_labels = []

for i in test_set:
  test_values.append([i[0], i[1]])
  test_labels.append(i[2])
  
for i in train_set:
  train_values.append([i[0], i[1]])
  train_labels.append(i[2])
  
predicted_labels_train = []

for i in train_values:
  prediction = predict_label(i[0], i[1], -5.7, -1.3, 35)
  predicted_labels_train.append(prediction)

correct_predictions_train = 0
for i in range(len(predicted_labels_train)):
  if predicted_labels_train[i] == train_labels[i]:
    correct_predictions_train += 1

train_accuracy = correct_predictions_train/len(train_labels) *100
print('Training accuracy =', train_accuracy)

# Write your code below to test accuracy on test_values