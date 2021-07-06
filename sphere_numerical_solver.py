import numpy as np


def euler_method_sphere(initial, n, dt):
    theta = np.ones(n)*initial[0]
    phi  = np.ones(n)*initial[1]
    v_1  = np.ones(n)*initial[2]
    v_2  = np.ones(n)*initial[3]

    for i in range(1, n):
        v_1[i] = (np.cos(theta[i - 1]) * np.sin(theta[i - 1]) * v_2[i - 1] ** 2) * dt + v_1[i - 1]
        v_2[i] = (-2 * (np.cos(theta[i - 1]) / np.sin(theta[i - 1])) * v_1[i - 1] * v_2[i - 1]) * dt + v_2[i - 1]
        theta[i] = v_1[i - 1] * dt + theta[i - 1]
        phi[i] = v_2[i - 1] * dt + phi[i - 1]
    return [theta, phi, v_1, v_2]


def python_solver_sphere(variables, t):
    v_1, v_2, theta, phi = variables
    dv_1 = np.cos(theta) * np.sin(theta) * v_2 ** 2
    dv_2 = -2 * (np.cos(theta) / np.sin(theta)) * v_1 * v_2
    d_theta = v_1
    d_phi = v_2
    return [dv_1, dv_2, d_theta, d_phi]
