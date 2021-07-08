import numpy as np

import schwarzschild_geodesics_plot
import sphere_numerical_solver as sns
import minkowski_numerical_solver as mns
from scipy.integrate import odeint
import plotter
import minkowski_geodesics_plot
import schwarzschild_numerical_solver as schns
import pixel_transformation

# define dt, t and r
dt = 0.005                     # define dt
t_end = 6                      # t end value
t = np.arange(0, t_end, dt)    # create array for t
n = len(t)                     # define n for loop
r = 1                          # unit sphere

# define initial condtion for the sphere: theta, phi, velocity_theta, velocity_phi
# initial_sphere = [1, 1, 1, 1]

# Eulers method for the sphere
# theta_numerical, phi_numerical, v_1_numerical, v_2_numerical = sns.euler_method_sphere(initial_sphere, n, dt)
# plotter.plot_phi_to_theta(phi_numerical, theta_numerical, "by using eulers method for the sphere")
# plotter.plot_trajectories(t, r, theta_numerical, phi_numerical, "trajectories by using eulers method for the sphere")
# plotter.plot_three_dimensional_spherical_with_unit_sphere(r, theta_numerical, phi_numerical, "3D plot by using eulers method for the sphere")

# Python solver for the sphere
# solver_output = odeint(sns.python_solver_sphere, initial_sphere, t)
# theta_solver   = solver_output[:, 2]
# phi_solver     = solver_output[:, 3]
# plotter.plot_phi_to_theta(phi_solver, theta_solver, "by using a python solver for the sphere")
# plotter.plot_trajectories(t, r, theta_solver, phi_solver, "trajectories by using a pyhton solver for the sphere")
# plotter.plot_three_dimensional_spherical_with_unit_sphere(r, theta_solver, phi_solver, "3D plot by using a python solver for the sphere")

# define initial condtion for Minkowski space
# initial_minkowksi = [1, 1, 1, 1, 1, 1]

# Eulers method for Minkowski space
# r_numerical, theta_numerical, phi_numerical, v_1_numerical, v_2_numerical, v_3_numerical = mns.euler_method_minkowski(initial, n, dt)
# plotter.plot_trajectories(t, r_numerical, theta_numerical, phi_numerical, "trajectories by using eulers method for Minkowski space")
# plotter.plot_three_dimensional_spherical(r_numerical, theta_numerical, phi_numerical, "3D plot by using eulers method for Minkowksi space")

# Python solver for Minkowski space
# U = odeint(mns.python_solver_minkowski, initial_minkowksi, t)
# r_solver       = U[:, 0]
# theta_solver   = U[:, 1]
# phi_solver     = U[:, 2]
# plotter.plot_trajectories(t, r_solver, theta_solver, phi_solver, "trajectories by using a python solver for Minkowski space")
# plotter.plot_three_dimensional_spherical(r_solver, theta_solver, phi_solver, "3D plot by using a python solver for Minkowksi space")

# Plot the geodesics of the Minkowski space
# t_end = 20  # increase t to make sure the rays go from Z = -10 to Z = 10
# x_start, y_start, x_end, y_end = minkowski_geodesics_plot.create_minkowski_geodesics_loop(dt, t_end)
# minkowski_geodesics_plot.create_photo(x_start, y_start, 'start photo Minkowski space')
# minkowski_geodesics_plot.create_photo(x_end, y_end, 'end photo Minkowski space')

# define initial condtion for Schwarzschild metric
initial_schwarzschild = [1, 1, 1, 1, 1, 1, 1, 1]

# Eulers method for Schwarzschild metric
# t_numerical, r_numerical, theta_numerical, phi_numerical, v_0_numerical, v_1_numerical, v_2_numerical, v_3_numerical = schns.euler_method_schwarzschild(initial_schwarzschild, n, dt)
# plotter.plot_trajectories(t, r_numerical, theta_numerical, phi_numerical, "trajectories by using eulers method for Schwarzschild geodesic")
# plotter.plot_three_dimensional_spherical(r_numerical, theta_numerical, phi_numerical, "3D plot by using eulers method for Schwarzschild geodesic")

# Python solver for Schwarzschild space
# U = odeint(schns.python_solver_schwarzschild, initial_schwarzschild, t)
# t_solver       = U[:, 0]
# r_solver       = U[:, 1]
# theta_solver   = U[:, 2]
# phi_solver     = U[:, 3]
# plotter.plot_trajectories(t, r_solver, theta_solver, phi_solver, "trajectories by using a python solver for Schwarzschild geodesic")
# plotter.plot_three_dimensional_spherical(r_solver, theta_solver, phi_solver, "3D plot by using a python solver for Schwarzschild geodesic")

# Plot the geodesics of the Minkowski space
# t_end = 20  # increase t to make sure the rays go from Z = -10 to Z = 10
# x_start, y_start, x_end, y_end = schwarzschild_geodesics_plot.create_schwarschild_geodesics_loop(dt, t_end)
# schwarzschild_geodesics_plot.create_photo(x_start, y_start, 'start photo Schwarzschild')
# schwarzschild_geodesics_plot.create_photo(x_end, y_end, 'end photo Schwarzschild')

# Transform pixels
pixel_transformation.create_transformed_image('Minkowski')

#minkowski_geodesics_plot.create_specific_minkowski_geodesic(-6, 6, 0.05, 20)
