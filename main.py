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

# define initial condtion for the sphere: theta, phi, velocity_theta, velocity_phi
initial_sphere = [4, 4, 4, 4]

# Eulers method for the sphere
# theta_numerical, phi_numerical, v_1_numerical, v_2_numerical = sphere_numerical_solver.euler_method(initial_sphere, n, dt)
# plotter.plot_phi_to_theta(phi_numerical, theta_numerical, "by using eulers method for the unit sphere")
# plotter.plot_trajectories(t, r, theta_numerical, phi_numerical, "trajectories by using eulers method for the unit sphere")
# plotter.plot_three_dimensional_spherical_with_unit_sphere(r, theta_numerical, phi_numerical, "geodesic plot by using eulers method for the unit sphere")

# Python solver for the sphere
# U = odeint(sphere_numerical_solver.python_solver_INT, initial_sphere, t)
# sol = solve_ivp(sphere_numerical_solver.python_solver_IPV, (0, t_end), initial_sphere, method='LSODA', t_eval=t)
# theta_solver   = U[:, 2]
# phi_solver     = U[:, 3]
# plotter.plot_phi_to_theta(phi_solver, theta_solver, "by using a python solver for the sphere")
# plotter.plot_trajectories(t, r, theta_solver, phi_solver, "trajectories by using a pyhton solver for the sphere")
# plotter.plot_three_dimensional_spherical_with_unit_sphere(r, theta_solver, phi_solver, "geodesic plot by using a python solver for the sphere")

# define initial condtion for Minkowski space to get an impression of the geodesics
initial_minkowksi = [1, 1, 1, 1, 1, 1]

# Eulers method for Minkowski space
# r_numerical, theta_numerical, phi_numerical, v_1_numerical, v_2_numerical, v_3_numerical = minkowski_numerical_solver.euler_method(initial, n, dt)
# plotter.plot_trajectories(t, r_numerical, theta_numerical, phi_numerical, "trajectories by using eulers method for Minkowski space")
# plotter.plot_three_dimensional_spherical(r_numerical, theta_numerical, phi_numerical, "3D plot by using eulers method for Minkowksi space")

# Python solver for Minkowski space
# U = odeint(minkowski_numerical_solver.python_solver, initial_minkowksi, t)
# r_solver       = U[:, 0]
# theta_solver   = U[:, 1]
# phi_solver     = U[:, 2]
# plotter.plot_trajectories(t, r_solver, theta_solver, phi_solver, "trajectories of the geodesic by using a python solver for Minkowski space")
# plotter.plot_three_dimensional_spherical(r_solver, theta_solver, phi_solver, "3D plot of the geodesic by using a python solver for Minkowksi space")

# Plot the geodesics of the Minkowski space
# t_end = 20  # increase t to make sure the rays go from Z = -10 to Z = 10
# x_start, y_start, x_end, y_end = minkowski_geodesic_construction.create_geodesic_field(dt, 6, t_end)
# minkowski_geodesic_construction.create_scatter(x_start, y_start, 'starting postions field Minkowski space')
# minkowski_geodesic_construction.create_scatter(x_end, y_end, 'end postions field Minkowski space')

# input_path = 'input_transformable_images//100x100_car.jpg'
# output_path = 'output_transformable_images//100x100_car_output.jpg'

# pixel_transformation.create_transformed_minkowski_image(dt, t_end, input_path, output_path)

# Define r_s
r_s = 0.4

# define initial condtion for Schwarzschild metric
initial_schwarzschild = [1, 1, 1, 1, 1, 1, 1, 1]

t_end = 40

# Eulers method for Schwarzschild metric
# t_numerical, r_numerical, theta_numerical, phi_numerical, v_0_numerical, v_1_numerical, v_2_numerical, v_3_numerical = schwarzschild_numerical_solver.euler_method(initial_schwarzschild, n, dt, r_s)
# plotter.plot_trajectories(t, r_numerical, theta_numerical, phi_numerical, "trajectories by using eulers method for Schwarzschild geodesic")
# plotter.plot_three_dimensional_spherical(r_numerical, theta_numerical, phi_numerical, "3D plot by using eulers method for Schwarzschild geodesic")

# Python solver for Schwarzschild space
# U = odeint(schwarzschild_numerical_solver.python_solver, initial_schwarzschild, t, (r_s, ))
# r_solver       = U[:, 1]
# theta_solver   = U[:, 2]
# phi_solver     = U[:, 3]
# plotter.plot_trajectories(t, r_solver, theta_solver, phi_solver, "trajectories of the geodsic by using a python solver for Schwarzschild metric")
# plotter.plot_three_dimensional_spherical(r_solver, theta_solver, phi_solver, "3D plot by using a python solver for Schwarzschild geodesic")

# Plot the geodesics of the Schwarzschild space
# x_start, y_start, x_end, y_end = schwarzschild_geodesic_construction.create_geodesics_field(dt, 11, 6, r_s, True)
# x_start, y_start, x_end, y_end = schwarzschild_geodesic_construction.create_geodesics_field(dt, 13, 6, r_s, True)
# x_start, y_start, x_end, y_end = schwarzschild_geodesic_construction.create_geodesics_field(dt, 15, 6, r_s, True)
# x_start, y_start, x_end, y_end = schwarzschild_geodesic_construction.create_geodesics_field(dt, 17, 6, r_s, True)
# x_start, y_start, x_end, y_end = schwarzschild_geodesic_construction.create_geodesics_field(dt, 20, 6, r_s, True)
# x_start, y_start, x_end, y_end = schwarzschild_geodesic_construction.create_geodesics_field(dt, 40, 6, r_s, True)

# schwarzschild_geodesic_construction.create_scatter(x_start, y_start, 'starting postions field Schwarzschild')
# schwarzschild_geodesic_construction.create_scatter(x_end, y_end, 'end postions field Schwarzschild')

input_path = 'input_transformable_images//nebula.jpg'

x_size, y_size = pixel_transformation.create_transformed_schwarzschild_image(input_path, dt, t_end, r_s)
# comparison_transformation_image.plot(input_path, output_path, r_s, x_size, y_size)
# comparison_transformation_image.plot(input_path, output_path, 100)

# schwarzschild_geodesic_construction.create_geodesics_field(dt, t_end, 30, r_s, plot=True)
# pixel_transformation.create_transformed_schwarzschild_image(input_path, output_path, dt, t_end, r_s)

