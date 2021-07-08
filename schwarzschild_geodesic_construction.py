import matplotlib.pyplot as plt
import numpy as np
import conversion_formulas as ccs
from scipy.integrate import odeint
import schwarzschild_numerical_solver


x_start_series_schwarzschild = []
y_start_series_schwarzschild = []
x_end_series_schwarzschild = []
y_end_series_schwarzschild = []


def create_specified_geodesic(x_start, y_start, dt, t_end, r_s):
    t = np.arange(0, t_end, dt)  # create array for t
    # n = len(t)
    z_start = -10
    x_start_series_schwarzschild.append(x_start)
    y_start_series_schwarzschild.append(y_start)
    initial_schwarzschild = ccs.form_bol_four_dimensional_vector(x_start, y_start, z_start, 0, 0, 1, r_s)
    # U = schwarzschild_numerical_solver.euler_method(initial_schwarzschild, n, dt, r_s)
    # r_solver = U[1]
    # theta_solver = U[2]
    # phi_solver = U[3]
    # print(r_solver[0], theta_solver[0], phi_solver[0])
    # x_end, y_end, z_end = ccs.spherical_to_cartesian(r_solver[-1], theta_solver[-1], phi_solver[-1])
    # print(x_end, y_end)
    U = odeint(schwarzschild_numerical_solver.python_solver, initial_schwarzschild, t, args=(0.5, 0))
    r_solver = U[:, 1]
    theta_solver = U[:, 2]
    phi_solver = U[:, 3]
    x_end, y_end, z_end = ccs.spherical_to_cartesian(r_solver[-1], theta_solver[-1], phi_solver[-1])
    return x_end, y_end


def create_geodesics_field(dt, t_end, r_s):
    fig = plt.figure()

    ax = plt.axes(projection='3d')
    ax.set_zlim3d(-12, 12)

    t = np.arange(0, t_end, dt)  # create array for t

    for i in range(0, 20):
        for j in range(0, 20):
            x_start = 10 - i
            y_start = 10 - j
            z_start = -10
            x_start_series_schwarzschild.append(x_start)
            y_start_series_schwarzschild.append(y_start)
            try:
                initial_schwarzschild = ccs.form_bol_four_dimensional_vector(x_start, y_start, z_start, 0, 0, 1, r_s)
                U = odeint(schwarzschild_numerical_solver.python_solver, initial_schwarzschild, t, args=(0.5, 0))
                r_solver = U[:, 1]
                theta_solver = U[:, 2]
                phi_solver = U[:, 3]
                X, Y, Z = ccs.spherical_to_cartesian(r_solver[-1], theta_solver[-1], phi_solver[-1])
                x_end_series_schwarzschild.append(X)
                y_end_series_schwarzschild.append(Y)
                ax.plot3D(X, Y, Z, 'blue')
            except ZeroDivisionError:
                continue
    return x_start_series_schwarzschild, y_start_series_schwarzschild, x_end_series_schwarzschild, y_end_series_schwarzschild


def remove_issue_points(x_series, y_series):
    for i in range(max(x_series, y_series)):
        if x_series or y_series is None:
            x_series[i] = 0
            x_series[i] = 0


# create X Y scattered plot
def create_photo(x_series, y_series, plot_title):
    plt.scatter(x_series, y_series)
    plt.title(plot_title)
    plt.show()


