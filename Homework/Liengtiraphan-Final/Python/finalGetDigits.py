import numpy as np
from numpy import genfromtxt

def getDataSet():
    # Read digits data & split it into X and y for training and testing
    dataset = genfromtxt('../Documents/Dataset/features.csv', delimiter=' ')
    y = dataset[:, 0]
    X = dataset[:, 1:]

    dataset = genfromtxt('../Documents/Dataset/features-t.csv', delimiter=' ')
    y_te = dataset[:, 0]
    X_te = dataset[:, 1:]
    return X, y, X_te, y_te