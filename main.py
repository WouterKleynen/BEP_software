import numpy as np
import matplotlib.pyplot as plt
import schwarzschild_geodesic_construction
import sphere_numerical_solver
import minkowski_numerical_solver
from scipy.integrate import odeint
from scipy.integrate import solve_ivp
import plotter
import minkowski_geodesic_construction
import schwarzschild_numerical_solver
import pixel_transformation
import comparison_transformation_image

# define dt, t and r
dt = 0.005                     # define dt
t_end = 6                      # t end value
t = np.arange(0, t_end, dt)    # create array for t
n = len(t)                     # define n for loop
r = 1                          # unit sphere

# define initial condtion for the unit sphere: theta, phi, velocity_theta, velocity_phi
# initial_sphere = [1, 1, 1, 1]

# Eulers method for the unit sphere
# theta_numerical, phi_numerical, v_1_numerical, v_2_numerical = sphere_numerical_solver.euler_method(initial_sphere, n, dt)
# Figure 2
# plotter.plot_phi_to_theta(phi_numerical, theta_numerical, "by using eulers method for the unit sphere")
# Figure 3
# plotter.plot_trajectories(t, r, theta_numerical, phi_numerical, "trajectories by using eulers method for the unit sphere")
# Figure 4
# plotter.plot_three_dimensional_spherical_with_unit_sphere(r, theta_numerical, phi_numerical, "geodesic plot by using eulers method for the unit sphere")

# Python solver for the unit sphere
# U = odeint(sphere_numerical_solver.python_solver_INT, initial_sphere, t)
# Checker for Solver (optional)
# sol = solve_ivp(sphere_numerical_solver.python_solver_IPV, (0, t_end), initial_sphere, method='LSODA', t_eval=t)
# theta_solver   = U[:, 2]
# phi_solver     = U[:, 3]

# Figure 5 left
# plotter.plot_phi_to_theta(phi_solver, theta_solver, "by using a python solver for the sphere")

# Figure 5 middle
# plotter.plot_trajectories(t, r, theta_solver, phi_solver, "trajectories by using a pyhton solver for the sphere")

# FIgure 5 right
# plotter.plot_three_dimensional_spherical_with_unit_sphere(r, theta_solver, phi_solver, "geodesic plot by using a python solver for the sphere")

# define three different initial condtion for Minkowski space to get an impression of the geodesics
# initial_minkowksi_one   = [1, 1, 1, 1, 1, 1]
# initial_minkowksi_two   = [2, 2, 2, 2, 2, 2]
# initial_minkowksi_three = [3, 3, 3, 3, 3, 3]
# initial_minkowksi_four   = [4, 4, 4, 4, 4, 4]

# Eulers method for Minkowski space (Optional)
# r_numerical, theta_numerical, phi_numerical, v_1_numerical, v_2_numerical, v_3_numerical = minkowski_numerical_solver.euler_method(initial_minkowksi_one, n, dt)
# plotter.plot_trajectories(t, r_numerical, theta_numerical, phi_numerical, "trajectories by using eulers method for Minkowski space")
# plotter.plot_three_dimensional_spherical(r_numerical, theta_numerical, phi_numerical, "3D plot by using eulers method for Minkowksi space")

# Python solver for Minkowski space
# U = odeint(minkowski_numerical_solver.python_solver, initial_minkowksi_one, t)
# r_solver       = U[:, 0]
# theta_solver   = U[:, 1]
# phi_solver     = U[:, 2]

# Figure 6
# plotter.plot_trajectories(t, r_solver, theta_solver, phi_solver, "trajectories of the geodesic by using a python solver for Minkowski space")

# Figure 10
# plotter.plot_three_dimensional_spherical(r_solver, theta_solver, phi_solver, "3D plot of the geodesic by using a python solver for Minkowksi space")
#
# U = odeint(minkowski_numerical_solver.python_solver, initial_minkowksi_two, t)
# r_solver       = U[:, 0]
# theta_solver   = U[:, 1]
# phi_solver     = U[:, 2]

# Figure 7
# plotter.plot_trajectories(t, r_solver, theta_solver, phi_solver, "trajectories of the geodesic by using a python solver for Minkowski space")
#
# U = odeint(minkowski_numerical_solver.python_solver, initial_minkowksi_three, t)
# r_solver       = U[:, 0]
# theta_solver   = U[:, 1]
# phi_solver     = U[:, 2]

# Figure 8
# plotter.plot_trajectories(t, r_solver, theta_solver, phi_solver, "trajectories of the geodesic by using a python solver for Minkowski space")
#
# U = odeint(minkowski_numerical_solver.python_solver, initial_minkowksi_four, t)
# r_solver       = U[:, 0]
# theta_solver   = U[:, 1]
# phi_solver     = U[:, 2]

# Figure 9
# plotter.plot_trajectories(t, r_solver, theta_solver, phi_solver, "trajectories of the geodesic by using a python solver for Minkowski space")

