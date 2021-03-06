# -*- coding: utf-8 -*-
"""Machine_learning_Wine Shop.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1m1kOXDcCv0tm3YLkOMY7Dm7j4zoiqhbl

#Basic Machine Learning Program:
"""

import numpy as np
import pandas as pd
import sklearn 
import seaborn as sns 
import matplotlib.pyplot as plt

data  = pd.read_csv("/content/winequality-red.csv")

data.head(6)

data.corr

data.columns

data.info()

data['quality'].unique()

#Check correleation between the variables using Seaborn's pairplot.
sns.pairplot(data)

from collections import Counter
Counter(data['quality'])

#Count the Result variable 
sns.countplot(x='quality', data = data)

#Plot the box plot to check the outliers
sns.boxplot('quality','fixed acidity', data = data)

data.describe()

#We have create new column called as Result.
# C - Bad
# B - Average
# A - Excellent
Result  = []
for i in data['quality']:
  if i >= 1 and i <= 3:
    Result.append('C')
  elif i >= 4 and i <= 7:
    Result.append('B')
  elif i >= 8 and i <= 10:
    Result.append('A')
data['Result'] = Result

data.columns

data['Result'].unique()

Counter(data['Result'])

#Split x and Y 
x = data.iloc[:,:11]
y = data['Result']

x.head(10)

y.head(10)

#Now Scale the data using standardScaler for PCA
from sklearn.preprocessing import StandardScaler
sc =StandardScaler()
x = sc.fit_transform(x)

#View the scales features 
print(x)

from sklearn.decomposition import PCA
pca  = PCA()
x_pca  = pca.fit_transform(x)

#Plot the graph to get principle components 
plt.figure(figsize=(16,8))
plt.plot(np.cumsum(pca.explained_variance_ratio_), 'ro-')
plt.grid()

pca_new = PCA(n_components=8)
x_new = pca_new.fit_transform(x)

print(x_new)

#Split the data into Train and Test data set 
# from sklearn.cross_validation import train_test_split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x_new, y, test_size = 0.25)

print(x_train.shape)
print(x_test.shape)
print(y_train.shape)
print(x_test.shape)

#Logistic Regression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix
lr =LogisticRegression()
lr.fit(x_train,y_train)
lr_predict = lr.predict(x_test)

#Print confusion_matrix AND accuracy_score
lr_conf_metrix = confusion_matrix(y_test,lr_predict)
lr_acc_metrix = accuracy_score(y_test,lr_predict)
print(lr_conf_metrix)
print(lr_acc_metrix)

sns.boxplot('Result','fixed acidity', data = data)

#Decision Tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
dt = DecisionTreeClassifier()
dt.fit(x_train, y_train)
dt_predict = dt.predict(x_test)

#Print confusion_matrix and accuracy_score
dt_conf_metrics = confusion_matrix(y_test,dt_predict)
dt_acc_metrix = accuracy_score(y_test,dt_predict)
print(dt_conf_metrics)
print(dt_acc_metrix* 100)

#Navie Bayers 
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score
nb = GaussianNB()
nb.fit(x_train,y_train)
nb_predict = nb.predict(x_test)

#Print confusion_matrix and accuracy_score
nb_conf_metrics = confusion_matrix(y_test,nb_predict)
nb_acc_metrics = accuracy_score(y_test,nb_predict)
print(nb_conf_metrics)
print(nb_acc_metrics* 100)

#Random Forest Classfiers 
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix,accuracy_score
Rc = RandomForestClassifier()
Rc.fit(x_train,y_train)
Rc_predict = Rc.predict(x_test)

#Print confusion_matrix and accuracy_score
Rc_conf_metrics = confusion_matrix(y_test,Rc_predict)
Rc_acc_metrics = accuracy_score(y_test,Rc_predict)
print(Rc_conf_metrics)
print(Rc_acc_metrics * 100)

#SVM Classifier
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, accuracy_score
sc = SVC()
sc.fit(x_train,y_train)
sf_predict = sc.predict(x_test)

#Print the cnfusion metrics and accuracy_score
sc_conf_metrics = confusion_matrix(y_test,sf_predict)
sc_acc_metrics  =accuracy_score(y_test,sf_predict)
print(sc_conf_metrics)
print(sc_acc_metrics * 100)

#Liner Kernal 
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix, accuracy_score
sc = SVC(kernel='linear')
sc.fit(x_train,y_train)
sf_predict = sc.predict(x_test)

sc_conf_metrics = confusion_matrix(y_test,sf_predict)
sc_acc_metrics  =accuracy_score(y_test,sf_predict)
print(sc_conf_metrics)
print(sc_acc_metrics * 100)

