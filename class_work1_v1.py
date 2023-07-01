import numpy as np
import cv2 as cv


image_width = 800
image_height = 600
background_color = (255, 255, 255)  
line_color = (0, 0, 0)  
image = np.full((image_height, image_width, 3), background_color, dtype=np.uint8)


start_point = (100, 300)  
end_point = (700, 300)  
line_thickness = 2


slope = (end_point[1] - start_point[1]) / (end_point[0] - start_point[0])

e
angle = np.arctan(slope)


line_length = int(np.sqrt((end_point[0] - start_point[0]) ** 2 + (end_point[1] - start_point[1]) ** 2))


for t in range(line_length):
    x = int(start_point[0] + t * np.cos(angle))
    y = int(start_point[1] + t * np.sin(angle))
    image[y, x] = line_color


image_path = "kanti.jpg" 
original_image = cv.imread(image_path)


convolved_image = cv.filter2D(original_image, -1, image)


cv.imshow("Convolved Image", convolved_image)
cv.waitKey(0)
cv.destroyAllWindows()