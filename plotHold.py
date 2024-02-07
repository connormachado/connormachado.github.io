import matplotlib.pyplot as plt
import numpy as np


xPos = [175.2890625, 245.67578125, 301.953125, 271.0, 176.29296875]
yPos = [595.4140625, 633.90625, 587.30078125, 512.6171875, 595.6640625]


xpoints = np.array( xPos )
ypoints = np.array( yPos )


ax = plt.gca()
ax.set_xlim([0, 740]) #1284
ax.set_ylim([0, 1073]) #2280
plt.plot(xpoints, ypoints)
plt.show()
