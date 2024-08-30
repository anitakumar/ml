# -*- coding: utf-8 -*-
"""overfitting and underfitting.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HHpJt1JgRmaCY-B-3vSZK63KPGaJ9CJu
"""

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from matplotlib import pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
import numpy as np



X,y = make_classification(n_samples=9000, n_features=18, n_informative=4, n_redundant=12, random_state=4)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

X_train.shape, X_test.shape, y_train.shape, y_test.shape

train_scores, test_scores = list(), list()

values =[ i for i in range(1,21)]

for i in values:
  model= DecisionTreeClassifier(max_depth=i)
  model.fit(X_train, y_train)
  train_yhat = model.predict(X_train)
  train_acc = accuracy_score(y_train, train_yhat)
  test_yhat = model.predict(X_test)
  test_acc = accuracy_score(y_test, test_yhat)
  train_scores.append(train_acc)
  test_scores.append(test_acc)

len(train_scores), len(test_scores)

plt.plot(values, train_scores, 'o-', label='Train')
plt.plot(values, test_scores, 'o-', label='Test')
plt.legend()
plt.show()

"""lower values is overfitting and then higher values it is overfitting"""



"""How to prevent overfitting and underfitting problem"""

from sklearn.model_selection import GridSearchCV

param_grid = {'criterion': ['gini','entropy'],'max_depth':[2,4,6,10,20],'min_samples_split':[5,10,20,50,100]}
clf= GridSearchCV(DecisionTreeClassifier(), param_grid, cv=3,n_jobs= 1,scoring='accuracy')
clf.fit(X_train, y_train)

clf.best_estimator_

"""The best crireion is entropy and use depth of 20"""



print(accuracy_score(y_train,clf.best_estimator_.predict(X_train)))
print(accuracy_score(y_test,clf.best_estimator_.predict(X_test)))