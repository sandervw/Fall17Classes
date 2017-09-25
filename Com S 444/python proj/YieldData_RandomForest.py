# Import all modules and functions
# Works with Python 3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn import preprocessing

# Read the training and testing files
train = pd.read_csv("./YieldData_P3/(Train)WeatherDataset_NA.csv",sep=',')
test = pd.read_csv("./YieldData_P3/(Test)WeatherDataset_NA.csv",sep=',')

# We replace the "NAs" with the median of that column.
for col in [np.r_[4:20]]:
    train.iloc[:,col] = train.iloc[:,col].fillna(train.iloc[:,col].median())
    test.iloc[:,col] = test.iloc[:,col].fillna(test.iloc[:,col].median())

# Random Forest in Scikit-Learn can't handle string variables. Here, we convert the string class labels into integers.
le = preprocessing.LabelEncoder()
train.Yield = le.fit_transform(train.Yield)
test.Yield = le.fit_transform(test.Yield)

# We can view the order in which the labels are encoded (default is to encode them based on the first occurence)
le.classes_

# We define our Random Forest Classifier and fit it to the training and testing data.
# Then we make predictions to get the predicted probability and class.
# Finally, we view the classifier performance metrics for predictions on the test data.

rf = RandomForestClassifier(n_estimators=500, oob_score=True, random_state=1)
rf.fit(train.drop(['Yield', 'County'], axis=1),train.Yield)
probs = rf.predict_proba(test.drop(['Yield', 'County'], axis=1))
results = rf.predict(test.drop(['Yield', 'County'], axis=1))
print("Confusion Matrix: ", '\n', list(le.classes_), '\n', metrics.confusion_matrix(test.Yield,results))
print("Accuracy: ", metrics.accuracy_score(test.Yield,results))
print(metrics.classification_report(test.Yield, results))

# We extract the feature importance from the Random Forest Classifier and visualize them.
importances = rf.feature_importances_
indices = np.argsort(importances)
features = train.drop(['Yield', 'County'], axis=1).columns
plt.title('Feature Importances')
plt.barh(range(len(indices)), importances[indices], color='b', align='center')
plt.yticks(range(len(indices)), features[indices]) ## removed [indices]
plt.xlabel('Relative Importance')
plt.show()
