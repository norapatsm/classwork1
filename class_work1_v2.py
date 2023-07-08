import cv2 as cv
import numpy as np


image = np.zeros((32, 32))


start_point = (0, 10)
end_point = (20, 30)
color = (255, 255, 255)
thickness = 1
image = cv.line(image, start_point, end_point, color, thickness)


cv.imwrite("./filter.png", image)


input_image = cv.imread("./kanti.jpg", cv.IMREAD_GRAYSCALE)
filter_image = cv.imread("./filter.png", cv.IMREAD_GRAYSCALE)


filter_sum = filter_image.sum()
filter_image = filter_image / filter_sum


output_image = cv.filter2D(src=input_image, ddepth=-1, kernel=filter_image)


cv.imwrite("./output_image.png", output_image)