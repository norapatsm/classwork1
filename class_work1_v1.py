import numpy as np
import cv2 as cv

# Create a black image with a white background
image_width = 800
image_height = 600
background_color = (255, 255, 255)  # White color in RGB
line_color = (0, 0, 0)  # Black color in RGB
image = np.full((image_height, image_width, 3), background_color, dtype=np.uint8)

# Define the line parameters
start_point = (100, 300)  # Starting point of the line (x, y)
end_point = (700, 300)  # Ending point of the line (x, y)
line_thickness = 2

# Calculate the line slope
slope = (end_point[1] - start_point[1]) / (end_point[0] - start_point[0])

# Calculate the line angle
angle = np.arctan(slope)

# Calculate the line length
line_length = int(np.sqrt((end_point[0] - start_point[0]) ** 2 + (end_point[1] - start_point[1]) ** 2))

# Draw the line pixel by pixel
for t in range(line_length):
    x = int(start_point[0] + t * np.cos(angle))
    y = int(start_point[1] + t * np.sin(angle))
    image[y, x] = line_color

# Load an image to convolve with the line
image_path = "kanti.jpg" 
original_image = cv.imread(image_path)

# Perform convolution between the line and the image
convolved_image = cv.filter2D(original_image, -1, image)

# Display the convolved image
cv.imshow("Convolved Image", convolved_image)
cv.waitKey(0)
cv.destroyAllWindows()