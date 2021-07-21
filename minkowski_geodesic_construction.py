import matplotlib.pyplot as plt
import numpy as np
import conversion_formulas
import minkowski_numerical_solver
from scipy.integrate import odeint

x_start_series_minkowski = []
y_start_series_minkowski = []
x_end_series_minkowski = []
y_end_series_minkowski = []


def create_specified_geodesic(x_start, y_start, z_start, dt, t_end):
    t = np.arange(0, t_end, dt)
    x_start_series_minkowski.append(x_start)
    y_start_series_minkowski.append(y_start)
    initial_spherical = conversion_formulas.form_bol_three_dimensional_vector(x_start, y_start, z_start, 0, 0, 1)
    U = odeint(minkowski_numerical_solver.python_solver, initial_spherical, t)
    r_solver     = U[:, 0]
    theta_solver = U[:, 1]
    phi_solver   = U[:, 2]
    return r_solver, theta_solver, phi_solver


def create_geodesic_field(dt, field_size, t_end, plot=False):
    if plot:
        fig = plt.figure()
        ax = plt.axes(projection='3d')

    t = np.arange(0, t_end, dt)  # create array for t

    for i in range(0, field_size+1):
        for j in range(0, field_size+1):
            x_start = field_size/2 - i
            y_start = field_size/2 - j
            z_start = -10
            x_start_series_minkowski.append(x_start)
            y_start_series_minkowski.append(y_start)
            print('x start = ' + str(x_start), 'y start = ' + str(y_start), 'z start = ' + str(z_start))
            try:
                r, theta, phi = create_specified_geodesic(x_start, y_start, z_start, dt, t_end)
                X, Y, Z = conversion_formulas.spherical_to_cartesian(r, theta, phi)
                print('x end = ' + str(X[-1]), 'y end = ' + str(Y[-1]), 'z end = ' + str(Z[-1]))
                x_end_series_minkowski.append(X[-1])
                y_end_series_minkowski.append(Y[-1])
                if plot:
                    ax.plot3D(X, Y, Z, 'blue')
                    ax.set_xlabel('X')
                    ax.set_ylabel('Y')
                    ax.set_zlabel('Z')
            except ZeroDivisionError:
                continue
    if plot:
        plt.show()
    return x_start_series_minkowski, y_start_series_minkowski, x_end_series_minkowski, y_end_series_minkowski


# create scattered X Y plot
def create_photo(x_series, y_series, plot_title):
    plt.scatter(x_series, y_series)
    plt.title(plot_title)
    plt.show()


