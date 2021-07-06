import matplotlib.pyplot as plt
import numpy as np
import conversion_coordinate_system as ccs
import minkowski_numerical_solver as mns
from scipy.integrate import odeint
import schwarzschild_numerical_solver as schns


x_start_series_minkowski = []
y_start_series_minkowski = []
x_end_series_minkowski = []
y_end_series_minkowski = []


x_start_series_schwarzschild = []
y_start_series_schwarzschild = []
x_end_series_schwarzschild = []
y_end_series_schwarzschild = []


def create_specific_schwarzschild_geodesic(x_start, y_start, dt, t_end):
    t = np.arange(0, t_end, dt)  # create array for t
    z_start = -10
    x_start_series_minkowski.append(x_start)
    y_start_series_minkowski.append(y_start)
    initial_spherical = ccs.form_initial_spherical_vector(x_start, y_start, z_start, 0, 0, 1)
    U = odeint(mns.python_solver_minkowski, initial_spherical, t)
    r_solver = U[:, 1]
    theta_solver = U[:, 2]
    phi_solver = U[:, 3]
    X, Y, Z = ccs.conversion_coordinate_spherical_to_cartesian(r_solver, theta_solver, phi_solver)
    x_end = X[-1]
    y_end = Y[-1]
    return x_end, y_end


def create_schwarschild_geodesics_loop(dt, t_end):
    fig = plt.figure()

    ax = plt.axes(projection='3d')
    ax.set_zlim3d(-12, 12)

    # define dt, t and r
    t = np.arange(0, t_end, dt)  # create array for t

    for i in range(0, 10):
        for j in range(0, 10):
            x_start = 10 - i
            y_start = 10 - j
            z_start = -10
            x_start_series_schwarzschild.append(x_start)
            y_start_series_schwarzschild.append(y_start)
            initial_spherical = ccs.form_initial_four_dimensional_vector(x_start, y_start, z_start, 0, 0, 1)
            U = odeint(schns.python_solver_schwarzschild, initial_spherical, t)
            r_solver     = U[:, 1]
            theta_solver = U[:, 2]
            phi_solver   = U[:, 3]
            X, Y, Z = ccs.conversion_coordinate_spherical_to_cartesian(r_solver, theta_solver, phi_solver)
            x_end_series_schwarzschild.append(X[-1])
            y_end_series_schwarzschild.append(Y[-1])
            ax.plot3D(X, Y, Z, 'blue')
    plt.show()
    return x_start_series_schwarzschild, y_start_series_schwarzschild, x_end_series_schwarzschild, y_end_series_schwarzschild


def create_photo(x_series, y_series, plot_title):
    # create X Y plot of starting point
    plt.ylim(11, 0)
    plt.xlim(11, 0)
    plt.scatter(x_series, y_series)
    plt.title(plot_title)
    plt.show()


