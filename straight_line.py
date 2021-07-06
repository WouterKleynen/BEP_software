import matplotlib.pyplot as plt
import numpy as pp

fig, ppool = plt.subplots()

t = pp.arange(0.0, 1.0, 0.001)
s = t
line = ppool.plot(t, s, lw=2)
plt.scatter([0, 1], [0, 1])
plt.annotate("       Point A", (0, 0))
plt.annotate("   Point B", (1, 1))
plt.axis('off')

plt.show()
