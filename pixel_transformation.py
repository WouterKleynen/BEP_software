import cv2
import minkowski_geodesic_construction
import schwarzschild_geodesic_construction
import time
from shutil import copyfile
import warnings
import conversion_formulas

# Numpy throws a RuntimeWarning when 0 is divided by 0 in the origin. We simply skip this value.
warnings.filterwarnings("ignore", category=RuntimeWarning)

test_input = 'input_transformable_images//100x100_cathy.jpeg'
test_output = 'output_transformable_images//100x100_cathy.jpeg'

x_start_series_schwarzschild = []
y_start_series_schwarzschild = []
x_end_series_schwarzschild = []
y_end_series_schwarzschild = []


def open_input_and_output_image(input_path=test_input, output_path=test_output):
    copyfile(test_input, test_output)

    input_image = cv2.imread(input_path)
    output_image = cv2.imread(output_path)
    return input_image, output_image


def blacken_output_image(output_image, output_path=test_output):
    x = output_image.shape[0]
    y = output_image.shape[1]
    for i in range(0, x):
        for j in range(0, y):
            output_image[i, j] = [0, 0, 0]
    cv2.imwrite(output_path, output_image)
    return x, y, output_image


def create_transformed_minkowski_image(dt, t_end, input_path=test_input, output_path=test_output):
    input_image, output_image = open_input_and_output_image()
    x_size, y_size, output_image = blacken_output_image(output_image)
    for x in range(0, x_size):
        for y in range(0, y_size):
            R, G, B = input_image[x][y]
            x_start = -x_size / 2 + x
            y_start = y_size / 2 - y
            print(x_start, y_start)
            z_start = -10
            try:
                r, theta, phi = minkowski_geodesic_construction.create_specified_geodesic(
                    x_start, y_start, z_start, dt, t_end)
                position_x_end_transposed, position_y_end_transposed, position_z_end_transposed = \
                    conversion_formulas.spherical_to_cartesian(r[-1], theta[-1], phi[-1])
                position_x_end = round(position_x_end_transposed + x_size / 2)
                position_y_end = round(-position_y_end_transposed + y_size / 2)
                print(position_x_end,position_y_end)
                output_image[position_x_end, position_y_end] = R, G, B
            except ZeroDivisionError:
                continue
            cv2.imshow('image', output_image)
            cv2.waitKey(1)
    cv2.waitKey(0)
    cv2.imwrite(output_path, output_image)


def create_transformed_schwarzschild_image(dt, t_end, r_s, input_path=test_input, output_path=test_output):
    input_image, output_image = open_input_and_output_image()
    x_size, y_size, output_image = blacken_output_image(output_image)
    for x in range(0, x_size):
        for y in range(0, y_size):
            x_start = -x_size / 2 + x
            y_start = y_size / 2 - y
            z_start = -10
            try:
                results = schwarzschild_geodesic_construction.\
                    create_specified_geodesic(x_start, y_start, z_start, dt, t_end, r_s)
                if results is not None:
                    r, theta, phi = results
                    position_x_end_transposed, position_y_end_transposed, position_z_end_transposed = \
                        conversion_formulas.spherical_to_cartesian(r[-1], theta[-1], phi[-1])
                    if (position_x_end_transposed < -x_size / 2 or position_x_end_transposed > x_size / 2) or (
                            position_y_end_transposed < - y_size / 2 or position_y_end_transposed > y_size / 2):
                        continue
                    position_x_end = round(position_x_end_transposed + x_size / 2)
                    position_y_end = round(-position_y_end_transposed + y_size / 2)
                    R, G, B = input_image[position_x_end][position_y_end]
                else:
                    # print('The solver returned None') -> r < r_s
                    continue
            except ZeroDivisionError:
                # print('Zero division error') -> origin
                continue
            output_image[x, y] = R, G, B
            cv2.imshow('image', output_image)
            cv2.waitKey(1)
    # For some reason the solver skips the first geodesic, (I have no idea why), this calculates it specifially again
    r, theta, phi = schwarzschild_geodesic_construction.create_specified_geodesic(-x_size / 2, y_size / 2, -10, dt, t_end, r_s)
    position_x_end_transposed, position_y_end_transposed, position_z_end_transposed \
        = conversion_formulas.spherical_to_cartesian(r[-1], theta[-1], phi[-1])
    position_x_end = round(position_x_end_transposed + x_size / 2)
    position_y_end = round(-position_y_end_transposed + y_size / 2)
    R, G, B = input_image[position_x_end][position_y_end]
    output_image[0, 0] = R, G, B
    cv2.imwrite(output_path, output_image)
    cv2.imshow('image', output_image)
    cv2.waitKey(0)








