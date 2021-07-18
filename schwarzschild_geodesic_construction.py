import matplotlib.pyplot as plt
import numpy as np
import conversion_formulas as ccs
import events_tester
import warnings

warnings.filterwarnings("error")


x_start_series_schwarzschild = []
y_start_series_schwarzschild = []
x_end_series_schwarzschild = []
y_end_series_schwarzschild = []


def create_specified_geodesic(x_start, y_start, z_start, dt, t_end, r_s):
    t = np.arange(0, t_end, dt)
    initial_schwarzschild = ccs.form_bol_four_dimensional_vector(x_start, y_start, z_start, 0, 0, 1, r_s)
    V = events_tester.python_solver_with_termination(t, t_end, initial_schwarzschild, r_s)
    if V is not None:
        r_solver = V[1]
        theta_solver = V[2]
        phi_solver = V[3]
        return r_solver, theta_solver, phi_solver
    else:
        return None


def create_geodesics_field(dt, t_end, field_size, r_s):
    fig = plt.figure()

    ax = plt.axes(projection='3d')

    t = np.arange(0, t_end, dt)  # create array for t

    for i in range(0, field_size + 1):
        for j in range(0, field_size + 1):
            x_start = field_size / 2 - i
            y_start = field_size / 2 - j
            z_start = -10
            x_start_series_schwarzschild.append(x_start)
            y_start_series_schwarzschild.append(y_start)
            # print('x start = ' + str(x_start), 'y start = ' + str(y_start), 'z start = ' + str(z_start))
            try:
                results = create_specified_geodesic(x_start, y_start, z_start, dt, t_end, r_s)
                if results is not None:
                    r, theta, phi = results
                    X, Y, Z = ccs.spherical_to_cartesian(r, theta, phi)
                    # print('x end = ' + str(X[-1]), 'y end = ' + str(Y[-1]), 'z end = ' + str(Z[-1]))
                    if (X[-1] < -field_size/2 or X[-1] > field_size/2) or (Y[-1] < -field_size/2 or Y[-1] > field_size/2):
                        continue
                    x_end_series_schwarzschild.append(X[-1])
                    y_end_series_schwarzschild.append(Y[-1])
                    ax.plot3D(X, Y, Z, 'blue')
                else:
                    # print('The solver returned None') -> r < r_s
                    continue
            except ZeroDivisionError:
                # print('Zero division error') -> origin
                continue
    ###########################################################################
    # For some reason the solver skips the first geodesic, (I have no idea why), this calculates it specifially again
    initial_schwarzschild = ccs.form_bol_four_dimensional_vector(field_size/2, field_size/2, -10, 0, 0, 1, r_s)
    V = events_tester.python_solver_with_termination(t, t_end, initial_schwarzschild, r_s)
    r_solver = V[1]
    theta_solver = V[2]
    phi_solver = V[3]
    X, Y, Z = ccs.spherical_to_cartesian(r_solver, theta_solver, phi_solver)
    ax.plot3D(X, Y, Z, 'blue')
    ###########################################################################
    ax.title.set_text('r_s = ' + str(r_s) + ', t = ' + str(t_end))
    plt.show()
    return x_start_series_schwarzschild, y_start_series_schwarzschild, x_end_series_schwarzschild, y_end_series_schwarzschild


# create X Y scattered plot
def create_photo(x_series, y_series, plot_title):
    plt.scatter(x_series, y_series)
    plt.title(plot_title)
    plt.show()

