"""
================================
Spectral Clustering
================================
Modified on 2016-12-06 by Piradon Liengtiraphan with help from Dr. Rivas
"""

import matplotlib.pyplot as plt
from sklearn import metrics
from numpy import genfromtxt
from sklearn.model_selection import KFold
from sklearn.cluster import SpectralClustering
import os
import time

# Start Timer
start_time = time.time()

# How many times to run KMeans.py
run_times = 1

for i in range(run_times):
    # read digits data & split it into X (training input) and y (target output)
    X = genfromtxt('Dataset/IP-Port.csv', delimiter=' ')

    plt.plot(X[:, 0], X[:, 1], '.')
    plt.plot(X[:, 0], X[:, 2], 'r.')
    # plt.show()

    bestk = []
    kc = 0
    result_num = len(os.listdir('KMeans_Results'))
    with open('Spectral_Clustering_Results/spectral_clustering_results' + str(result_num) + '.txt', 'w') as file:
        for clusters in range(2, 101, 1):
            kf = KFold(n_splits=10)
            # clusters = 85
            kscore = []
            k = 0

            print("============ Spectral Score ============")
            file.writelines("============ Spectral Score ============" + "\n")
            for train, test in kf.split(X):
                #print("%s %s" % (train, test))
                X_train, X_test = X[train], X[test]

                #time.sleep(100)

                # we create an instance of Neighbors Classifier and fit the data.
                clf = SpectralClustering(n_clusters=clusters)
                clf.fit(X_train)

                labels = clf.labels_
                kscore.append(metrics.silhouette_score(X_train, labels, metric='euclidean'))

                print(kscore[k])
                file.writelines(str(kscore[k]) + "\n")
                k=k+1

            print("============ Clusters ============")
            file.writelines("============ Clusters ============" + "\n")
            print (clusters)
            file.writelines(str(clusters) + "\n")
            bestk.append(sum(kscore)/len(kscore))
            print("============ Best Spectral[Spectral] ============")
            print(bestk[kc])
            file.writelines("============ Best Spectral[Spectral] ============" + "\n")
            file.writelines(str(bestk[kc]) + "\n")
            kc+=1

            # to do here: given this array of E_outs in CV, find the max, its
            # corresponding index, and its corresponding value of clusters
            print("============ Best Spectral Array ============")
            file.writelines("============ Best Spectral Array ============" + "\n")
            print(bestk)
            file.writelines(str(bestk) + "\n")

        print("============ Best Spectral ============")
        file.writelines("============ Best Spectral ============" + "\n")
        print(max(bestk))
        file.writelines(str(max(bestk)) + "\n")
        print("============ Best Spectral Index ============")
        file.writelines("============ Best Spectral Index ============" + "\n")
        print(bestk.index(max(bestk)))
        file.writelines(str(bestk.index(max(bestk))) + "\n")

        # Calculates Running Time
        run_time = time.time() - start_time
        minutes, seconds = divmod(run_time, 60)
        hours, minutes = divmod(minutes, 60)
        print("============ Running Time ============")
        file.writelines("============ Running Time ============" + "\n")
        print("Seconds Time Format --- %s seconds ---" % (time.time() - start_time))
        print("Normal Time Format --- %d:%02d:%02d ---" % (hours, minutes, seconds))
        file.writelines(str("Seconds Time Format --- %s seconds ---" % (time.time() - start_time) + "\n"))
        file.writelines(str("Normal Time Format --- %d:%02d:%02d ---" % (hours, minutes, seconds)))