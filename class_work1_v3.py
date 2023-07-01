import numpy as np
import cv2 as cv

# Create a blank image
image_width = 32
image_height = 32
line_color = (255, 255, 255)  # White color in RGB
image = np.zeros((image_height, image_width, 3), dtype=np.uint8)

# Define the line parameters
start_point = (0, 10)  # Starting point of the line (x, y)
end_point = (20, 30)  # Ending point of the line (x, y)
line_thickness = 1

# Draw the line on the image
cv.line(image, start_point, end_point, line_color, line_thickness)


cv.imwrite("line_filter.png", image)


image_path = "kanti.jpg"
original_image = cv.imread(image_path, cv.IMREAD_GRAYSCALE)


line_filter_image = cv.imread("line_filter.png", cv.IMREAD_GRAYSCALE)


line_filter_sum = line_filter_image.sum()
line_filter_image = line_filter_image / line_filter_sum


output_image = cv.filter2D(src=original_image, ddepth=-1, kernel=line_filter_image)

# Saving the output image
cv.imwrite("output_image.png", output_image)
