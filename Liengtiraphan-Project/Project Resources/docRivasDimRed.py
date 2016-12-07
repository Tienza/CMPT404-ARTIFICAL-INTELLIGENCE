import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
X = np.genfromtxt('Dataset/IP-Port.csv', delimiter=' ')
pca = PCA(n_components=2, random_state=0)
pca.fit(X) 
X_pca = pca.fit_transform(X) 


plt.plot(X_pca[:, 0], X[:, 1], '.')
plt.show()
