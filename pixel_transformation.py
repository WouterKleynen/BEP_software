import minkowski_geodesic_construction
import schwarzschild_geodesic_construction
from shutil import copyfile
import warnings
import conversion_formulas
import cv2
import os.path
import math
import numpy as np

# Numpy throws a RuntimeWarning when 0 is divided by 0 in the origin. We simply skip this value.
warnings.filterwarnings("ignore", category=RuntimeWarning)


def crop_to_largest_central_square(input_path):
    Image = cv2.imread(input_path)
    height = Image.shape[0]
    width = Image.shape[1]
    if height >= width:
        new_height = width
        new_width = width
    else:
        new_height = height
        new_width = height
    start_width = round((width - new_width) / 2)
    start_height = round((height - new_height) / 2)
    cropped_image = Image[start_height:start_height + new_height, start_width:start_width + new_width]

    extension = os.path.splitext(input_path)[1]
    cropped_path = input_path.replace(str(extension), '_cropped' + str(extension))

    cv2.imwrite(cropped_path, cropped_image)
    return cropped_image, cropped_path


def blacken_output_image(output_image, output_path):
    x = output_image.shape[0]
    y = output_image.shape[1]
    for i in range(0, x):
        for j in range(0, y):
            output_image[i, j] = [0, 0, 0]
    cv2.imwrite(output_path, output_image)
    return x, y, output_image


def sphere_circle(output_path):
    output_image = cv2.imread(output_path)
    width = output_image.shape[0]
    center_height = math.floor(width / 2)
    extension = os.path.splitext(output_path)[1]
    new_path = output_path.replace(str(extension), '_made_into_sphere' + str(extension))
    for i in range(math.floor(width / 2.0), width):
        if np.any(output_image[center_height, i] != 0):
            radius = i - math.floor(width / 2.0)
            output_image = cv2.circle(output_image, (round(width / 2), round(width / 2)), round(1.3 * radius),
                                      (0, 0, 0), -1)
            cv2.imwrite(new_path, output_image)
            cv2.imshow('image', output_image)
            cv2.waitKey(0)
            break
        # print(output_image[i, center_height])


def create_transformed_minkowski_image(dt, t_end, input_path):
    title = input_path.split("//", 1)
    extension = os.path.splitext(input_path)[1]
    output_path = 'output_transformable_images//' + title[1]
    output_path = output_path.replace(str(extension), '_transformed' + str(extension))
    copyfile(input_path, output_path)
    input_image = cv2.imread(input_path)
    output_image = cv2.imread(output_path)
    x_size, y_size, output_image = blacken_output_image(output_image, output_path)
    for y in range(0, y_size):
        for x in range(0, x_size):
            x_start = -10 + 20 * (x / x_size)
            y_start = 10 - 20 * (y / y_size)
            z_start = -10
            try:
                r, theta, phi = minkowski_geodesic_construction.create_specified_geodesic(
                    x_start, y_start, z_start, dt, t_end)
                position_x_end_transposed, position_y_end_transposed, position_z_end_transposed = \
                    conversion_formulas.spherical_to_cartesian(r[-1], theta[-1], phi[-1])
                position_x_end = round((position_x_end_transposed + 10) * x_size / 20)
                position_y_end = round((position_y_end_transposed - 10) * y_size / -20)
                R, G, B = input_image[position_y_end][position_x_end]
            except ZeroDivisionError:
                continue
            # CV2 apparently reverses the order of row and columns which is super weird but ok
            output_image[y, x] = R, G, B
            cv2.imshow('image', output_image)
            cv2.waitKey(1)
    cv2.imwrite(output_path, output_image)
    cv2.imshow('image', output_image)
    cv2.waitKey(0)


def create_transformed_schwarzschild_image(input_path, dt, t_end, r_s, Z_end):
    black_radius = 0
    title = input_path.split("//", 1)
    extension = os.path.splitext(input_path)[1]
    output_path = 'output_transformable_images//' + title[1]
    output_path = output_path.replace(str(extension), '_transformed' + '_r_s='+str(r_s) + '_Z_end=' + str(Z_end)
                                      + str(extension))
    input_image, input_path = crop_to_largest_central_square(input_path)
    copyfile(input_path, output_path)
    output_image = cv2.imread(output_path)
    y_size, x_size, output_image = blacken_output_image(output_image, output_path)
    print(y_size, x_size)
    for y in range(0, y_size):
        for x in range(0, x_size):
            x_start = -10 + 20 * (x / x_size)
            y_start = 10 - 20 * (y / y_size)
            z_start = -10
            try:
                results = schwarzschild_geodesic_construction. \
                    create_specified_geodesic(x_start, y_start, z_start, dt, t_end, r_s, Z_end)
                if results is not None:
                    r, theta, phi = results
                    position_x_end_transposed, position_y_end_transposed, position_z_end_transposed = \
                        conversion_formulas.spherical_to_cartesian(r[-1], theta[-1], phi[-1])
                    position_x_end = round((position_x_end_transposed + 10) * x_size / 20)
                    position_y_end = round((position_y_end_transposed - 10) * y_size / -20)
                    if (position_x_end < 0 or position_x_end >= x_size) or (
                            position_y_end < 0 or position_y_end >= y_size):
                        continue
                    # CV2 apparently reverses the order of row and columns which is super weird but ok
                    R, G, B = input_image[position_y_end][position_x_end]
                    output_image[y, x] = R, G, B
                else:
                    distance_center_x = abs(x - x_size / 2)
                    distance_center_y = abs(y - y_size / 2)
                    if distance_center_x != x_size / 2.0 and distance_center_y != y_size / 2.0:
                        radius = math.sqrt(distance_center_x ** 2 + distance_center_y ** 2)
                        if radius > black_radius and distance_center_x != 50.0:
                            black_radius = radius
                    continue
            except ZeroDivisionError:
                continue
            except IndexError:
                continue
            except ValueError:
                continue
            cv2.imshow('image', output_image)
            cv2.waitKey(1)
        cv2.imwrite(output_path, output_image)
    # For some reason the solver skips the first geodesic, (I have no idea why), this calculates it specifially again
    r, theta, phi = schwarzschild_geodesic_construction.create_specified_geodesic(-10, 10, -10, dt, t_end, r_s, Z_end)
    position_x_end_transposed, position_y_end_transposed, position_z_end_transposed \
        = conversion_formulas.spherical_to_cartesian(r[-1], theta[-1], phi[-1])
    position_x_end = round((position_x_end_transposed + 10) * x_size / 20)
    position_y_end = round((position_y_end_transposed - 10) * y_size / -20)
    R, G, B = input_image[position_x_end][position_y_end]
    output_image[0, 0] = R, G, B
    output_image = cv2.circle(output_image, (round(x_size / 2), round(y_size / 2)), math.ceil(1.3*black_radius), (0, 0, 0),
                              -1)
    cv2.imwrite(output_path, output_image)
    cv2.imshow('image', output_image)
    cv2.waitKey(0)
    return x_size, y_size


# sphere_circle('output_transformable_images//hubble.jpg')
# sphere_circle('output_transformable_images//600x600_space.jpg')
# sphere_circle('output_transformable_images//605_479_colored_space.jpg')
# sphere_circle('output_transformable_images//747x800_stars.jpg')
# sphere_circle('output_transformable_images//1180x884_space.jpg')
# sphere_circle('output_transformable_images//blue_space.jpg')
# sphere_circle('output_transformable_images//nebula.jpg')
# sphere_circle('output_transformable_images//whatever_this_is.jpg')
# sphere_circle('output_transformable_images//100x100_car_distorted_r_s=0.4_Z_end=20.jpg')



