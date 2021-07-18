import cv2
import minkowski_geodesic_construction
import schwarzschild_geodesic_construction
import time
import matplotlib.pyplot as plt
from shutil import copyfile
import warnings
import conversion_formulas

# Numpy throws a RuntimeWarning when 0 is divided by 0 in the origin. We simply skip this value.
warnings.filterwarnings("ignore", category=RuntimeWarning)

test_input = 'input_transformable_images//100x100_car.jpg'
test_output = 'output_transformable_images//100x100_car.jpg'


def create_transformed_image(input_path=test_input, output_path=test_output):

    copyfile(test_input, test_output)
    timeout = time.time() + 80  # 5 minutes from now

    input_image = cv2.imread(input_path)
    output_image = cv2.imread(output_path)

    x = input_image.shape[0]
    y = input_image.shape[1]

    dt = 0.005
    t_end = 20

    # turn output image white
    for i in range(0, x):
        for j in range(0, y):
            output_image[i, j] = [255, 255, 255]

    cv2.imwrite(output_path, output_image)

    for i in range(0, x):
        for j in range(0, y):
            R, G, B = input_image[i][j]
            try:
                r, theta, phi = minkowski_geodesic_construction.create_specified_geodesic(
                    i - x / 2.0, j - y / 2.0, -10, dt, t_end)
                pixel_x_end_float, pixel_y_end_float, pixel_z_end_float = \
                    conversion_formulas.spherical_to_cartesian(r[-1], theta[-1], phi[-1])
            except ZeroDivisionError:
                continue
            pixel_x_end_int = round(pixel_x_end_float + x/2)
            pixel_y_end_int = round(pixel_y_end_float + y/2)
            output_image[pixel_x_end_int, pixel_y_end_int, 0] = R
            output_image[pixel_x_end_int, pixel_y_end_int, 1] = G
            output_image[pixel_x_end_int, pixel_y_end_int, 2] = B
            if time.time() > timeout:
                break
            cv2.imshow('image', output_image)
            cv2.waitKey(1)

    cv2.imwrite(output_path, output_image)
