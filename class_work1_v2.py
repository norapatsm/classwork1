import cv2 as cv
import numpy as np

# Creating a blank image
image = np.zeros((32, 32))

# Drawing a line on the image
start_point = (0, 10)
end_point = (20, 30)
color = (255, 255, 255)
thickness = 1
image = cv.line(image, start_point, end_point, color, thickness)

# Saving the image
cv.imwrite("./filter.png", image)

# Reading the input image and the filter image
input_image = cv.imread("./kanti.jpg", cv.IMREAD_GRAYSCALE)
filter_image = cv.imread("./filter.png", cv.IMREAD_GRAYSCALE)

# Normalizing the filter image
filter_sum = filter_image.sum()
filter_image = filter_image / filter_sum

# Applying the filter
output_image = cv.filter2D(src=input_image, ddepth=-1, kernel=filter_image)

# Saving the output image
cv.imwrite("./ANC.png", output_image)