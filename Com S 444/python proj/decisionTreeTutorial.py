"""
Created by David E. Hufnagel on Sep 18, 2017
For more information see http://scikit-learn.org/stable/modules/tree.html
"""
#in UNIX: conda install python-graphviz
import sys
from sklearn import tree
from sklearn.datasets import load_iris 
import graphviz
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.datasets import load_breast_cancer 

#Import the iris dataset, build a model using the training data, and view the tree splitting for that model
iris = load_iris()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data,iris.target)

dot_data = tree.export_graphviz(clf, out_file="iris.dot", feature_names=iris.feature_names, class_names=iris.target_names, filled=True, rounded=True, special_characters=True)
#In UNIX: dot -Tpng iris.dot -o iris.png
#open the .png file then plot the decision surface before comparing

#Plot the decision surface
#Graph Decision surface
n_classes = 3
plot_colors = "bry"
plot_step = 0.02

for pairidx, pair in enumerate([[0, 1], [0, 2], [0, 3],
                                [1, 2], [1, 3], [2, 3]]):
    # We only take the two corresponding features
    X = iris.data[:, pair]
    y = iris.target

    # Train
    clf = tree.DecisionTreeClassifier().fit(X, y)

    # Plot the decision boundary
    plt.subplot(2, 3, pairidx + 1)

    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, plot_step),
                         np.arange(y_min, y_max, plot_step))

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    cs = plt.contourf(xx, yy, Z, cmap=plt.cm.Paired)

    plt.xlabel(iris.feature_names[pair[0]])
    plt.ylabel(iris.feature_names[pair[1]])
    plt.axis("tight")

    # Plot the training points
    for i, color in zip(range(n_classes), plot_colors):
        idx = np.where(y == i)
        plt.scatter(X[idx, 0], X[idx, 1], c=color, label=iris.target_names[i],
                    cmap=plt.cm.Paired)

    plt.axis("tight")

plt.suptitle("Decision surface of a decision tree using paired features")
plt.legend()
plt.show()

#Look at the file and learn about what the tree contains and how the splitting decision was made



#Show that different parameters can change the tree
clf = tree.DecisionTreeClassifier()
clf = tree.DecisionTreeClassifier(max_depth=3)
clf = clf.fit(iris.data,iris.target)

dot_data = tree.export_graphviz(clf, out_file="iris2.dot", feature_names=iris.feature_names, class_names=iris.target_names, filled=True, rounded=True, special_characters=True)
#In UNIX: dot -Tpng iris2.dot -o iris2.png
#open the .png file and checkout the tree



#Build the tree for the breast cancer dataset
bc = load_breast_cancer()
clf = tree.DecisionTreeClassifier()
clf = clf.fit(bc.data, bc.target)



bc_dot = tree.export_graphviz(clf, out_file="bc.dot", feature_names=bc.feature_names, class_names=bc.target_names, filled=True, rounded=True, special_characters=True)
#In UNIX: dot -Tpng tree.dot -o tree.png

#Look at the file and learn about what the tree contains