from sklearn import tree;
from sklearn.datasets import load_iris;
import graphviz;

iris = load_iris();
clf = tree.DecisionTreeClassifier();
clf = clf.fit(iris.data, iris.target);

dot_data = tree.export_graphviz(clf, out_file="iris.dot", 
                         feature_names=iris.feature_names,  
                         class_names=iris.target_names,  
                         filled=True, rounded=True,  
                         special_characters=True);

graph = graphviz.Source(dot_data);

#dot -Tpng iris.dot -o iris.png

graph;
