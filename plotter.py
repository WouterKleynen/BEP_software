import matplotlib.pyplot as plt
import numpy as np
import conversion_coordinate_system as ccs


def plot_trajectories(t, r, theta, phi, text):
    plt.plot(t, r * np.cos(theta), label="Z = r*cos(theta)")  # plot Z
    plt.plot(t, r * np.sin(theta) * np.sin(phi % (2 * np.pi)), label="Y = r*sin(theta)sin(phi)")  # plot Y
    plt.plot(t, r * np.sin(theta) * np.cos(phi % (2 * np.pi)), label="X = r*sin(theta)cos(phi)")  # plot X
    plt.legend()
    plt.title(text)
    plt.show()


def plot_phi_to_theta(phi, theta, title):
    plt.plot(phi % (2 * np.pi), theta, label="phi")  # plot Z
    plt.title("phi plotted to theta " + title)
    plt.show()


def plot_point_in_three_dimension(X, Y, Z):
    fig = plt.figure(figsize=(4, 4))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(X, Y, Z)
    plt.show()


def plot_three_dimensional_spherical(r, theta, phi, text):
    fig = plt.figure(figsize=(5, 5), dpi=100)
    ax = fig.add_subplot(111, projection='3d')
    ax.set_aspect('auto')
    x, y, z = ccs.conversion_coordinate_spherical_to_cartesian(r, theta, phi)
    ax.plot(x, y, z, 'r', lw=2)
    plt.title(text)
    plt.show()


def plot_three_dimensional_spherical_with_starting_point(r, theta, phi):
    plot_point_in_three_dimension(r, theta, phi)
    fig = plt.figure(figsize=(5, 5), dpi=100)
    ax = fig.add_subplot(111, projection='3d')
    ax.set_aspect('auto')

    z = r * np.cos(theta)  # plot the curve
    y = r * np.sin(theta) * np.sin(phi % (2 * np.pi))
    x = r * np.sin(theta) * np.cos(phi % (2 * np.pi))

    ax.plot(x, y, z, 'r', lw=2)
    plt.show()


def plot_three_dimensional_spherical_with_unit_sphere(r, theta, phi, text):
    fig = plt.figure(figsize=(5, 5), dpi=100)
    ax = fig.add_subplot(111, projection='3d')
    ax.set_aspect('auto')

    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)

    x = r * np.outer(np.cos(u), np.sin(v))
    y = r * np.outer(np.sin(u), np.sin(v))
    z = r * np.outer(np.ones(np.size(u)), np.cos(v))

    ax.plot_surface(x, y, z, rstride=4, cstride=4, color='b', linewidth=0, alpha=0.5)

    z = np.cos(theta)  # plot the curve
    y = np.sin(theta) * np.sin(phi % (2 * np.pi))
    x = np.sin(theta) * np.cos(phi % (2 * np.pi))

    ax.plot(x, y, z, 'r', lw=2)
    plt.title(text)
    plt.show()

