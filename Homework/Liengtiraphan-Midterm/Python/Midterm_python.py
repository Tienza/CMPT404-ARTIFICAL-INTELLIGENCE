import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt

# Read digits data & split it into X (training input) and y (target output)
dataset = genfromtxt('features.csv', delimiter=' ')
y = dataset[:, 0]
X = dataset[:, 1:]
y[y!=1] = -1 # Rest of numbers are negative class
y[y==1] = +1 # Number zero, is the positive class

# Plots data
c0 = plt.scatter(X[y==-1,0], X[y==-1,1], s=20, color='r', marker='x')
c1 = plt.scatter(X[y==1,0], X[y==1,1], s=20, color='b', marker='o')

# Displays legend
plt.legend((c0, c1), ('All Other Numbers -1', 'Number Zero +1'), loc='upper right', scatterpoints=1, fontsize=11)

# Displays axis legends and title
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_1$')
plt.title(r'Intensity and Symmetry of Digits')

# Saves the figure into a .pdf file (desired!)
plt.savefig('midterm.plot.pdf', bbox_inches='tight')
plt.show()

print("Code has finished running...")