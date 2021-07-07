import numpy as np
import matplotlib.pyplot as plt
import cv2

# Read the image with Opencv
img = cv2.imread('input_image')
# Change the color from BGR to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Orgird to store data
x, y = np.ogrid[0:img.shape[0], 0:img.shape[1]]
# In Python3 matplotlib assumes rgbdata in range 0.0 to 1.0
img = img.astype('float32')/255
fig = plt.Figure()
# gca do not work thus use figure objects inbuilt function.
ax = fig.add_subplot(projection='3d')

# Plot data
ax.plot_surface(x-50, y-50, np.atleast_2d(0)-10, rstride=10, cstride=10, facecolors=img, label="TEST")
ax.plot_surface(x-50, y-50, np.atleast_2d(0)+10, rstride=10, cstride=10, facecolors=img, label="NO")

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

fig.savefig('output_image')

