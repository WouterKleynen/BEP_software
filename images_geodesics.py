import cv2
import numpy as np
import minkowski_geodesics_plot as mgp
import time

timeout = time.time() + 30   # 5 minutes from now

input_path = 'C://Users//woute//Downloads//rainbow-sq_input.jpg'
output_path = 'C://Users//woute//Downloads//rainbow-sq_output.jpg'

input_image = cv2.imread(input_path)
output_image = cv2.imread(output_path)

x = output_image.shape[0]
y = output_image.shape[1]

dt = 0.005
t_end = 20

# turn output image white
for i in range(1, x):
    for j in range(1, y):
        output_image[i, j] = [255, 255, 255]

cv2.imwrite(output_path, output_image)


for i in range(1, x):
    for j in range(1, y):
        R, G, B = input_image[i][j]
        pixel_x_end_float, pixel_y_end_float  = mgp.create_specific_minkowski_geodesic(i, j, dt, t_end)
        pixel_x_end_int = round(pixel_x_end_float)
        pixel_y_end_int = round(pixel_y_end_float)
        output_image[pixel_x_end_int, pixel_y_end_int, 0] = R
        output_image[pixel_x_end_int, pixel_y_end_int, 1] = G
        output_image[pixel_x_end_int, pixel_y_end_int, 2] = B
        if time.time() > timeout:
            break
        cv2.imshow('image', output_image)
        cv2.waitKey(1)

cv2.imwrite(output_path, output_image)







