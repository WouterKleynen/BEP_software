import matplotlib.pyplot as plt
import numpy as np
import conversion_formulas as ccs
import solver_with_events
import warnings

warnings.filterwarnings("error")

x_start_series_schwarzschild = []
y_start_series_schwarzschild = []
x_end_series_schwarzschild = []
y_end_series_schwarzschild = []


def create_specified_geodesic(x_start, y_start, z_start, dt, t_end, r_s, Z_end):
    t = np.arange(0, t_end, dt)
    initial_schwarzschild = ccs.form_bol_four_dimensional_vector(x_start, y_start, z_start, 0, 0, 1, r_s)
    V = solver_with_events.python_solver_with_termination(t, t_end, initial_schwarzschild, r_s, Z_end)
    if V is not None:
        r_solver = V[1]
        theta_solver = V[2]
        phi_solver = V[3]
        return r_solver, theta_solver, phi_solver
    else:
        return None


def create_geodesics_field(dt, t_end, field_size, r_s, Z_end, plot=False):
    if plot:
        fig = plt.figure()
        ax = plt.axes(projection='3d')

    t = np.arange(0, t_end, dt)  # create array for t

    for x in range(0, field_size + 1):
        for y in range(0, field_size + 1):
            x_start = field_size / 2 - x
            y_start = field_size / 2 - y
            z_start = -10
            x_start_series_schwarzschild.append(x_start)
            y_start_series_schwarzschild.append(y_start)
            # print('x start = ' + str(x_start), 'y start = ' + str(y_start), 'z start = ' + str(z_start))
            try:
                results = create_specified_geodesic(x_start, y_start, z_start, dt, t_end, r_s, Z_end)
                if results is not None:
                    r, theta, phi = results
                    X, Y, Z = ccs.spherical_to_cartesian(r, theta, phi)
                    # print('x end = ' + str(X[-1]), 'y end = ' + str(Y[-1]), 'z end = ' + str(Z[-1]))
                    if (X[-1] < -field_size / 2 or X[-1] > field_size / 2) or (
                            Y[-1] < -field_size / 2 or Y[-1] > field_size / 2):
                        continue
                    x_end_series_schwarzschild.append(X[-1])
                    y_end_series_schwarzschild.append(Y[-1])
                    if plot:
                        ax.plot3D(X, Y, Z, 'blue')
                        ax.set_xlabel('X')
                        ax.set_ylabel('Y')
                        ax.set_zlabel('Z')
                else:
                    # print('The solver returned None') -> r < r_s
                    continue
            except ZeroDivisionError:
                # print('Zero division error') -> origin
                continue
    # For some reason the solver skips the first geodesic, (I have no idea why), this calculates it specifially agai
    r, theta, phi = create_specified_geodesic(field_size / 2, field_size / 2, -10, dt, t_end, r_s, Z_end)
    X, Y, Z = ccs.spherical_to_cartesian(r, theta, phi)
    x_end_series_schwarzschild.append(X[-1])
    y_end_series_schwarzschild.append(Y[-1])
    if plot:
        ax.plot3D(X, Y, Z, 'blue')
        ax.title.set_text('r_s = ' + str(r_s) + ', t = ' + str(t_end))
        plt.show()
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')
    return x_start_series_schwarzschild, y_start_series_schwarzschild, x_end_series_schwarzschild, y_end_series_schwarzschild


# create X Y scattered plot
def create_scatter(x_series, y_series, plot_title):
    plt.scatter(x_series, y_series)
    plt.title(plot_title)
    plt.show()
