from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets

# load iris dataset
iris_bunch = load_iris()
iris = pd.DataFrame(iris_bunch.data, columns=iris_bunch.feature_names)
iris["group"] = iris_bunch.target

# reduce the dimensionality of the data to 2 dimensions using PCA
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(iris)

# create a scatter plot of the reduced data, colored by target values
plt.scatter(X_reduced[:, 0], X_reduced[:, 1], c=list(iris["group"]))
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('Iris Dataset PCA')
plt.show()

