import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


x = np.arange(0,4.5,0.5)
plt.figure(figsize=(6,4), dpi=100)
plt.plot(x[:4], x[:4]**2, 'r.-', label='2x')
plt.plot(x[3:], x[3:]**2, 'b.--', label='x2')
plt.plot([0.1,0.2,0.3],[-0.3,-0.2,-0.1])
plt.xlabel('X-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show()