import cv2
import minkowski_geodesic_construction
import schwarzschild_geodesic_construction
import time
from shutil import copyfile
import warnings
import conversion_formulas

# Numpy throws a RuntimeWarning when 0 is divided by 0 in the origin. We simply skip this value.
warnings.filterwarnings("ignore", category=RuntimeWarning)

test_input = 'input_transformable_images//100x100_car.jpg'
test_output = 'output_transformable_images//100x100_car.jpg'


def open_input_and_output_image(input_path=test_input, output_path=test_output):
    copyfile(test_input, test_output)

    input_image = cv2.imread(input_path)
    output_image = cv2.imread(output_path)
    return input_image, output_image


def whiten_output_image(output_image, output_path=test_output):
    x = output_image.shape[0]
    y = output_image.shape[1]
    for i in range(0, x):
        for j in range(0, y):
            output_image[i, j] = [255, 255, 255]
    cv2.imwrite(output_path, output_image)
    return x, y, output_image


def create_transformed_minkowski_image(dt, t_end, input_path=test_input, output_path=test_output):
    input_image, output_image = open_input_and_output_image()
    x, y, output_image = whiten_output_image(output_image)
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
            cv2.imshow('image', output_image)
            cv2.waitKey(1)

    cv2.imwrite(output_path, output_image)

# def create_transformed_schwarzschild_image(dt, t_end, input_path=test_input, output_path=test_output):
