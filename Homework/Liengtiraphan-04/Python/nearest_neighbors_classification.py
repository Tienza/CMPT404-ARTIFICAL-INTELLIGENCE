"""
================================
Nearest Neighbors Classification
================================
Modified in class by Dr. Rivas
"""

import numpy as np
import matplotlib.pyplot as plt
import hw4_data_points as hw4
from matplotlib.colors import ListedColormap
from sklearn import neighbors
from numpy import genfromtxt
from sklearn.model_selection import KFold
import time

# read digits data & split it into X (training input) and y (target output)
X, y, ytrue = hw4.genDataSet(1000)#genfromtxt('features.csv', delimiter=' ')

X = X.reshape(len(X),1)
y = y.reshape(len(y),1)
ytrue = ytrue.reshape(len(ytrue),1)
'''y = np.array(dataset)[:, 0]
X = np.array(dataset)[:, 1:]
y[y != 0] = -1  # rest of numbers are negative class
y[y == 0] = +1  # number zero is the positive class'''

bestk = []
kc = 0
for n_neighbors in range(1, 900, 2):
    kf = KFold(n_splits=10)
    #n_neighbors = 2
    kscore = []
    k = 0
    for train, test in kf.split(X):
        # print("%s %s" % (train, test))
        X_train, X_test, y_train, y_test = X[train], X[test], y[train], y[test]

        # time.sleep(100)

        # we create an instance of Neighbors Classifier and fit the data.
        clf = neighbors.KNeighborsRegressor(n_neighbors, weights='distance')
        clf.fit(X_train, y_train)

        kscore.append(abs(clf.score(X_test, y_test)))
        # print kscore[k]
        k = k + 1

    print(n_neighbors)
    bestk.append(sum(kscore) / len(kscore))
    print(bestk[kc])
    kc += 1


# to do here: given this array of E_outs in CV, find the max, its
# corresponding index, and its corresponding value of n_neighbors
new_bestk = sorted(bestk, reverse=True)
get_index = [new_bestk[0], new_bestk[1], new_bestk[2]]

print(sorted(bestk, reverse=True))
print("")
for i in get_index:
    print("Idex of " + str(i) + "in bestk: " + str(bestk.index(i)))
    print("n_neighbors of " + str(i) + " in bestk: " + str(bestk.index(i) + (bestk.index(i) + 1)))
    print("")
print("")
for i in range(3):
    print("Rank " + str(i+1) + ". " "CV E_out: " + str(new_bestk[i]))

# Write to File
with open('hw4_results.txt', 'w') as f:
    f.write(str(sorted(bestk, reverse=True)))
    f.write("\n")
    f.write("\n")
    for i in get_index:
        f.write("Index of " + str(i) + " in bestk: " + str(bestk.index(i)))
        f.write("\n")
        f.write("n_neighbors of " + str(i) + " in bestk: " + str(bestk.index(i) + (bestk.index(i) + 1)))
        f.write("\n")
        f.write("\n")
    f.write("\n")
    for i in range(3):
        f.write("Rank " + str(i+1) + ". " "CV E_out: " + str(new_bestk[i]))
        f.write("\n")