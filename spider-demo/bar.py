# Bar chart

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

labels = ['A', 'B', 'C']
values = [1, 4, 2]

bars = plt.bar(labels, values)
#bars[0].set_hatch('/')
#bars[1].set_hatch('o')
#bars[2].set_hatch('*')

patterns = ['/', 'o', '*']
for bar in bars:
    bar.set_hatch(patterns.pop(0))

plt.figure(figsize=(6, 4), dpi=100)

plt.show()