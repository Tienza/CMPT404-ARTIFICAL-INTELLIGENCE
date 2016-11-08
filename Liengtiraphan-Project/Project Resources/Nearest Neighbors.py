"""
================================
Nearest Neighbors Classification
================================
Modified in class by Dr. Rivas
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import neighbors
from numpy import genfromtxt
from sklearn.model_selection import KFold
import time


# read digits data & split it into X (training input) and y (target output)
X, y, ytrue = genfromtxt('Dataset/IP-Port.csv', delimiter=' ')

X = X.reshape(len(X),1)
y = y.reshape(len(y),1)
ytrue = ytrue.reshape(len(ytrue),1)

plt.plot(X, y, '.')
plt.plot(X, ytrue, 'rx')
plt.show()

bestk=[]
kc=0
for n_neighbors in range(1,101,2):
  kf = KFold(n_splits=10)
  #n_neighbors = 85
  kscore=[]
  k=0
  for train, test in kf.split(X):
    #print("%s %s" % (train, test))
    X_train, X_test, y_train, y_test = X[train], X[test], y[train], y[test]
  
    #time.sleep(100)
  
    # we create an instance of Neighbors Classifier and fit the data.
    clf = neighbors.KNeighborsRegressor(n_neighbors, weights='distance')
    clf.fit(X_train, y_train)
  
    kscore.append(clf.score(X_test,y_test))
    #print kscore[k]
    k=k+1
  
  print (n_neighbors)
  bestk.append(sum(kscore)/len(kscore))
  print(bestk[kc])
  kc+=1

# to do here: given this array of E_outs in CV, find the max, its 
# corresponding index, and its corresponding value of n_neighbors
print(bestk)
