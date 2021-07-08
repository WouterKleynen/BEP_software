import numpy as np


def euler_method(initial, n, dt):
    r = np.ones(n)*initial[0]
    theta = np.ones(n)*initial[1]
    phi  = np.ones(n)*initial[2]
    v_1  = np.ones(n)*initial[3]
    v_2  = np.ones(n)*initial[4]
    v_3 = np.ones(n)*initial[5]
    for i in range(1, n):
        v_1[i] = (r[i - 1] * v_2[i - 1] ** 2 + r[i - 1] * np.sin(theta[i - 1]) ** 2 * v_3[i - 1] ** 2) * dt + v_1[i - 1]
        v_2[i] = (-2 * v_2[i - 1] * v_1[i - 1] / r[i - 1] + np.sin(theta[i - 1]) * np.cos(theta[i - 1]) * v_3[
            i - 1] ** 2) * dt + v_2[i - 1]
        v_3[i] = (-2 * v_3[i - 1] * v_1[i - 1] / r[i - 1] - 2 * np.cos(theta[i - 1]) / np.sin(theta[i - 1]) * v_2[
            i - 1] * v_3[i - 1]) * dt + v_3[i - 1]
        r[i] = v_1[i - 1] * dt + r[i - 1]
        theta[i] = v_2[i - 1] * dt + theta[i - 1]
        phi[i] = v_3[i - 1] * dt + phi[i - 1]
    return [r, theta, phi, v_1, v_2, v_3]


def python_solver(variables, t):
    r, theta, phi, v_one, v_two, v_three = variables
    d_v_one   = r * v_two ** 2 + r * np.sin(theta) ** 2 * v_three ** 2
    d_v_two   = -2*(v_two * v_one) / r + np.sin(theta) * np.cos(theta) * v_three ** 2
    d_v_three = -2*(v_three * v_one) / r - 2*np.cos(theta) / np.sin(theta) * v_two * v_three
    d_r       = v_one
    d_theta   = v_two
    d_phi     = v_three
    return [d_r, d_theta, d_phi, d_v_one, d_v_two, d_v_three]

