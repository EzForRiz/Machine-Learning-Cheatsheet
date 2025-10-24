# Support Vector Machines (SVMs) are a powerful supervised learning algorithm, particularly used for classification tasks. While a multilayer perceptron (MLP) is a neural network that adjusts its weights to minimize the error, SVM works by finding the optimal hyperplane that separates data points of different classes with the maximum margin. Unlike MLP, SVM focuses on maximizing this margin and is particularly effective in high-dimensional spaces. It can also handle non-linearly separable data using kernel functions, making SVM a strong alternative to MLPs.




# Importing required libraries
import numpy as np
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

def prepare_data():
  # Reading image files using Pillow
  img_list = []
  for i in range(1, 301):
      img = Image.open('./gray_g'+str(i)+'.png').convert('L')
      img_list.append(img)
  
  # Reshaping the image data to a 1-dimensional array
  img_data = np.array([np.array(img).flatten() for img in img_list])
  
  # The first 100 images have tag 0, the next 100 images have tag 1, and the next 100 images have tag 2
  tag = np.concatenate((np.zeros(100), np.ones(100), np.ones(100)*2))
  
  return img_data, tag

def get_model():
  # Return the selected model
  return SVC()
  
def train_model(model, data, tags):
  
  # Training an MLP classifier
  model.fit(data, tags)
  
  return model
  
def get_predictions(model, test_img):
  
  # Getting predictions
  predictions = model.predict(test_img)
  
  return predictions
  
def evaluate_predictions(predicted_tags, actual_tags):
  
  # Computing accuracy of the predictions
  accuracy = accuracy_score(actual_tags, predicted_tags)
  
  print("Prediction accuracy:", accuracy)


def main():

  # Data
  img_data, tags = prepare_data()
  
  # Splitting data into train and test portions
  train_img, test_img, train_tags, test_tags = train_test_split(img_data, tags, test_size=0.2)
    
  # Model
  model = get_model()
  
  # Training
  trained_model = train_model(model, train_img, train_tags)
  
  # Prediction
  predictions = get_predictions(trained_model, test_img)
  
  # Evaluation
  evaluate_predictions(predictions, test_tags)
  
main()