import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# Line chart


x = [0,1,2,3,4]
y = [0,2,4,6,8]

# Resixe your graph
plt.figure(figsize=(5,3), dpi=100)

#plt.plot(x, y, label='2x', color='red', linewidth=2, marker='.', linestyle='--', markersize='12', markeredgecolor='blue')
# use shorthand notation
# fmt = [color][marker][line]
plt.plot(x, y, 'r.--', label='2x')


#line number two
x2 = np.arange(0,4.5,0.5)

# pick slices to show
plt.plot(x2[:5], x2[:5]**2, label='x**2')
plt.plot(x2[4:], x2[4:]**2, 'b--')


plt.title('our first graph', fontdict={'fontname': 'Comic Sans Ms', 'fontsize': 20})
plt.xlabel('X axis')
plt.ylabel('y axis')
plt.legend()
plt.savefig('graph.png')
#plt.xticks([0,1,2,3,4])
#plt.yticks([0,2,4,6,8,10])
plt.show();

