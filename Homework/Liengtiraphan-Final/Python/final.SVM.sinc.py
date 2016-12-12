import finalGenData
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.svm import SVR
from sklearn.model_selection import KFold

# number of samples
N = 1000

# generate data & split it into X (training input) and y (target output)
X, y = finalGenData.genDataSet(N)

# linear regression solution
w=np.linalg.pinv(X.T.dot(X)).dot(X.T).dot(y)


#penC  <- Penalty parameter C of the error term
#tubEpsilon  <- the epsilon-tube within which no penalty is associated
result_num = len(os.listdir('../Documents/final.SVM.sinc.py_Results'))
with open('../Documents/final.SVM.sinc.py_Results/final.SVM.sinc.results' + str(result_num) + '.txt', 'w') as file:
  bestC=0
  bestEpsilon=0
  bestGamma=0
  bestScore=float('-inf')
  score=0
  print("============ CV Score ============")
  file.writelines("============ CV Score ============" + "\n")
  for penC in np.logspace(-5, 15, num=11, base=2):
    for tubEpsilon in np.linspace(0, 1, num=11):
      for paramGamma in np.logspace(-15, 3, num=10, base=2):
        kf = KFold(n_splits=10)
        cvscore=[]
        for train, validation in kf.split(X):
          X_train, X_validation, y_train, y_validation = X[train, :], X[validation, :], y[train], y[validation]
          # here we create the SVR
          svr =  SVR(C=penC, epsilon=tubEpsilon, gamma=paramGamma, kernel='rbf', verbose=False)
          # here we train the SVR
          svr.fit(X_train, y_train)
          # now we get E_out for validation set
          score=svr.score(X_validation, y_validation)
          cvscore.append(score)

        # average CV score
        score=sum(cvscore)/len(cvscore)
        if (score > bestScore):
          bestScore=score
          bestC=penC
          bestEpsilon=tubEpsilon
          bestGamma=paramGamma
          print("C " + str(penC) + ", epsilon " + str(tubEpsilon) + ", gamma " + str(paramGamma) + ". Testing set CV score: %f" % score)
          file.writelines("C " + str(penC) + ", epsilon " + str(tubEpsilon) + ", gamma " + str(paramGamma) + ". Testing set CV score: %f" % score + "\n")

  # here we get a new training dataset
  X, y = finalGenData.genDataSet(N)
  # here we create the final SVR
  svr =  SVR(C=bestC, epsilon=bestEpsilon, gamma=bestGamma, kernel='rbf', verbose=True)
  # here we train the final SVR
  svr.fit(X, y)

  # E_out in training
  print("============ E_out in Training ============")
  file.writelines("============ E_out in Training ============" + "\n")
  print("Training set score: %f" % svr.score(X, y))
  file.writelines("Training set score: %f" % svr.score(X, y) + "\n")
  # here we get a new testing dataset
  X, y = finalGenData.genDataSet(N)
  # here test the final SVR and get E_out for testing set
  ypred=svr.predict(X)
  score=svr.score(X, y)
  print("============ Testing Set Score ============")
  file.writelines("============ Testing Set Score ============" + "\n")
  print("Testing set score: %f" % score)
  file.writelines("Testing set score: %f" % score + "\n")
  plt.plot(X[:, 0], X[:, 1], '.')
  plt.plot(X[:, 0], y, 'rx')
  plt.plot(X[:, 0], ypred, '-k')
  ypredLR=X.dot(w)
  plt.plot(X[:, 0], ypredLR, '--g')
  plt.show()
