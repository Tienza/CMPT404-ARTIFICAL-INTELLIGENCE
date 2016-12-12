"""
================================
Nearest Neighbors Classification
================================
Modified in class by Dr. Rivas
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.cluster import KMeans
from sklearn import metrics
from sklearn.metrics import pairwise_distances
from numpy import genfromtxt
from sklearn.model_selection import KFold
import time


# read digits data & split it into X (training input) and y (target output)
X = genfromtxt('Dataset/IP-Port.csv', delimiter=' ')


plt.plot(X[:,0], X[:,1], '.')
plt.plot(X[:,0], X[:,2], 'r.')
plt.show()

bestk=[]
kc=0
for clusters in range(2,101,1):
  kf = KFold(n_splits=10)
  #clusters = 85
  kscore=[]
  k=0
  for train, test in kf.split(X):
    #print("%s %s" % (train, test))
    X_train, X_test = X[train], X[test]
  
    #time.sleep(100)
  
    # we create an instance of Neighbors Classifier and fit the data.
    clf = KMeans(n_clusters=clusters)
    clf.fit(X_train)
 
    labels = clf.labels_ 
    kscore.append(metrics.silhouette_score(X_train, labels, metric='euclidean'))
    print(kscore[k])
    k=k+1
  
  print (clusters)
  bestk.append(sum(kscore)/len(kscore))
  print(bestk[kc])
  kc+=1

# to do here: given this array of E_outs in CV, find the max, its 
# corresponding index, and its corresponding value of clusters
print(bestk)
