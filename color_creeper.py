#!/usr/bin/env python
# coding: utf-8

import numpy as np
import seaborn as sns
#import matplotlib as plt
from matplotlib import pyplot as plt


# Here is a matrix that will color a creeper
# The 0's are black, the 1's will be various colors of green
number_matrix = [
    [1, 1, 1, 1 ,1, 1, 1, 1],
    [1, 1, 1, 1 ,1, 1, 1, 1],
    [1, 0, 0, 1 ,1, 0, 0, 1],
    [1, 0, 0, 1 ,1, 0, 0, 1],
    [1, 1, 1, 0, 0, 1, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 0, 1, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]
# Mpw change out the 1's for various numbers to represent the different colors of a creeper

adjusted_matrix = []
for row in number_matrix:
    output_row = []
    for element in row:
        if element == 0:
            output_row.append(0)
        else:
            new_num = np.random.randint(3)+1
            output_row.append(new_num)
    adjusted_matrix.append(output_row)

cmap = ['black', 'green', 'seagreen', 'darkgreen']
fig, ax = plt.subplots(figsize=(8,8))
ax.legend([],[], frameon=False)
ax.set(yticklabels=[])
sns.heatmap(ax=ax, data=adjusted_matrix, cmap=cmap, cbar=False, yticklabels=False, xticklabels=False)
plt.savefig('Creeper.png')
