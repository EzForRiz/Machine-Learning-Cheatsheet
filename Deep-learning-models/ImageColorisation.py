preprocess_image()
load_model()
colorize_image()



# Import statements
import numpy as np
import cv2     # this is opencv for images and videos processing tools
import matplotlib.pyplot as plt

# Load the Model
net = cv2.dnn.readNetFromCaffe("colorization_deploy_v2.prototxt", "colorization_release_v2.caffemodel")
pts = np.load("pts_in_hull.npy")

# Load centers for ab channel quantization used for rebalancing.
class8 = net.getLayerId("class8_ab")
conv8 = net.getLayerId("conv8_313_rh")
pts = pts.transpose().reshape(2, 313, 1, 1)
net.getLayer(class8).blobs = [pts.astype("float32")]
net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]





# Code explanation

# Line 2: We use the cv2.dnn.readNetFromCaffe function to load the pretrained model, which typically consists of two files: a .prototxt defining the network architecture and a .caffemodel containing the learned weights.

# Line 3: We load the cluster centers for the ab color channels from the file pts_in_hull.npy using NumPy’s load function. These cluster centers are used to rebalance the model output, improving colorization quality.

# Line 6: We get the layer ID for the class8_ab layer in the network, which will be used to update the cluster centers.

# Line 7: We get the layer ID for the conv8_313_rh layer in the network, which will be used to update the rebalancing weights.

# Line 8: We transpose and reshape the cluster centers to match the expected input shape of the class8_ab layer.

# Transpose changes the order of dimensions.

# Reshape changes the array into the shape (2, 313, 1, 1).

# Line 9: We update the class8_ab layer with the cluster centers.

# astype("float32") ensures the data type is float32.

# Line 10: We update the conv8_313_rh layer with a rebalancing weight.

# np.full([1, 313], 2.606, dtype="float32") creates an array of shape (1, 313) filled with the value 2.606.







# Applying the Colorization Process

# So far, we have learned to install the required libraries and loaded the pretrained model and data. In this lesson, we will learn the steps needed for the colorization implementation:

# Reading and preprocessing the image: The input image is loaded and converted from the standard BGR color to the LAB color space. In LAB space, the L channel represents lightness, and the a and b channels represent color information. The image is resized to a specific size required by the model.

# Predicting colors: The L channel (grayscale information) is extracted and normalized before being fed into the model. The model processes this input to predict color information and the a and b channels.

# Combining and post-processing the image: The predicted a and b channels are resized to the original image size. These channels are combined with the original L channel to create a full LAB image. The LAB image is converted to the BGR color space to produce the final colorized image.

# Displaying the results: The original grayscale and colorized images are displayed side-by-side for comparison.



image = cv2.imread("house.jpg")

scaled = image.astype("float32") / 255.0



lab = cv2.cvtColor(scaled, cv2.COLOR_BGR2LAB)



resized = cv2.resize(lab, (224, 224))
L = cv2.split(resized)[0]
L -= 50



net.setInput(cv2.dnn.blobFromImage(L))
ab_channels = net.forward()[0, :, :, :].transpose((1, 2, 0))
ab_channels = cv2.resize(ab_channels, (image.shape[1], image.shape[0]))



LAB_channel = cv2.split(lab)[0]
colorized = np.concatenate((LAB_channel[:, :, np.newaxis], ab_channels), axis=2)



colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)
colorized = np.clip(colorized, 0, 1)
colorized = (255 * colorized).astype("uint8")




plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(colorized, cv2.COLOR_BGR2RGB))
plt.title('Colorized Image')
plt.axis('off')
plt.savefig("output/colorized_image.png")
plt.show()












# complete code:


# Import statements
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Load the Model
net = cv2.dnn.readNetFromCaffe("colorization_deploy_v2.prototxt", "colorization_release_v2.caffemodel")
pts = np.load("pts_in_hull.npy")

# Load centers for ab channel quantization used for rebalancing
class8 = net.getLayerId("class8_ab")
conv8 = net.getLayerId("conv8_313_rh")
pts = pts.transpose().reshape(2, 313, 1, 1)
net.getLayer(class8).blobs = [pts.astype("float32")]
net.getLayer(conv8).blobs = [np.full([1, 313], 2.606, dtype="float32")]

# Load the input image
image = cv2.imread("house.jpg")
scaled = image.astype("float32") / 255.0
lab = cv2.cvtColor(scaled, cv2.COLOR_BGR2LAB)

resized = cv2.resize(lab, (224, 224))
L = cv2.split(resized)[0]
L -= 50

net.setInput(cv2.dnn.blobFromImage(L))
ab_channels = net.forward()[0, :, :, :].transpose((1, 2, 0))
ab_channels = cv2.resize(ab_channels, (image.shape[1], image.shape[0]))
LAB_channel = cv2.split(lab)[0]
colorized = np.concatenate((LAB_channel[:, :, np.newaxis], ab_channels), axis=2)
colorized = cv2.cvtColor(colorized, cv2.COLOR_LAB2BGR)
colorized = np.clip(colorized, 0, 1)
colorized = (255 * colorized).astype("uint8")


plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow((cv2.cvtColor(image, cv2.COLOR_BGR2RGB)))
plt.title('Grayscale Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(colorized, cv2.COLOR_BGR2RGB))
plt.title('Colorized Image')
plt.axis('off')
plt.savefig("output/a")
plt.show()





#explanation:

# Lines 7–8: Load a pretrained colorization neural network from Caffe model files into net and load the color cluster centers from a NumPy file into pts.

# Lines 11–15: Assign quantization centers to the class8_ab layer and rebalance the weights to the conv8_313_rh layer of the pretrained colorization neural network.

# Lines 18–20: The code will read an image, scale its pixel values to the range [0, 1], and convert the image from BGR to LAB color space.

# Lines 22–24: Resize the LAB image to 224x224 pixels, extract the L channel, and normalize it by subtracting 50.

# Lines 26–33: The code processes the L channel through the neural network to obtain the ab color channels, resize them to the original image size, and combine them with the original L channel converts the LAB image back to BGR, and adjusts the pixel values to the 0-255 range.

# Lines 36–40: Set up a figure with two subplots, display the original image converted to RGB in the first subplot with the title Grayscale Image, and turn off the axis.

# Lines 42–47: Set up the second subplot, display the colorized image converted to RGB, set the title to Colorized Image, turn off the axis, save the figure as output/a, and show the plot.

