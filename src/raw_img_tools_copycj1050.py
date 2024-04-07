      
    
import numpy as np
import matplotlib.pyplot as plt

# Load the image from the npy file
image = np.load('000_1050.npy')

# Get the dimensions of the image
height, width = image.shape

# Define the fraction of the image you want to keep (e.g., 0.5 for bottom half)
fraction = 0.3

# Calculate the number of rows to keep
rows_to_keep = int(height * fraction)

# Take the bottom part of the image
bottom_part = image[height - rows_to_keep :, :]

# Define the range of rows for the horizontal middle wedge
middle_wedge_height = 700  # Adjust this value as needed
middle_wedge_start = (rows_to_keep - middle_wedge_height) // 5
middle_wedge_end = middle_wedge_start + middle_wedge_height

# Select the horizontal middle wedge from the bottom part of the image
horizontal_middle_wedge = bottom_part[middle_wedge_start:middle_wedge_end, :]

# Display the horizontal middle wedge
plt.imshow(horizontal_middle_wedge)
plt.axis('off')
plt.show()
