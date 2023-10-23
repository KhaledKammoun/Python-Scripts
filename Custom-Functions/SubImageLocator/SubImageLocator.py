import cv2
import numpy as np
from tensorflow.keras.applications import VGG16
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
from sklearn.metrics.pairwise import cosine_similarity

# Load a pre-trained VGG16 model
model = VGG16(weights='imagenet', include_top=False)

# Load the larger image and the sub-image
larger_image = cv2.imread('image.jpg')
sub_image = cv2.imread('smaller_image.jpg')

# Resize the sub-image to match the dimensions of the VGG16 model
target_size = (224, 224)
sub_image = cv2.resize(sub_image, target_size)

# Convert the larger image to the format required by the VGG16 model
larger_image = cv2.resize(larger_image, target_size)
larger_image = np.expand_dims(larger_image, axis=0)
larger_image = preprocess_input(larger_image)

# Convert the sub-image to the format required by the VGG16 model
sub_image = np.expand_dims(sub_image, axis=0)
sub_image = preprocess_input(sub_image)

# Use the VGG16 model to predict
larger_image_features = model.predict(larger_image)
sub_image_features = model.predict(sub_image)

# Reshape the feature arrays to 2D
larger_image_features = larger_image_features.reshape(1, -1)
sub_image_features = sub_image_features.reshape(1, -1)

# Compare features using cosine similarity
similarity = cosine_similarity(larger_image_features, sub_image_features)

# Set a similarity threshold to decide if it's a match
similarity_threshold = 0.9

if similarity[0][0] >= similarity_threshold:
    print("Match found.")
else:
    print("No match found.")
