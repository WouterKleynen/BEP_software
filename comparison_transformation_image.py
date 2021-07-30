import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def plot(input_path, output_path, r_s, x_size, y_size):
    xx, yy = np.meshgrid(np.linspace(-10, 10, x_size), np.linspace(10, -10, y_size))
    zz, yz = np.meshgrid(np.linspace(0, 0, x_size), np.linspace(0, 0, y_size))

    # create vertices for a rotated mesh (3D rotation matrix)
    X_low = xx
    Y_low = yy
    Z_low = -10 + zz

    X_high = xx
    Y_high = yy
    Z_high = 10 + zz
    # # create the figure
    fig = plt.figure()

    u = np.linspace(0, 2 * np.pi, 100)
    v = np.linspace(0, np.pi, 100)

    x = r_s * np.outer(np.cos(u), np.sin(v))
    y = r_s * np.outer(np.sin(u), np.sin(v))
    z = r_s * np.outer(np.ones(np.size(u)), np.cos(v))

    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X_low, Y_low, Z_low, rstride=1, cstride=1, facecolors=plt.imread(input_path)/255., shade=False)
    ax.plot_surface(X_high, Y_high, Z_high, rstride=1, cstride=1, facecolors=plt.imread(output_path)/255., shade=False)
    ax.plot_surface(x, y, z, rstride=4, cstride=4, color='k', linewidth=0)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