# Plot the geodesics of the Minkowski space
# t_end = 20  # increase t to make sure the rays go from Z = -10 to Z = 10
# field_size = 6  # define field size

# Figure 11
# x_start, y_start, x_end, y_end = minkowski_geodesic_construction.create_geodesic_field(dt, field_size, t_end, True)

# Figure 12 left
# minkowski_geodesic_construction.create_scatter(x_start, y_start, 'starting postions field Minkowski space')

# Figure 12 right
# minkowski_geodesic_construction.create_scatter(x_end, y_end, 'end postions field Minkowski space')

# input_path = 'input_transformable_images//100x100_car.jpg'
# output_path = 'output_transformable_images//100x100_car_output.jpg'

# pixel_transformation.create_transformed_minkowski_image(dt, t_end, input_path, output_path)

# Define r_s
# r_s = 0.4
#
# # define initial condtion for Schwarzschild metric
# initial_schwarzschild = [1, 1, 1, 1, 1, 1, 1, 1]
#
# t_end = 40

# Eulers method for Schwarzschild metric
# t_numerical, r_numerical, theta_numerical, phi_numerical, v_0_numerical, v_1_numerical, v_2_numerical, v_3_numerical = schwarzschild_numerical_solver.euler_method(initial_schwarzschild, n, dt, r_s)
# plotter.plot_trajectories(t, r_numerical, theta_numerical, phi_numerical, "trajectories by using eulers method for Schwarzschild geodesic")
# plotter.plot_three_dimensional_spherical(r_numerical, theta_numerical, phi_numerical, "3D plot by using eulers method for Schwarzschild geodesic")

# Python solver for Schwarzschild space
# U = odeint(schwarzschild_numerical_solver.python_solver, initial_schwarzschild, t, (r_s, ))
# r_solver       = U[:, 1]
# theta_solver   = U[:, 2]
# phi_solver     = U[:, 3]
#
# # Plot Figure 17
# plotter.plot_trajectories(t, r_solver, theta_solver, phi_solver, "trajectories of the geodsic by using a python solver for Schwarzschild metric")
#
#
# r_s = 0.8

# Plot the geodesics of the Schwarzschild space
# Z_end = 10
# r_s = 1
# x_start, y_start, x_end, y_end = schwarzschild_geodesic_construction.create_geodesics_field(dt, 40, 6, r_s, Z_end, True)

# schwarzschild_geodesic_construction.create_scatter(x_start, y_start, 'starting postions field Schwarzschild')
# schwarzschild_geodesic_construction.create_scatter(x_end, y_end, 'end postions field Schwarzschild')

# input_path = 'input_transformable_images//starry_night.jpg'
# r_s = 0.5
# Z_end = 25
# x_size, cropped_input_path, output_path = pixel_transformation.create_transformed_schwarzschild_image(input_path, dt, t_end, r_s, Z_end)
# comparison_transformation_image.plot(cropped_input_path, output_path, r_s, x_size, Z_end)


# input_path = 'input_transformable_images//100x100_car.jpg'
# r_s = 0.4
# Z_end = 10
# Figure 23
# x_size, cropped_input_path, output_path = pixel_transformation.create_transformed_schwarzschild_image(input_path, dt, t_end, r_s, Z_end)
# Figure 24
# comparison_transformation_image.plot(input_path, output_path, r_s, x_size, Z_end)

# input_path = 'input_transformable_images//blue_space.jpg'
# r_s = 0.3
# Z_end = 30
# x_size, cropped_input_path, output_path = pixel_transformation.create_transformed_schwarzschild_image(input_path, dt, t_end, r_s, 20)
# comparison_transformation_image.plot(cropped_input_path, output_path, r_s, x_size, Z_end)
#
# cropped_input_path = 'input_transformable_images//600x600_space_cropped.jpg'
# output_path = 'output_transformable_images//600x600_space_transformed_r_s=0.55_Z_end=20_made_into_sphere.jpg'
# r_s = 0.8
# Z_end = 20
# x_size = 600
# x_size, cropped_input_path, output_path = pixel_transformation.create_transformed_schwarzschild_image(input_path, dt, t_end, r_s, 20)
# comparison_transformation_image.plot(cropped_input_path, output_path, r_s, x_size, Z_end)
#
# input_path = 'input_transformable_images//nebula.jpg'
# r_s = 0.8
# Z_end = 20
# x_size, cropped_input_path, output_path = pixel_transformation.create_transformed_schwarzschild_image(input_path, dt, t_end, r_s, 20)
# comparison_transformation_image.plot(cropped_input_path, output_path, r_s, x_size, Z_end)
#
# input_path = 'input_transformable_images//whatever_this_is.jpg'
# r_s = 0.3
# Z_end = 30
# x_size, cropped_input_path, output_path = pixel_transformation.create_transformed_schwarzschild_image(input_path, dt, t_end, r_s, 20)
# comparison_transformation_image.plot(cropped_input_path, output_path, r_s, x_size, Z_end)

