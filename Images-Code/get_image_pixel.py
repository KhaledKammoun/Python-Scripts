import cv2

# Read the image
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)  # Read as grayscale

# Define the scale factor
scale_factor = 0.05  # Adjust this value to change the scale

# Resize the image
resized_image = cv2.resize(image, None, fx=scale_factor, fy=scale_factor)

# Get the dimensions of the resized image
height, width = resized_image.shape

# Initialize an empty matrix to store pixel intensities
intensity_matrix = []

# Define a threshold to determine black pixels
threshold = 100  # Adjust this as needed

# Iterate through each pixel and store its intensity values in the matrix
for y in range(height):
    row = []
    for x in range(width):
        intensity = resized_image[y, x]
        if intensity < threshold:
            row.append('.')
        else:
            row.append(' ')
    print(''.join(row))  # Print the row as a string
    intensity_matrix.append(row)

# # Print the intensity matrix
# for row in intensity_matrix:
#     print(row)
