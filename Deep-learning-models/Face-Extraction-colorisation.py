import os
import cv2
import matplotlib.pyplot as plt
import mediapipe as mp

# Suppress TensorFlow Lite informational messages
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

# Set up the confidence level
MIN_CONFIDENCE_LEVEL = 0.5

def initialize_mediapipe():
    """
    Initializing mediapipe face detection sub-module
    """
    # Enable face detection
    mp_face_detection = mp.solutions.face_detection.FaceDetection(MIN_CONFIDENCE_LEVEL)
    return mp_face_detection

# Initialize MediaPipe
mp_face_detection = initialize_mediapipe()

def extract_face(image):
    # Convert the image from BGR to RGB format
    rgb_frame = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Detect faces using the RGB frame
    faces = mp_face_detection.process(rgb_frame)
    
    # We only expect one face, so process the first detection
    detection = faces.detections[0]
    # Extract bounding box
    bboxC = detection.location_data.relative_bounding_box
    ih, iw, _ = image.shape
    bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)
    x, y, w, h = bbox
    
    # Extract the face from the image
    face = image[y:y+h, x:x+w]
    
    return face
# Read Input Image
img = cv2.imread("person.jpeg")

# Extract face from the image
face = extract_face(img)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow((cv2.cvtColor(img, cv2.COLOR_BGR2RGB)))
plt.title('Person Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(face, cv2.COLOR_BGR2RGB))
plt.title('Extracted Face')
plt.axis('off')
plt.savefig("output/a")
plt.show()




# Lines 7–18: The function initializes the mediapipe face detection submodule to enable face detection with a minimum confidence level of 0.5.

# Lines 23–41: The function extracts a face from an image by converting it to RGB, detecting faces, retrieving the bounding box of the first detection, and then cropping the image to extract the face region based on the bounding box coordinates.





import os
import numpy as np
import cv2
import matplotlib.pyplot as plt
import mediapipe as mp

def colorize_face(image):
    # Write your code here

    return image

# Suppress TensorFlow Lite informational messages
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'

# Set up the confidence level
MIN_CONFIDENCE_LEVEL = 0.5

def initialize_mediapipe():
    """
    Initializing mediapipe face detection sub-module
    """
    # Enable face detection
    mp_face_detection = mp.solutions.face_detection.FaceDetection(MIN_CONFIDENCE_LEVEL)
    return mp_face_detection

# Initialize MediaPipe
mp_face_detection = initialize_mediapipe()

def extract_face(image):
    # Write your code here
    
    return image
# Read the input image
img = cv2.imread("person.jpeg")

# Extract face from the image
face = extract_face(img)
colorized_face = colorize_face(face)

# Colorize the extracted face
colorized_face = colorize_face(face)

# Display the original, extracted face, and colorized face images
plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Complete Person Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(face, cv2.COLOR_BGR2RGB))
plt.title('Extracted Face')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(colorized_face, cv2.COLOR_BGR2RGB))
plt.title('Colorized Face')
plt.axis('off')

plt.savefig("output/face_comparison.png")
plt.show()