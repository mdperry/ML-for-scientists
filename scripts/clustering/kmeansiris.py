#!/usr/bin/env python
"""Demonstration of logistic regression and the iris dta set."""

import numpy 
import numpy.random
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import sklearn
import sklearn.datasets
import sklearn.cluster

def kmeansDemo(filename=None, **kwargs):
    iris = sklearn.datasets.load_iris()
    X = iris.data
    y = iris.target

    usedims = [0,2]
    model = sklearn.cluster.KMeans(n_clusters=3)
    model.fit(X)
    centers =  model.cluster_centers_

    cmap_light = colors.ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
    cmap_bold = colors.ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

    # Plot also the training points
    for i in range(3):
        idxs = numpy.where(y == i)
        plt.scatter(X[idxs, usedims[0]], X[idxs, usedims[1]], c=y[idxs], cmap=cmap_light, alpha=0.45)
        plt.scatter([centers[i,usedims[0]]], [centers[i,usedims[1]]], c='k', marker='x', s=20)

    plt.xlabel(iris.feature_names[usedims[0]])
    plt.ylabel(iris.feature_names[usedims[1]])

    outputPlot(filename)


def outputPlot(filename=None):
    if filename is None:
        plt.show()
    else:
        plt.savefig(filename, transparent=True)
        plt.close()

if __name__ == '__main__':
    base = 'outputs/clustering/'
    kmeansDemo(filename=base+'kmeans-demo.png')
