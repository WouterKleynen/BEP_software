import numpy as np


def euler_method(initial, n, dt, r_s):
    t      = np.ones(n) * initial[0]
    r      = np.ones(n) * initial[1]
    theta  = np.ones(n) * initial[2]
    phi    = np.ones(n) * initial[3]
    v_0    = np.ones(n) * initial[4]
    v_1    = np.ones(n) * initial[5]
    v_2    = np.ones(n) * initial[6]
    v_3    = np.ones(n) * initial[7]

    for i in range(1, n):
        v_0[i] = (-r_s / (r[i-1] * (r[i-1] - r_s)) * v_0[i - 1] * v_1[i - 1]) * dt + v_0[i - 1]
        v_1[i] = (-(r_s * (r[i-1] - r_s) / (2.0 * r[i-1] ** 3)) * v_0[i - 1] ** 2 + (r_s / (2 * r[i-1] * (r[i-1] - r_s))) *
                  v_1[i - 1] ** 2 + (r[i-1] - r_s) * (v_2[i - 1] ** 2 + np.sin(theta[i-1]) ** 2 * v_3[i - 1] ** 2)) * dt + v_1[i - 1]
        v_2[i] = (- (2.0 / r[i-1]) * v_2[i - 1] * v_1[i - 1] + np.sin(theta[i-1]) * np.cos(theta[i-1]) * v_3[i - 1] ** 2) * dt + v_2[
            i - 1]
        v_3[i] = (- (2.0 / r[i-1]) * v_1[i - 1] * v_3[i - 1] - 2 * (np.cos(theta[i-1]) / np.sin(theta[i-1])) * v_2[i - 1] * v_3[
            i - 1]) * dt + v_3[i - 1]
        t[i] = v_0[i - 1] * dt + t[i - 1]
        r[i] = v_1[i - 1] * dt + r[i - 1]
        theta[i] = v_2[i - 1] * dt + theta[i - 1]
        phi[i] = v_3[i - 1] * dt + phi[i - 1]
    return [t, r, theta, phi, v_0, v_1, v_2, v_3]


def python_solver(initial_values, t, r_s, c):
    t, r, theta, phi, v_zero, v_one, v_two, v_three = initial_values
    d_v_zero = - r_s / (r * (r - r_s)) * v_zero * v_one
    d_v_one = - (r_s * (r - r_s) / (2.0 * r ** 3)) * v_zero ** 2 + (r_s / (2 * r * (r - r_s))) * v_one ** 2 + \
                  (r - r_s) * (v_two ** 2 + np.sin(theta) ** 2 * v_three ** 2)
    d_v_two = - (2.0 / r) * v_two * v_one + np.sin(theta) * np.cos(theta) * v_three ** 2
    d_v_three = -(2.0 / r) * v_one * v_three - 2 * (np.cos(theta) / np.sin(theta)) * v_two * v_three
    d_t = v_zero
    d_r = v_one
    d_theta = v_two
    d_phi = v_three
    return [d_t, d_r, d_theta, d_phi, d_v_zero, d_v_one, d_v_two, d_v_three]
