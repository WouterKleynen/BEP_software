import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img

# reading the image
testImage = img.imread('out.png')

# displaying the image
plt.imshow(testImage)

ax = plt.figure().add_subplot(projection='3d')

# Plot a sin curve using the x and y axes.
x = np.linspace(0, 1, 100)
y = np.sin(x * 2 * np.pi) / 2 + 0.5
ax.plot(x, y, zs=-10, zdir='z', label='curve in (x, y)')
ax.plot(x, y, zs=10, zdir='z', label='curve in (x, y)')


# Make legend, set axes limits and labels
ax.legend()
ax.set_xlim(0, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-10, 10)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()