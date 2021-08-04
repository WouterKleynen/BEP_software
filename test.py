# importing cv2
import cv2
import os.path

path = 'output_transformable_images//100x100_car_transformed_r_s=0.4_Z_end=20_made_into_sphere.jpg'

output_image = cv2.imread(path)
extension = os.path.splitext(path)[1]
new_path = path.replace(str(extension), '_sphered' + str(extension))
# path

# Reading an image in default mode
image = cv2.imread(path)

# Window name in which image is displayed
window_name = 'Image'

# Center coordinates
center_coordinates = (50, 50)

# Radius of circle
radius = 15

# Blue color in BGR
color = (0, 0, 0)

# Line thickness of 2 px
thickness = -1

# Using cv2.circle() method
# Draw a circle with blue line borders of thickness of 2 px
image = cv2.circle(image, center_coordinates, radius, color, thickness)

# Displaying the image
cv2.imshow(window_name, image)
cv2.waitKey(0)
cv2.imwrite(new_path, image)