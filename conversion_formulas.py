import numpy as np


def atan2(Y, X):
    if X > 0:
        return np.arctan(float(Y)/float(X))
    if X < 0 and Y >= 0:
        return np.arctan(float(Y)/float(X)) + np.pi
    if X < 0 and Y < 0:
        return np.arctan(float(Y) / float(X)) - np.pi
    if X == 0 and Y > 0:
        return np.pi/2.0
    if X == 0 and Y < 0:
        return -np.pi/2.0


def cartesian_to_spherical(X, Y, Z):
    r = np.sqrt(X**2+Y**2+Z**2)
    theta = np.arccos(float(Z)/float(r))
    phi = atan2(Y, X)
    return r, theta, phi


def spherical_to_cartesian(r, theta, phi):
    X = r * np.sin(theta) * np.cos(phi)
    Y = r * np.sin(theta) * np.sin(phi)
    Z = r * np.cos(theta)
    return X, Y, Z


def velocity_cartesian_to_spherical(X, Y, Z, v_X, v_Y, v_Z):
    X = float(X)
    Y = float(Y)
    Z = float(Z)
    r = np.sqrt(X**2+Y**2+Z**2)
    factor = X**2 + Y**2
    v_1 = (X / r) * v_X + (Y / r) * v_Y + (Z / r) * v_Z
    v_2 = (X*Z)/(np.sqrt(factor)*(r**2))*v_X + (Y*Z)/(np.sqrt(factor)*(r**2))*v_Y + -factor/(np.sqrt(factor)*(r**2))*v_Z
    v_3 = -Y/factor*v_X + X/factor*v_Y
    return v_1, v_2, v_3


def form_bol_three_dimensional_vector(X, Y, Z, v_X, v_Y, v_Z):
    r, theta, phi = cartesian_to_spherical(X, Y, Z)
    v_1, v_2, v_3 = velocity_cartesian_to_spherical(X, Y, Z, v_X, v_Y, v_Z)
    return [r, theta, phi, v_1, v_2, v_3]


def form_bol_four_dimensional_vector(X, Y, Z, v_X, v_Y, v_Z, r_s):
    r, theta, phi = cartesian_to_spherical(X, Y, Z)
    v_1, v_2, v_3 = velocity_cartesian_to_spherical(X, Y, Z, v_X, v_Y, v_Z)
    v_0 = schwarzschild_v_0(v_1, v_2, v_3, r_s, r, theta)
    return [0, r, theta, phi, v_0, v_1, v_2, v_3]


def schwarzschild_v_0(v_1, v_2, v_3, r_s, r, theta):
    g_00 = (1.0 - float(r_s) / float(r))
    g_11 = -(1.0/(1.0-float(r_s)/float(r)))
    g_22 = -r**2
    g_33 = -r ** 2 * np.sin(theta)
    v_0 = np.sqrt((-v_1**2 * g_11 - v_2 ** 2 * g_22 - v_3 ** 2 * g_33)/g_00)
    return v_0

