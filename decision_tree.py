# -*- coding: utf-8 -*-
"""1nt20is047_lab2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HxDDt9MMmu2WHxIE_PgRmwD5F3xCkJKd
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import metrics
from sklearn import tree
data=pd.read_csv('zoo_data(For Decision Tree Program).csv')
data

X=data.iloc[:, :-1]
y=data.iloc[:,-1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=42) # 70% training and 30% test
 #Create Decision Tree classifer object
model = DecisionTreeClassifier()

# Train Decision Tree Classifer
model = model.fit(X_train,y_train)

#Predict the response for test dataset
y_pred = model.predict(X_test)

# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred)*100)

from sklearn import tree
tree.plot_tree(model,filled=True)

text_representation = tree.export_text(model)
print(text_representation)