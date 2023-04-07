import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

fifa = pd.read_csv('fifa_data.csv')
fifa.head()

plt.figure(figsize=(8,5), dpi=100)
plt.title('Distribution of skill level in fifa 2018')
bins = [40,50,60,70,80,90,100]
plt.hist(fifa.Overall, bins=bins)
plt.xticks(bins)
plt.xlabel('Skill level')
plt.ylabel('Number of players')
plt.savefig('distribution.png')
plt.show();