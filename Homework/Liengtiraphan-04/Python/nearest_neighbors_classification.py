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
dataset = hw4.genDataSet(1000)#genfromtxt('features.csv', delimiter=' ')
y = np.array(dataset)[:, 0]
X = np.array(dataset)[:, 1:]
y[y != 0] = -1  # rest of numbers are negative class
y[y == 0] = +1  # number zero is the positive class

bestk = []
kc = 0
for n_neighbors in range(1, 1000, 2):
    kf = KFold(n_splits=3)
    n_neighbors = 2
    kscore = []
    k = 1
    for train, test in kf.split(X):
        # print("%s %s" % (train, test))
        X_train, X_test, y_train, y_test = X[train], X[test], y[train], y[test]

        # time.sleep(100)

        # we create an instance of Neighbors Classifier and fit the data.
        clf = neighbors.KNeighborsClassifier(n_neighbors, weights='distance')
        clf.fit(X_train, y_train)

        kscore.append(clf.score(X_test, y_test))
        # print kscore[k]
        k = k + 1

    print(n_neighbors)
    bestk.append(sum(kscore) / len(kscore))
    print(bestk[kc])
    kc += 1

# to do here: given this array of E_outs in CV, find the max, its
# corresponding index, and its corresponding value of n_neighbors
print(bestk)