import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import confusion_matrix, matthews_corrcoef
from sklearn import preprocessing
from sklearn import tree;
from sklearn.datasets import load_iris;
import graphviz;

# Read the training and testing files
train = pd.read_csv("yield.train.csv",sep=',')
test = pd.read_csv("yield.test.csv",sep=',')

# We replace the "NAs" with the median of that column.
for col in [np.r_[4:20]]:
    train.iloc[:,col] = train.iloc[:,col].fillna(train.iloc[:,col].median())
    test.iloc[:,col] = test.iloc[:,col].fillna(test.iloc[:,col].median())

# Random Forest in Scikit-Learn can't handle string variables. Here, we convert the string class labels into integers.
le = preprocessing.LabelEncoder()
train.Yield = le.fit_transform(train.Yield)
test.Yield = le.fit_transform(test.Yield)

# We can view the order in which the labels are encoded (default is to encode them based on the first occurence)
print(le.classes_)


clf = tree.DecisionTreeClassifier(max_depth=4)

clf = clf.fit(train.drop(['Yield', 'County'], axis=1),train.Yield)

results = clf.predict(test.drop(['Yield', 'County'], axis=1))

features = train.drop(['Yield', 'County'], axis=1).columns

featureImportances = clf.feature_importances_

print(matthews_corrcoef(test.Yield, results))

print features

print featureImportances


#dot_data = tree.export_graphviz(clf, out_file="iris.dot", 
                         #feature_names=iris.feature_names,  
                         #class_names=iris.target_names,  
                         #filled=True, rounded=True,  
                         #special_characters=True);

#graph = graphviz.Source(dot_data);

#dot -Tpng iris.dot -o iris.png
