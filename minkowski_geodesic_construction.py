import matplotlib.pyplot as plt
import numpy as np
import conversion_formulas
import minkowski_numerical_solver
from scipy.integrate import odeint

x_start_series_minkowski = []
y_start_series_minkowski = []
x_end_series_minkowski = []
y_end_series_minkowski = []


def create_specified_geodesic(x_start, y_start, dt, t_end):
    t = np.arange(0, t_end, dt)
    z_start = -10
    x_start_series_minkowski.append(x_start)
    y_start_series_minkowski.append(y_start)
    initial_spherical = conversion_formulas.form_bol_three_dimensional_vector(x_start, y_start, z_start, 0, 0, 1)
    U = odeint(minkowski_numerical_solver.python_solver, initial_spherical, t)
    r_solver = U[:, 0]
    theta_solver = U[:, 1]
    phi_solver = U[:, 2]
    x_end, y_end, z_end = conversion_formulas.spherical_to_cartesian(r_solver[-1], theta_solver[-1], phi_solver[-1])
    return x_end, y_end


def create_geodesic_field(dt, t_end):
    fig = plt.figure()

    ax = plt.axes(projection='3d')
    ax.set_zlim3d(-12, 12)

    t = np.arange(0, t_end, dt)  # create array for t

    for i in range(0, 21):
        for j in range(0, 21):
            x_start = 10 - i
            y_start = 10 - j
            z_start = -10
            x_start_series_minkowski.append(x_start)
            y_start_series_minkowski.append(y_start)
            try:
                initial_spherical = conversion_formulas.form_bol_three_dimensional_vector(x_start, y_start, z_start, 0,
                                                                                          0, 1)
                U = odeint(minkowski_numerical_solver.python_solver, initial_spherical, t)
                r_solver        = U[:, 0]
                theta_solver    = U[:, 1]
                phi_solver      = U[:, 2]
                X, Y, Z = conversion_formulas.spherical_to_cartesian(r_solver, theta_solver, phi_solver)
                x_end_series_minkowski.append(X[-1])
                y_end_series_minkowski.append(Y[-1])
                ax.plot3D(X, Y, Z, 'blue')
            except ZeroDivisionError:
                continue
    plt.show()
    return x_start_series_minkowski, y_start_series_minkowski, x_end_series_minkowski, y_end_series_minkowski


# create scattered X Y plot
def create_photo(x_series, y_series, plot_title):
    plt.scatter(x_series, y_series)
    plt.title(plot_title)
    plt.show()


