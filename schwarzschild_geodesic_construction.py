import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate.odepack

import conversion_formulas as ccs
from scipy.integrate import odeint
import schwarzschild_numerical_solver
import events_tester
import warnings

# warnings.filterwarnings("error")


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
    U = odeint(schwarzschild_numerical_solver.python_solver, initial_schwarzschild, t, (r_s,))
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

    for i in range(0, 7):
        for j in range(0, 7):
            x_start = 3 - i
            y_start = 3 - j
            z_start = -10
            x_start_series_schwarzschild.append(x_start)
            y_start_series_schwarzschild.append(y_start)
            print(x_start, y_start)
            try:
                initial_schwarzschild = ccs.form_bol_four_dimensional_vector(x_start, y_start, z_start, 0, 0, 1, r_s)
                U = odeint(schwarzschild_numerical_solver.python_solver, initial_schwarzschild, t, (r_s,))
                try:
                    events_tester.python_solver_with_termination(t, t_end, initial_schwarzschild, r_s)
                except UserWarning:
                    continue
                r_solver     = U[:, 1]
                if not all(r > r_s for r in r_solver):  # check if within Schwarzschild radius
                    continue
                else:
                    theta_solver = U[:, 2]
                    phi_solver   = U[:, 3]
                    X, Y, Z = ccs.spherical_to_cartesian(r_solver, theta_solver, phi_solver)
                    x_end_series_schwarzschild.append(X[-1])
                    y_end_series_schwarzschild.append(Y[-1])
                    ax.plot3D(X, Y, Z, 'blue')
            except scipy.integrate.odepack.ODEintWarning:
                continue
            except ZeroDivisionError:
                continue
    ax.title.set_text('r_s = ' + str(r_s) + ', t = ' + str(t_end))
    plt.show()
    return x_start_series_schwarzschild, y_start_series_schwarzschild, x_end_series_schwarzschild, y_end_series_schwarzschild


# create X Y scattered plot
def create_photo(x_series, y_series, plot_title):
    plt.scatter(x_series, y_series)
    plt.title(plot_title)
    plt.show()


